# -*- coding: utf-8 -*-
"""
@author: vijayakumar_p
"""

from PIL import Image
import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

co = []
cropping = False
def crop(event, x, y, flags, param):
	global co, cropping
	if event == cv2.EVENT_LBUTTONDOWN:
		co = [(x, y)]
		cropping = True
	elif event == cv2.EVENT_LBUTTONUP:
		co.append((x, y))
		cropping = False
		cv2.rectangle(img, co[0], co[1], (0, 255, 0), 2)
		cv2.imshow("image", img)
path=str(input("Enter path to image: "))
img = cv2.imread(path)
imgc = img.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", crop)
while True:
	cv2.imshow("image", img)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"): #reset ROI
		image = imgc.copy()
	elif key == ord("s"): #select ROI
		break
if len(co) == 2:
	roi = imgc[co[0][1]:co[1][1], co[0][0]:co[1][0]]
	cv2.imwrite("target.jpg", roi)  
cv2.destroyAllWindows()

img = Image.open('target.jpg')
ei = pytesseract.image_to_string(img)
print(ei)