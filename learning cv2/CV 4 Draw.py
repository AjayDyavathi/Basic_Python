import cv2
import numpy as np

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150,150), (0,0,255), 15)
cv2.rectangle(img, (20,20), (300,300), (0,255,0), 5)
cv2.circle(img, (100,300),50, (255,0,0),-1)

pts=np.array([[50,50], [200,30], [150,100], [200,400]], np.int32)
#pts=pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (56,90,255), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Ajay', (10,130), font, 1, (200,5,0), 2, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
