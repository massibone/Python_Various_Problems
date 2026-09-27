import cv2
import os
from datetime import datetime

# Percorso al classificatore Haar Cascade fornito con OpenCV
CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

def main(output_dir="captures", camera_index=0, scaleFactor=1.1, minNeighbors=5):
    os.makedirs(output_dir, exist_ok=True)

    face_cascade = cv2.CascadeClassifier(CASCADE_PATH)
    if face_cascade.empty():
        raise RuntimeError("Impossibile caricare il classificatore Haar Cascade.")

    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        raise RuntimeError("Impossibile aprire la webcam.")

    print("Premi [spazio] per salvare un'immagine, [q] per uscire.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=scaleFactor,
            minNeighbors=minNeighbors,
            minSize=(30, 30)
        )

        # Disegna riquadri intorno ai volti
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Mostra il numero di volti rilevati
        cv2.putText(frame, f"Volti: {len(faces)}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        cv2.imshow("Rilevamento facciale (Haar Cascade)", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == 32:  # barra spaziatrice
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(output_dir, f"capture_{ts}.png")
            cv2.imwrite(filename, frame)
            print(f"Immagine salvata: {filename}")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

