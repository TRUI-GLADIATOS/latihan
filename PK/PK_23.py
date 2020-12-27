#find contours and draw it
import numpy as np
import cv2

logo = cv2.imread('opencv-logo.png')
logogray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(logogray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Banyak contours =" +str(len(contours)))
print(contours[0])

cv2.drawContours(logo, contours, -1, (0,255,0), 3)

cv2.imshow('logo', logo)
cv2.imshow('logo GRAY', logogray)
cv2.waitKey(0)
cv2.destroyAllWindows()