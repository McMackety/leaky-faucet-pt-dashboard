import threading
import io
import time

class RocketReplay(threading.Thread):
    def __init__(self):
        self.data = []
        self.mutex = threading.Lock()
        self.should_stop = False
        self.previous_time = 0
        self.file = io.open("HotFire11.9.21.csv", "r")
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
            try:
                if self.should_stop:
                    return
                data = self.file.readline()
                data.strip()
                array = data.split(',')
                self.data = array
                print((abs(float(array[0]) - self.previous_time) / 10000.0))
                time.sleep(abs(float(array[0]) - self.previous_time) / 10000.0)
                self.previous_time = float(array[0])
            except Exception:
                self.data = []
            self.mutex.release()