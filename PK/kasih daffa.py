import serial


#Serial Communication Initialization
#ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate
#ser = serial.Serial ("COM13", 9600)

import time

while True:
    delay = 60 / 12  ###for 5 seconds delay
    close_time = time.time() + delay
    while True:
        print("Forward!")
        data = 'G'
        if time.time() > close_time:
            break

    delay = 60 / 12  ###for 5 seconds delay
    close_time = time.time() + delay
    while True:
        print("Right!")
        data = 'R'
        if time.time() > close_time:
            break

    delay = 60 / 12  ###for 5 seconds delay
    close_time = time.time() + delay
    while True:
        print("Forward!")
        data = 'G'
        if time.time() > close_time:
            break

    delay = 60 / 12  ###for 5 seconds delay
    close_time = time.time() + delay
    while True:
        print("Right!")
        data = 'R'
        if time.time() > close_time:
            break

    delay = 60 / 12  ###for 5 seconds delay
    close_time = time.time() + delay
    while True:
        print("Forward!")
        data = 'G'
        if time.time() > close_time:
            break

#    if (data1 != data):
#        data1 = data
        # Mengirim data secara serial
#        ser.write(str.encode(data1))
    break