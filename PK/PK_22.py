import cv2
import numpy as n

apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')
print(apple.shape)
print(orange.shape)
apeljeruk = n.hstack((apple[:, :256], orange[:, 256:]))

#generate gaussian pyramid buat apel
gpapel = apple.copy()
gp_apel = (gpapel)
for i in range (6) :
    gpapel = cv2.pyrDown(gpapel)
    gp_apel.append(gpapel)

#generate gaussian pyramid buat jeruk
gpjeruk = orange.copy()
gp_jeruk = (gpjeruk)
for i in range (6) :
    gpjeruk = cv2.pyrDown(gpjeruk)
    gp_jeruk.append(gpjeruk)

#generate laplacian pyramid buat apel
lpapel = gp_apel[5] #level=
lp_apel = [gpapel]
for i in range (5,0,-1):
    gaussian = cv2.pyrUp(gp_apel[i])
    laplacian = cv2.substract(gp_apel[i-1], gaussian)
    lp_apel.append(laplacian)

#generate laplacian pyramid buat apel
lpjeruk = gp_jeruk[5] #level=
lp_jeruk = [gpjeruk]
for i in range (5,0,-1):
    gaussian = cv2.pyrUp(gp_jeruk[i])
    laplacian = cv2.substract(gp_jeruk[i-1], gaussian)
    lp_jeruk.append(laplacian)

#taro stengah-stengah image setiap level
apeljerukpiramid = []
n = 0
for apellap, jeruklap in zip(lapapel, lapjeruk) :
    n +=1
    cols, rows, ch = apellap.shape
    laplacian = n.hstack((apellap[:, 0:int(cols/2)], orangelap[:, int(cols/2):]))
    apeljerukpiramid.append(laplacian)



cv2.imshow("apel", apple)
cv2.imshow("jeruk", orange)
cv2.imshow("stengah apel, stengah jeruk", apeljeruk)
cv2.waitKey(0)
cv2.destroyAllWindows()