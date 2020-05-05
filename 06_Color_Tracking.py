import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while(1):
        _, img = cap.read()

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_red = np.array([0,120,70])
        lower_blue = np.array([110,50,50])
        upper_red = np.array([10,255,255])
        upper_blue = np.array([130,255,255])
        #finding the range yellow colour in the image
        red = cv2.inRange(hsv, lower_red, upper_red)
        kernal = np.ones((5 ,5), "uint8")

        blue=cv2.dilate(red, kernal)

        res=cv2.bitwise_and(img, img, mask = red)

        #Tracking Colour (Red) 
        (contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area>300):
                        
                        x,y,w,h = cv2.boundingRect(contour)     
                        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
                        
        cv2.imshow("Color Tracking",img)
        img = cv2.flip(img,1)
        cv2.imshow("Red",res)
                               
        if cv2.waitKey(10) & 0xFF == 27:
                cap.release()
                cv2.destroyAllWindows()
                break
