import serial
import threading
import io

com_port = "/dev/tty.usbmodem14401"
baud_rate = 115200

class RocketSerial(threading.Thread):
    def __init__(self):
        self.data = []
        self.mutex = threading.Lock()
        self.should_stop = False
        self.file = io.open("log.csv", "a")
        self.serial = serial.Serial(com_port, baud_rate, timeout=1)
        threading.Thread.__init__(self)

    def read_data(self):
        self.mutex.acquire()
        new_data = self.data
        self.mutex.release()
        return new_data

    def stop(self):
        self.mutex.acquire()
        self.should_stop = True
        self.mutex.release()

    def run(self):
        while True:
            self.mutex.acquire()
            if self.should_stop:
                return
            data = self.serial.readline()
            data = data.decode()
            data.strip()
            array = data.split(',')
            if len(array) == 9 and array[0] != "0":
                self.file.write(data)
            self.data = array
            self.mutex.release()