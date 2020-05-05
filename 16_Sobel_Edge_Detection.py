import cv2 
import numpy as np 
scale = 1
delta = 0
ddepth = cv2.CV_16S
cap = cv2.VideoCapture('3_&_4_ip.mp4') #for livestream, argument=0 
  
while(1): 
  
    # Take each frame 
    _, src = cap.read() 
    src = cv2.GaussianBlur(src, (3, 3), 0)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    grad_x = cv2.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    grad_y = cv2.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    # Convert to HSV for simpler calculations 

    cv2.imshow('Sobel',grad) 
    k = cv2.waitKey(5) & 0xFF
    if k == 27: 
        break
  
cv2.destroyAllWindows() 
  
#release the frame 
cap.release() 