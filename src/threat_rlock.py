"""
    Race condition
    Thread safe
    Dead lock
    atomic
"""
from threading import Thread, RLock

num = 0  # shared resource
lock = RLock()


def add():
    global num
    with lock:
        subtract()
        for _ in range(100000):
            num += 1


def subtract():
    global num
    with lock:
        for _ in range(100000):
            num -= 1


def both():
    subtract()
    add()


t1 = Thread(target=add)
t2 = Thread(target=subtract)

t1.start()
t2.start()

t1.join()
t2.join()

print(num)
print('Done . . . ')
