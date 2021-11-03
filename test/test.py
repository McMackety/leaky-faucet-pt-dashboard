import serial
import time
import math

def generateDigit(j):
    return math.sin(j + time.time()) * 500

port = 'COM2'
baud = 115200
testDigit = str(100)
printout = testDigit.encode()

ser = serial.Serial(port, baud)
print(ser.name)

stop_time = time.time() + 10
while True:
    for j in range(0, 8):
        ser.write(str(abs(round(generateDigit(j), 2))).encode() + b',')

    ser.write(b'\n')

    time.sleep(0.1)
    if time.time() > stop_time:
        break