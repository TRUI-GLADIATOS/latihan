import cv2
import numpy as np

jpg = cv2.imread('shapes.png')
jpggray = cv2.cvtColor(jpg, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(jpggray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours (thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours :
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    cv2.drawContours(jpg, [approx], 0, (0,255,0), 3)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3 :
        cv2.putText(jpg, "segitiga", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0))
    elif len(approx) == 4 :
        x, y, w, h = cv2.boundingRect(approx)
        aspectRatio = float (w)/h
        print (aspectRatio)
        if 0.95 <= aspectRatio <= 1.05 :
            cv2.putText(jpg, "persegi", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0))
        else aspectRatio >= 0.95 and aspectRaio <= 1.05
            cv2.putText(jpg, "persegi panjang", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0))
    elif len(approx) == 5 :
        cv2.putText(jpg, "segi5", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0))
    elif len(approx) == 10 :
        cv2.putText(jpg, "bintang", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0))
    else:
        cv2.putText(jpg, "lingkaran", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0))


cv2.imshow("shapes", jpg)
cv2.waitKey(0)
cv2.destroyAllWindows()