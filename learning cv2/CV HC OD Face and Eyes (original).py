import cv2
import numpy as np
import os

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,255), 4)
        roi_gray = gray[x:x+w, y:y+h]
        roi_img = img[x:x+w, y:y+h]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_img, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)
            os.system('say face detected.')
        #img = cv2.Canny(img[x:x+w, y:y+h], 150, 150)

    #img = cv2.resize(img, (600,350))
    img=cv2.flip(img,1)
    cv2.imshow('image', img)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
