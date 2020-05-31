# 单线程死循环
while True:
    pass  # pass是占位符，即是空语句


# 2个线程死循环

import threading
# 子线程死循环
def thread1():
    while True:
        pass

th1 = threading.Thread(target=thread1)
th1.start()

# 主线程死循环
while True:
    pass


# 2个进程死循环
import multiprocessing

# 子进程死循环
def thread1():
    while True:
        pass

p1 = multiprocessing.Process(target=thread1)
p1.start()

# 主进程死循环
while True:
    pass


