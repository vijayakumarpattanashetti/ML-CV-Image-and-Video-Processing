# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:45:48 2019

@author: ASUS
"""

import cv2
import numpy as np;
 
cap = cv2.VideoCapture(0)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
while(1):
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.convertScaleAbs(frame)
    params = cv2.SimpleBlobDetector_Params()
    params.blobColor = 0
    params.filterByColor = True
    params.minArea = 0
    params.filterByArea = False
    params.minThreshold = 120;
    params.maxThreshold = 255;
    ver = (cv2.__version__).split('.')
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(frame)
    im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    if ret == True:
        cv2.imshow('frame', im_with_keypoints)
    else:
        cap.release()
        break
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()