import serial
import threading
import time

com_port = "COM3"
baud_rate = 115200

class RocketSerial(threading.Thread):
    def __init__(self):
        self.data = []
        self.should_stop = False
        self.serial = serial.Serial(com_port, baud_rate, timeout=1)
        threading.Thread.__init__(self)

    def read_data(self):
        return self.data

    def stop(self):
        self.should_stop = True

    def run(self):
        while True:
            if self.should_stop:
                return
            data = self.serial.readline()
            array = data.decode("utf-8") .split(',')
            array.pop()
            self.data = array