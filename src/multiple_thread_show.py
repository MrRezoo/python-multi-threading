"""
    Thread Pool Executor

"""

from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor
from threading import Thread


def show(name):
    print(f'Starting {name} ...')
    sleep(3)
    print(f'Finishing {name} ...')


# with ThreadPoolExecutor() as executor:
#     names = ['One', 'Two', 'Three', 'Four', 'Five']
#     executor.map(show, names)


with ThreadPoolExecutor(max_workers=2) as executor:
    names = ['One', 'Two', 'Three', 'Four', 'Five']
    executor.map(show, names)

print("Done . . .")
