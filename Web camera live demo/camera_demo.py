import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Open camera in gray mode
    camera = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Open camera in color mode
    # camera = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)

    # Display the resulting frame
    cv.imshow('frame', camera)

    # Exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
