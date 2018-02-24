#!usr/bin/env python3

import numpy as np
import cv2

x1, x2, y1, y2 = 100, 100, 300, 300

cap = cv2.VideoCapture(0)

while(True):
    #capture frame-by-frame
    ret, image = cap.read()

    #Operate on the frame
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.rectangle(image, (x1, y1), (x2,y2),(0,255,0),2)
    
    subIm = image[y1:y2, x1:x2]

    #display the result
    cv2.imshow('frame',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#When everything else is done release the capture
cap.release()
cv2.destroyAllWindows()
