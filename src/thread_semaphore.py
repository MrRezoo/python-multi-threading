"""
    Race condition
    Thread safe
    Dead lock
    atomic
"""
from threading import Thread, Semaphore, current_thread, BoundedSemaphore
from time import sleep

num = 0  # shared resource
lock_normal = Semaphore(value=2)


# lock_bounded = BoundedSemaphore(value=2)

def add():
    global num
    with lock_normal:
        print(current_thread().getName())
        sleep(2)
        num += 1


# def add():
#     global num
#     lock_normal.acquire()
#     print(current_thread().getName())
#     sleep(2)
#     num += 1
#     lock_normal.release()


#
# def add():
#     global num
#     lock_bounded.acquire()
#     print(current_thread().getName())
#     sleep(2)
#     num += 1
#     lock_bounded.release()

t1 = Thread(target=add)
t2 = Thread(target=add)
t3 = Thread(target=add)
t4 = Thread(target=add)
t5 = Thread(target=add)
t6 = Thread(target=add)
t7 = Thread(target=add)
t8 = Thread(target=add)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()

print('Done . . . ')
