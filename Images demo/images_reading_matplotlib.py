import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Get image in color
# img = cv.imread('./action.jpg', cv.IMREAD_COLOR)
# Get image in gray scale
img = cv.imread('./action.jpg', cv.IMREAD_GRAYSCALE)

# Show image in window normal not in the image original dimensions
cv.namedWindow('image', cv.WINDOW_NORMAL)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
