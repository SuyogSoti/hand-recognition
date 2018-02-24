#!usr/bin/env python3

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    #capture frame-by-frame
    ret, frame = cap.read()

    #Operate on the frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #display the result
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#When everything else is done release the capture
cap.release()
cv2.destroyAllWindows()
