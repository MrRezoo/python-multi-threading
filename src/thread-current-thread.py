from time import sleep, perf_counter
from threading import Thread, current_thread

start = perf_counter()


def show(name):
    print(f'Starting {name} ...')
    print(current_thread())
    print(current_thread().getName())
    sleep(3)
    print(f'Finishing {name} ...')


t1 = Thread(target=show, args=('One',), name='First')
t2 = Thread(target=show, args=('Two',), name='Second')

t1.start()
t2.start()

t1.join()
t2.join()

end = perf_counter()
print(round(end - start))
