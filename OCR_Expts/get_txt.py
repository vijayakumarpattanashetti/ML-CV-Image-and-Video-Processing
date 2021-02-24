# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:33:32 2020

@author: vijayakumar_p

"""

from PIL import Image
import pytesseract
import numpy as np
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img=Image.open('3.jpeg')
#img = cv2.imread('28.jpeg')
#width = int(img.shape[1] * 150 / 100)
#height = int(img.shape[0] * 300 / 100)
#dim = (width, height)
#img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#th1,img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY) #150 THRESHOLD
img=np.array(img.convert('L').resize((256, 256)))
#img=cv2.blur(img,(5,5))
#kernel = np.ones((3,4),np.uint8)
#img = cv2.erode(img,kernel,iterations = 4)
#img=cv2.blur(img,(3,1))
#cv2.imwrite('bp.jpg',img)

ei=pytesseract.image_to_string(img)
print(ei)