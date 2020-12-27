import cv2

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

cap.set(4, 24)
cap.set(5, 35)

print(cap.get(4))
print(cap.get(5))
while(cap.isOpened()) :
    ret, frame = cap.read()
    if ret == True :

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord ('q') :
            break
    else :
            break

cap.release ()
cv2.destroyAllWindows()