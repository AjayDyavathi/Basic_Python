import numpy as np
import cv2


img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

img[55,55] = [0,0,0]
#makes the [55,55] portion BLACK
px = img[55,55]

img[300:400, 100:200] = [0,0,255]

face = img[200:400,100:300]
img[0:200,0:200] = face


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.closeAllWindows()
