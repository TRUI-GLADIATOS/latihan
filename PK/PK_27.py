# template matching
# search and find the location of template inside larger images
#template must be smaller than the real image

import cv2
import numpy as np

aka = cv2.imread("akatsuki.jpg")
greyaka = cv2.cvtColor(aka, cv2.COLOR_BGR2GRAY)
pain = cv2.imread("pain.jpg",0) #the template should grey
w,h = pain.shape[::-1]

ha = cv2.matchTemplate(greyaka, pain, cv2.TM_CCOEFF_NORMED)
print(ha)
thr = 0.95 ;
loc = np.where(ha >= thr)
print (loc)
for pt in zip(*loc[::-1]):
    cv2.rectangle(aka, pt, (pt[0] + w, pt[1] + h), (0,255,0), 5)


cv2.imshow("pain", pain)
cv2.imshow("akatsuki", aka)
cv2.waitKey(0)
cv2.destroyAllWindows()
