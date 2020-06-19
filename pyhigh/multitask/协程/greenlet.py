# greenlet 实现多任务
# greenlet 对带yield的生成器进行了封装

from greenlet import greenlet
import time


def task_1():
    while True:
        print('=====11--------')
        gr2.switch()
        time.sleep(0.1)



def task_2():
    while True:
        print('=====22--------')
        gr1.switch()
        time.sleep(0.1)




gr1 = greenlet.greenlet(task_1)  #
gr2 = greenlet.greenlet(task_2)



