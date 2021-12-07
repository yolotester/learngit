import gevent
import time
# from gevent import monkey
#
# monkey.patch_all()  # 遇到程序中有延时/堵塞代码，自动更换成gevent中的模块

def task1(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
       # time.sleep(0.5)  # 遇到延时/堵塞时，gevent自动切换任务
        gevent.sleep(0.5)

def task2(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        # time.sleep(0.5)  # 遇到延时/堵塞时，gevent自动切换任务
        gevent.sleep(0.5)

def task3(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        # time.sleep(0.5)  # 遇到延时/堵塞时，gevent自动切换任务
        gevent.sleep(0.5)

g1 = gevent.spawn(task1,5)  # 创建gevent对象，指定task1函数执行，为task1函数传参
g2 = gevent.spawn(task2,5)
g3 = gevent.spawn(task3,5)


g1.join()  # 开始执行task1函数中的代码
g2.join()
g3.join()

# gevent.joinall([                 这种方式更简洁
#     gevent.spawn(task1, 5),
#     gevent.spawn(task2, 5),
#     gevent.spawn(task3, 5)
# ])