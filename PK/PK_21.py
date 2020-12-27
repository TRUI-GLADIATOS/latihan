import cv2
import numpy as n


img = cv2.imread('lena.jpg')
pd = cv2.pyrDown(img) #decrease resolution
pu = cv2.pyrUp(img) #increase resolution
#the resolution will be changed

cv2.imshow('lena', img)
cv2.imshow('lena1', pd)
cv2.imshow('lena2', pu)

cv2.waitKey(0)
cv2.destroyAllWindows()