import threading
from algorithm import algorithm_start

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

def execute_algorithm_security(func,*args):
    rwlock.write_acquire()
    func(args)
    rwlock.write_release()

def run(id):
    execute_algorithm_security(algorithm_start,id)
