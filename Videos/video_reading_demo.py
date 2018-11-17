import numpy as np
import cv2 as cv

# Load the video
cap = cv.VideoCapture('./CR7_goal.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    # Define the video format
    video = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Set the window size
    cv.namedWindow('frame', cv.WINDOW_NORMAL)

    # Show the video
    cv.imshow('frame', video)

    # Exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
