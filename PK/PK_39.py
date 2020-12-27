import numpy as np
import cv2 as cv
cap = cv.VideoCapture('vtest.avi')
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=False)
fgbg2 = cv.createBackgroundSubtractorMOG2(detectShadows=True)
fgbg4 = cv.createBackgroundSubtractorKNN()

while True :
    ret, frame = cap.read()
    if frame is None :
        break
    fgmask = fgbg.apply(frame)
    fgmask3 = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)
    fgmask2 = fgbg2.apply(frame)
    fgmask4 = fgbg4.apply(frame)

    cv.imshow('Frame', frame)
    cv.imshow('FGmask', fgmask)
    cv.imshow('FGmask2', fgmask2)
    cv.imshow('FGmask3', fgmask3)
    cv.imshow('FGmask4', fgmask4)

    keyboard = cv.waitKey(10)
    if keyboard == 'q' or keyboard == 27:
        break
cap.release()
cv.destroyAllWindows()
