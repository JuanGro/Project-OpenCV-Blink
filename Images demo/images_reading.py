import numpy as np
import cv2 as cv

# Get image in color
# img = cv.imread('./action.jpg', cv.IMREAD_COLOR)
# Get image in gray scale
img = cv.imread('./action.jpg', cv.IMREAD_GRAYSCALE)
# img = cv.imread('./action.jpg', cv.IMREAD_UNCHANGED)

# Show image in window normal not in the image original dimensions
cv.namedWindow('image', cv.WINDOW_NORMAL)

# Show the image
cv.imshow('image', img)

# Wait infenitely if is zero
k = cv.waitKey(0)

# wait for ESC key to exit
if k == 27:
    cv.destroyAllWindows()

# wait for 's' key to save and exit
elif k == ord('s'):
    # Save image
    cv.imwrite('image_output.png', img)
    cv.destroyAllWindows()
