# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:30:00 2020

@author: vijayakumar_p

#frame rate is 25fps
import cv2
myv=cv2.VideoCapture('a.mp4')
fr=myv.get(cv2.CAP_PROP_FPS)

img = cv2.imread('1.jpg')
hsi = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
acpr=np.average(hsi,axis=0)
ac=np.average(acpr,axis=0)

"""
import numpy as np
import cv2
import matplotlib.pyplot as plt
import scipy
from scipy import signal

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('a.mp4')
nhr=[]
l=0
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        img=roi_color
        acpr=np.average(img,axis=0)
        ac=np.average(acpr,axis=0)
        ans=np.average(ac,axis=0)
        nhr.append(ans)
        l+=1
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

print(l)
nhr=scipy.signal.detrend(nhr,type='linear')
#nhr=scipy.signal.hamming(128)
peaks=scipy.signal.find_peaks(nhr) #rel_height=0.5
print(len(peaks))
plt.plot(nhr)
plt.show()

cap.release()
cv2.destroyAllWindows()