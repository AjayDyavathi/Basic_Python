import cv2
import time

filename = time.strftime("%m-%d-%H-%M-%S") + '.avi'
fps = 16

cap = cv2.VideoCapture(0)

#in this way it always works, because your get the right "size"
size = (int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.cv.FOURCC('8', 'B', 'P', 'S')     #works, large
out = cv2.VideoWriter(filename, fourcc, fps, size, True)

#in this way, you must set the "size" to your size, 
#because you don't know the default "size" is right or not
#cap.set(3, 640)
#cap.set(4, 480)
#out = cv2.VideoWriter(filename, fourcc, fps, (640, 480), True)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    else:
        print ('Error...')
        break

cap.release()
out.release()
cv2.destroyAllWindows()
