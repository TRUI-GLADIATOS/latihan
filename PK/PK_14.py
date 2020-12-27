import cv2
import numpy as np

img = cv2.imread ('bolarubot7.jpg', 1)
_, hehe = cv2.threshold(img, 10,100, cv2.THRESH_BINARY)
_, hehe1 = cv2.threshold(img, 100,200, cv2.THRESH_BINARY_INV)
_, hehe2 = cv2.threshold(img, 250,255, cv2.THRESH_TRUNC)
_, hehe3 = cv2.threshold(img, 127,127, cv2.THRESH_TOZERO)
_, hehe4 = cv2.threshold(img, 127,127, cv2.THRESH_TOZERO_INV)

cv2.imshow("image", img)
cv2.imshow("hehe", hehe)
cv2.imshow("hehe1", hehe1)
cv2.imshow("hehe2", hehe2)
cv2.imshow("hehe3", hehe3)
cv2.imshow("hehe4", hehe4)

cv2.waitKey(0)
cv2.destroyAllWindows()