import cv2 
cap = cv2.VideoCapture(0) 
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG() #alterantively, cv2.createBackgroundSubtractorMOG2()
test = 'Motion detected'
while(1): 
    ret, frame = cap.read() 
    fgmask = fgbg.apply(frame) 
    (contours,hierarchy)=cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>500):
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
            cv2.putText(frame, "Message={}".format(test), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow('fgmask', frame) 
    cv2.imshow('frame', fgmask)    
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
cap.release() 
cv2.destroyAllWindows() 
