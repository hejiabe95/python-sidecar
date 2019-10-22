import time
import datetime
import threading

class RWlock(object):
    def __init__(self):
        self._lock = threading.Lock()
        self._extra = threading.Lock()
        self.read_num = 0

    def read_acquire(self):
        with self._extra:
            self.read_num += 1
            if self.read_num == 1:
                self._lock.acquire()

    def read_release(self):
        with self._extra:
            self.read_num -= 1
            if self.read_num == 0:
                self._lock.release()

    def write_acquire(self):
        self._lock.acquire()

    def write_release(self):
        self._lock.release()

rwlock = RWlock()

def algorithm_start(id):
    rwlock.write_acquire()
    print('start:',id, '-->', datetime.datetime.now())
    time.sleep(2)
    print('finish:',id, '-->', datetime.datetime.now())
    rwlock.write_release()
    return 'excute the algorithm.py'