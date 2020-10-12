import matplotlib
import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #height, width = img.shape[0:2]
    '''width = img.get(cv2.CAP_PROP_FRAME_WIDTH )
    height = img.get(cv2.CAP_PROP_FRAME_HEIGHT )
    rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)
    newImg = cv2.resize(img, (0,0), fx=0.75, fy=0.75)
    gray = cv2.cvtColor(newImg, cv2.COLOR_BGR2GRAY)
    inverted_img = 255-gray
    blur=cv2.blur(inverted_img,(5,5))
    img_blend= cv2.divide(gray, 255-blur, scale=256)
    f=cv2.cvtColor(img_blend, cv2.COLOR_GRAY2BGR)'''
    cv2.imshow('drawing', frame)
    cv2.waitKey(0)

cap.release() 
   
# Closes all the frames 
cv2.destroyAllWindows() 