import matplotlib
import numpy as np
import cv2

    
img = cv2.imread("3.jpg")
height, width = img.shape[0:2]

#                cv2.getRotationMatrix2D(center, angle, scale)
rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)


newImg = cv2.resize(img, (0,0), fx=0.75, fy=0.75)

gray = cv2.cvtColor(newImg, cv2.COLOR_BGR2GRAY)
inverted_img = 255-gray
blur=cv2.blur(inverted_img,(5,5))



img_blend= cv2.divide(gray, 255-blur, scale=256)
f=cv2.cvtColor(img_blend, cv2.COLOR_GRAY2BGR)
logo= cv2.divide(gray, 155-blur, scale=256)
cv2.imshow('logo Image', logo)
cv2.imshow('gray Image', gray)
cv2.imshow('inverted Image', inverted_img)
cv2.imshow('drawing Image', f)

cv2.imwrite('./img/logoImage.jpg', logo) 
cv2.imwrite('./img/grayImage.jpg', gray) 
cv2.imwrite('./img/invertedImage.jpg', inverted_img) 
cv2.imwrite('./img/drawingImage.jpg', f) 

cv2.waitKey(0)
'''cv2.imshow('Original Image', img) 
cv2.waitKey(0)'''