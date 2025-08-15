import cv2
import os

# Method 1: Use the full path to the cascade file (recommended)
# This gets the path from OpenCV's data directory
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

# Method 2: Alternative - check if cascade loaded properly
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# if face_cascade.empty():
#     print("Error: Could not load cascade classifier")
#     exit()

webcam = cv2.VideoCapture(0)

# Check if webcam is opened
if not webcam.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    ret, img = webcam.read()
    
    # Check if frame was read successfully
    if not ret:
        print("Error: Could not read frame")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow("Face Detection", img)
    key = cv2.waitKey(10) & 0xFF
    if key == 27:  # ESC key
        break

webcam.release()
cv2.destroyAllWindows()
