"""
    Race condition
    Thread safe
    Dead lock
    atomic
"""
from threading import Thread, Lock

num = 0  # shared resource
lock = Lock()


def add():
    """
        atomic
    """

    global num
    with lock:
        for _ in range(100000):
            num += 1


def subtract():
    """
        atomic
    :return:
    """
    global num
    with lock:
        for _ in range(100000):
            num -= 1


# def add():
#     """
#          Thread safe
#     :return:
#     """
#     lock.acquire()
#     global num
#     for _ in range(100000):
#         num += 1
#     lock.release()

# def subtract():
#     """
#         Dead lock
#     :return:
#     """
#     global num
#     lock.acquire()
#     for _ in range(100000):
#         num -= 1
#     lock.acquire()


t1 = Thread(target=add)
t2 = Thread(target=subtract)

t1.start()
t2.start()

t1.join()
t2.join()

print(num)
print('Done . . . ')
