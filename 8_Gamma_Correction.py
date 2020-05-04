# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 18:41:19 2019

@author: ASUS
"""

import cv2
import numpy as np

def adjust_gamma(image, gamma=1.0):

   invGamma = 1.0 / gamma
   table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")

   return cv2.LUT(image, table)

x = '5_op(pic_0).png'  #image
img = cv2.imread(x, 1)
width = int(img.shape[1] * 0.5)
height = int(img.shape[0] * 0.5)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cv2.imshow('original',resized)

gamma = 0.5
adjusted = adjust_gamma(resized, gamma=gamma)
cv2.putText(adjusted, "g={}".format(gamma), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
cv2.imwrite('gamma_correct.jpg',adjusted)
cv2.imshow("gamma image 1", adjusted)

cv2.waitKey(0)
cv2.destroyAllWindows()