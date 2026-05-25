# autonomous_demo.py
import cv2
import numpy as np
import torch
from ultralytics import YOLO  # requires 'ultralytics' package (YOLOv8). In alternativa usare yolov5 repo.
import networkx as nx
import math
from collections import deque

# ---------- CONFIG ----------
IMAGE_PATH = "Images/your_image.jpg"
YOLO_MODEL = "yolov8n.pt"  # scarica modello YOLOv8 nano o usa path locale
DETECTION_CLASSES = {"person": "pedestrian", "car": "vehicle", "bicycle": "cyclist", "motorbike": "vehicle"}  # mappatura semplificata
OCC_GRID_SIZE_M = (50, 50)  # metri area coperta (x, y)
GRID_RESOLUTION = 0.5  # metri per cella
# ----------------------------

# ---------- 1) Obstacle detection & classification ----------
class ObstacleDetector:
    def __init__(self, model_path=YOLO_MODEL, device=None):
        self.model = YOLO(model_path) if model_path else None
        if device:
            self.model.to(device)

    def detect(self, image, conf_thresh=0.25):
        """
        Returns list of detections: dict with bbox, score, label (mapped), raw_label
        bbox in (x1,y1,x2,y2)
        """
        results = self.model.predict(image, conf=conf_thresh, verbose=False)[0]
        dets = []
        for box, score, cls in zip(results.boxes.xyxy.cpu().numpy(),
                                   results.boxes.conf.cpu().numpy(),
                                   results.boxes.cls.cpu().numpy()):
            raw_label = self.model.names[int(cls)]
            label = DETECTION_CLASSES.get(raw_label, None)
            if label:
                dets.append({
                    "bbox": tuple(map(int, box)),
                    "score": float(score),
                    "raw_label": raw_label,
                    "label": label
                })
        return dets

    def draw(self, image, dets):
        for d in dets:
            x1,y1,x2,y2 = d["bbox"]
            cv2.rectangle(image, (x1,y1), (x2,y2), (0,255,0), 2)
            txt = f"{d['label']}:{d['score']:.2f}"
            cv2.putText(image, txt, (x1, y1-6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
        return image

# ---------- 2) Lane segmentation / detection ----------
class LaneDetector:
    def __init__(self):
        pass

    def preprocess(self, img):
        h, w = img.shape[:2]
        # Region of interest mask (lower half)
        mask = np.zeros_like(img[:,:,0])
        polygon = np.array([[
            (0, h),
            (w, h),
            (w, int(h*0.6)),
            (0, int(h*0.6))
        ]], np.int32)
        cv2.fillPoly(mask, polygon, 255)
        return mask

    def detect_lines(self, img):
        # Convert to grayscale, blur, Canny
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        edges = cv2.Canny(blur, 50, 150)

        # Mask region
        mask = self.preprocess(img)
        edges = cv2.bitwise_and(edges, mask)

        # Hough transform to find lines
        lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=50, minLineLength=50, maxLineGap=150)
        left_lines, right_lines = [], []
        h, w = img.shape[:2]
        if lines is None:
            return img, None

        for l in lines:
            x1,y1,x2,y2 = l[0]
            # filter near-vertical/horizontal
            if x2==x1: continue
            slope = (y2-y1)/(x2-x1)
            if abs(slope) < 0.3: continue
            if slope < 0:
                left_lines.append((x1,y1,x2,y2))
            else:
                right_lines.append((x1,y1,x2,y2))

        def avg_line(lines):
            if not lines: return None
            x_coords = []
            y_coords = []
            for x1,y1,x2,y2 in lines:
                x_coords += [x1,x2]
                y_coords += [y1,y2]
            # fit line y = m x + b
            m, b = np.polyfit(x_coords, y_coords, 1)
            y1 = h
            y2 = int(h*0.6)
            x1 = int((y1 - b) / m)
            x2 = int((y2 - b) / m)
            return (x1,y1,x2,y2)

        left_avg = avg_line(left_lines)
        right_avg = avg_line(right_lines)

        out = img.copy()
        if left_avg:
            cv2.line(out, (left_avg[0],left_avg[1]), (left_avg[2],left_avg[3]), (0,0,255), 6)
        if right_avg:
            cv2.line(out, (right_avg[0],right_avg[1]), (right_avg[2],right_avg[3]), (0,0,255), 6)

        # compute vehicle offset from lane center (very rough)
        offset = None
        if left_avg and right_avg:
            lane_center_x = ( (left_avg[0]+left_avg[2]) / 2 + (right_avg[0]+right_avg[2]) / 2 )/2
            vehicle_center_x = w/2
            offset = (vehicle_center_x - lane_center_x)  # pixels; + means vehicle is right of lane center
            cv2.putText(out, f"Offset px: {int(offset)}", (30,30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)
        return out, offset

# ---------- 3) Simple occupancy grid mapping + A* navigation ----------
class OccupancyGridMap:
    def __init__(self, size_m=OCC_GRID_SIZE_M, resolution=GRID_RESOLUTION):
        self.size_m = size_m
        self.resolution = resolution
        self.w = int(size_m[0] / resolution)
        self.h = int(size_m[1] / resolution)
        self.grid = np.zeros((self.h, self.w), dtype=np.uint8)  # 0 free, 1 occupied

    def world_to_grid(self, x, y):
        # assume origin at center-left bottom; for demo assume car at center-bottom
        gx = int((x + self.size_m[0]/2) / self.resolution)
        gy = int((self.size_m[1] - y) / self.resolution)
        return gx, gy

    def mark_obstacle_bbox(self, bbox, image_shape, max_distance_m=50.0):
        """
        Simple projection: assume camera faces forward, map bbox bottom center to world coordinate using a rough pinhole model.
        This is highly approximate—just for demo.
        """
        h_img, w_img = image_shape[:2]
        x1,y1,x2,y2 = bbox
        bx = (x1 + x2)/2
        by = y2  # bottom
        # normalize
        nx = (bx - w_img/2) / (w_img/2)  # -1..1
        ny = (h_img - by) / h_img  # 0..1 (closer => larger)
        # estimate distance in meters (crude)
        dist = max_distance_m * (1 - ny)
        # assume object lies dist meters ahead, lateral offset proportional to nx
        world_x = dist  # forward
        world_y = -nx * (self.size_m[0]/2)  # lateral
        gx, gy = self.world_to_grid(world_y + self.size_m[0]/2, world_x)  # adjust to grid coords
        if 0 <= gx < self.w and 0 <= gy < self.h:
            self.grid[gy-1:gy+2, gx-1:gx+2] = 1  # mark small occupied area

    def to_visual(self):
        vis = (1 - self.grid) * 255  # free white, occupied black
        vis = cv2.resize(vis, (self.w*4, self.h*4), interpolation=cv2.INTER_NEAREST)
        vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)
        return vis

def a_star(grid, start, goal):
    h, w = grid.shape
    def heuristic(a,b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    open_set = []
    import heapq
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, None))
    came_from = {}
    gscore = {start: 0}
    visited = set()
    while open_set:
        f, g, current, parent = heapq.heappop(open_set)
        if current in visited: continue
        visited.add(current)
        came_from[current] = parent
        if current == goal:
            # reconstruct path
            path = []
            cur = current
            while cur:
                path.append(cur)
                cur = came_from[cur]
            path.reverse()
            return path
        cx, cy = current
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nxp = cx+dx; nyp = cy+dy
            if 0 <= nxp < w and 0 <= nyp < h and grid[nyp, nxp] == 0:
                ng = g + 1
                if (nxp,nyp) not in gscore or ng < gscore[(nxp,nyp)]:
                    gscore[(nxp,nyp)] = ng
                    heapq.heappush(open_set, (ng + heuristic((nxp,nyp), goal), ng, (nxp,nyp), current))
    return None

