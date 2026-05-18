import cv2

# Corrected image path relative to the script's location
img_path = 'Images/your_image.jpg'  # Replace with your image path

# Load the image from file
img = cv2.imread(img_path)

if img is None:
    print(f"Error: Unable to read image '{img_path}'.")
else:
    # Convert the image to grayscale
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display the grayscale image in a window
    cv2.imshow('Grayscale Image', grayscale_img)

    # Wait for any key press to close the window
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()

edge_detection_opencv.py
import cv2

# Corrected image path relative to the script's location
img_path = 'Images/your_image.jpg'  # Replace with your image path

# Load the image from file
img = cv2.imread(img_path)

if img is None:
    print(f"Error: Unable to read image '{img_path}'.")
else:
    # Convert the image to grayscale for better edge detection
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(grayscale_img, 100, 200)  # Adjust thresholds for better results

    # Display the edge-detected image in a window
    cv2.imshow('Edges', edges)

    # Wait for any key press to close the window
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
face_detection_opencv.py
import cv2

# Load the Haar cascade classifier for face detection (download from OpenCV website)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Corrected image path relative to the script's location
img_path = 'Images/your_image.jpg'  # Replace with your image path

# Load the image from file
img = cv2.imread(img_path)

if img is None:
    print(f"Error: Unable to read image '{img_path}'.")
else:
    # Convert the image to grayscale for better face detection
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(grayscale_img)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the image with detected faces in a window
    cv2.imshow('Face Detection', img)

    # Wait for any key press to close the window
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()


