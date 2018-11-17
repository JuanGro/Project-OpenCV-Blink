import numpy as np
import cv2 as opencv

# Images to identify faces
face_cascade = opencv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = opencv.CascadeClassifier('haarcascade_eye.xml')

# Start camera capturing
cap = opencv.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, video = cap.read()

    if (ret == 1):
        # Video format
        gray = opencv.cvtColor(video, opencv.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # For each face
        for (x, y, w, h) in faces:
            # Draw a black rectangle
            video = opencv.rectangle(video, (x, y), (x + w, y + h), (255, 0, 0), 2)

            roi_gray = gray[y : y + h, x : x + w]
            roi_color = video[y : y + h, x : x + w]

            eyes = eye_cascade.detectMultiScale(roi_gray)

            eyes_count = 0

            # For each eye
            for (ex, ey, ew, eh) in eyes:
                if (ey + ey + eh) / 2 < (y + y + h) / 6:
                    print("face:", y, y + h, (y + y + h) / 2)
                    print("eye:", ey, ey + eh, (ey + ey + eh) / 2)
                    # Draw a green rectangle
                    opencv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                    eyes_count += 1

            # If detect a blink
            if eyes_count == 1:
                font = opencv.FONT_HERSHEY_SIMPLEX
                opencv.putText(video, 'BLINK', (500, 700), font, 4, (255,255,255), 2, opencv.LINE_AA)

        # Set the window size
        opencv.namedWindow('frame', opencv.WINDOW_NORMAL)

        # Display the resulting frame
        opencv.imshow('frame', video)

        # Exit
        if opencv.waitKey(1) & 0xFF == ord('q'):
            break

# When everything done, release the capture
cap.release()
opencv.destroyAllWindows()
