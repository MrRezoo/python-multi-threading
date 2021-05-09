from threading import Timer


def show(f, s):
    print(f'Hello World ...')


t = Timer(10, show)
t.start()
