import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512,512,3), np.uint8)
cv.rectangle(img,(0,0),(200,200),(0,255,0),3)
while(1):
    cv.imshow('image', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()
