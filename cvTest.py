#!usr/bin/env python3

import numpy as np
import cv2

x1, y1, x2, y2 = 50, 100, 250, 300

cap = cv2.VideoCapture(0)

cap.set(3, 800)
cap.set(4, 600)

while(True):
    #capture frame-by-frame
    ret, image = cap.read()
    image = cv2.flip(image, 1)   
    #Operate on the frame
#    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
    
    subIm = image[y1:y2, x1:x2]

    #display the result
    cv2.imshow('frame', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#When everything else is done release the capture
cap.release()
cv2.destroyAllWindows()
