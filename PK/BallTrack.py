import cv2
import numpy as np
import serial

# ser = serial.Serial("/dev/OpenCM9.04", 9600)  # Open port with baud rate
# data = 0

cap = cv2.VideoCapture(0)
# Set camera resolution
cap.set(3, 480)  # 3,480
cap.set(4, 320)  # 4,320
_, frame = cap.read()
rows, cols, _ = frame.shape

x_medium = int(cols / 2)
center = int(cols / 2)
position = 90  # degrees

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    # red color
    low_red = np.array([135, 47, 125])
    high_red = np.array([255, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    blur = cv2.blur(red_mask, (10, 10), 0)
    ret, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)
    thresh = cv2.erode(thresh, None, iterations=2)
    dilate = cv2.dilate(thresh, None, iterations=5)
    contours, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)

        x_medium = int((x + x + w) / 2)
        break

    cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)

    # Move servo motor
    if x_medium < center - 40:
        position += 2

    if x_medium > center + 40:
        position -= 2

    if position > 180:
        position = 180
    if position < 10:
        position = 10

    cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
    print(x_medium, position)

    if position < 100:
        #ser.write('0' + str.encode(str(position)))
        print (position)

    elif position < 10:
        #ser.write('0' + '0' + str.encode(str(position)))
        print(position)

    else:
        #ser.write(str.encode(str(position)))
        print(position)

    cv2.imshow("Frame", frame)
    cv2.imshow("dilate", dilate)
    cv2.imshow("blur", blur)
    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()