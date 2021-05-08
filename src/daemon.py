from time import sleep, perf_counter
from threading import Thread
import sys

start = perf_counter()


def show(name):
    print(f'Starting {name} ...')
    sleep(3)
    print(f'Finishing {name} ...')


t1 = Thread(target=show, args=('One',))
t2 = Thread(target=show, args=('Two',))

t1.setDaemon(True)

t1.start()
t2.start()


print(t1.isDaemon())

end = perf_counter()
print(round(end - start))
sys.exit()