from threading import Timer, Event, Thread
from time import sleep


def first(f, s):
    sleep(10)
    print(f'First is ready ...')
    f.set()
    s.wait()
    print(f'First is working ...')
    f.clear()


def second(f, s):
    print(f'Second is ready ...')
    s.set()
    f.wait()
    print(f'Second is working ...')
    f.clear()


f = Event()
s = Event()

t1 = Thread(target=first, args=(s, f,))
t2 = Thread(target=second, args=(s, f,))

t1.start()
t2.start()
