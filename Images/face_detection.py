import numpy as np
import cv2 as opencv
face_cascade = opencv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = opencv.CascadeClassifier('haarcascade_eye.xml')
img = opencv.imread('/Users/juan/anaconda3/lib/python3.7/site-packages/pyparrot/images/visionStream.jpg')
gray = opencv.cvtColor(img, opencv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# For each face
for (x, y, w, h) in faces:
    # Draw a black rectangle
    img = opencv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y : y + h, x : x + w]
    roi_color = img[y : y + h, x : x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)

    # For each eye
    for (ex, ey, ew, eh) in eyes:
        if (ey + ey + eh) / 2 < (y + y + h) / 4:
            # Draw a green rectangle
            opencv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            font = opencv.FONT_HERSHEY_SIMPLEX
            opencv.putText(img, 'BLINK', (500, 700), font, 4, (255,255,255), 2, opencv.LINE_AA)
# Set the window size
opencv.namedWindow('img', opencv.WINDOW_NORMAL)
opencv.imshow('img',img)
opencv.waitKey(0)
opencv.destroyAllWindows()
