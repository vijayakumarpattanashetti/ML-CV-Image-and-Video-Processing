# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 18:52:24 2019

@author: ASUS
"""

import cv2
import numpy as np

image = cv2.imread('9_ip.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((10, 1), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)

cv2MajorVersion = cv2.__version__.split(".")[0]
if int(cv2MajorVersion) >= 4:
    ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
else:
    im2, ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

for i, ctr in enumerate(sorted_ctrs):
    x, y, w, h = cv2.boundingRect(ctr)

    roi = image[y:y + h, x:x + w]

    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        
img1 = np.hstack((gray,thresh,img_dilation))
cv2.imshow("Gray, Threshold, Dilated",img1)
cv2.imshow("ROI Extracted",image)
cv2.waitKey(0)