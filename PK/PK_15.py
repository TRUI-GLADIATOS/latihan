import cv2
import numpy as np

img = cv2.imread ('sudoku.png', 0)
_, hehe = cv2.threshold(img, 127,255, cv2.THRESH_BINARY)
haha = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, )

cv2.imshow("image", img)
cv2.imshow("hehe", hehe)

cv2.waitKey(0)
cv2.destroyAllWindows()