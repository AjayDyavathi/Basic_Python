import cv2
import numpy as np
import matplotlib.pyplot as plt

#                                    0
img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR  = 1
#IMREAD_UNCHANGED  = -1

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.plot([20,10],[300,400], 'c',5)
plt.show()

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('watchgray.jpg', img)
