from threading import Timer


def show():
    print(f'Hello World ...')


t = Timer(10, show)
t.start()