# ---------- Main demo pipeline ----------
def main():
    img = cv2.imread(IMAGE_PATH)
    if img is None:
        print("Cannot load image:", IMAGE_PATH)
        return

    det = ObstacleDetector()
    lanes = LaneDetector()
    ogm = OccupancyGridMap()

    # 1) detect obstacles
    dets = det.detect(img, conf_thresh=0.25)
    img_det = det.draw(img.copy(), dets)

    # 2) lane detection
    lane_vis, offset = lanes.detect_lines(img_det)

    # 3) map obstacles into occupancy grid
    for d in dets:
        ogm.mark_obstacle_bbox(d["bbox"], img.shape)
    grid_vis = ogm.to_visual()

    # plan simple path from bottom-center of grid to a goal ahead (example)
    start = (ogm.w//2, ogm.h-1)
    goal = (ogm.w//2, ogm.h//3)  # somewhere ahead
    path = a_star(ogm.grid, start, goal)
    if path:
        # draw path on occupancy vis
        pv = grid_vis.copy()
        scale = 4
        for (gx, gy) in path:
            cv2.circle(pv, (gx*scale, gy*scale), 3, (0,0,255), -1)
    else:
        pv = grid_vis.copy()

    # show outputs
    cv2.imshow("Detections + Lanes", lane_vis)
    cv2.imshow("Occupancy Grid + Path", pv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
