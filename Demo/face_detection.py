import numpy as np
import cv2 as opencv

# Images to identify faces
face_cascade = opencv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = opencv.CascadeClassifier('haarcascade_eye.xml')

# Start camera capturing
cap = opencv.VideoCapture(0)

single_blink = 0
double_blink = 0

while(True):
    # Capture frame-by-frame
    ret, img = cap.read()

    if (ret == 1):
        # Video format
        gray = opencv.cvtColor(img, opencv.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # For each face
        for (x, y, w, h) in faces:
            # Draw a black rectangle
            img = opencv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            roi_gray = gray[y : y + h, x : x + w]
            roi_color = img[y : y + h, x : x + w]

            eyes = eye_cascade.detectMultiScale(roi_gray)

            # If detect a blink
            if len(eyes) >= 2:
                single_blink = 0
                double_blink = 0
            elif len(eyes) == 1:
                single_blink += 1
                double_blink = 0
            elif len(eyes) == 0:
                single_blink = 0
                double_blink += 1

            if single_blink >= 2:
                font = opencv.FONT_HERSHEY_SIMPLEX
                opencv.putText(img, 'BLINK', (500, 700), font, 4, (255,255,255), 2, opencv.LINE_AA)
            # elif double_blink >= 3:
            #     font = opencv.FONT_HERSHEY_SIMPLEX
            #     opencv.putText(img, 'DOUBLE BLINK', (150, 700), font, 4, (255,255,255), 2, opencv.LINE_AA)

            # For each eye
            for (ex, ey, ew, eh) in eyes:
                # Draw a green rectangle
                opencv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # Set the window size
        opencv.namedWindow('frame', opencv.WINDOW_NORMAL)

        # Display the resulting frame
        opencv.imshow('frame', img)

        # Exit
        if opencv.waitKey(1) & 0xFF == ord('q'):
            break

# When everything done, release the capture
cap.release()
opencv.destroyAllWindows()
