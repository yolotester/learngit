# 协程实现多任务
# 实现多任务占用资源最多的是进程，然后是线程，最后是协程
import time


def task_1():
    while True:
        print('=====11--------')
        time.sleep(0.1)
        yield


def task_2():  # 有yield语句，则此函数是生成器
    while True:
        print('=====22--------')
        time.sleep(0.1)
        yield


def main():
    t1 = task_1()  # 则函数的调用就是创建生成器对象
    t2 = task_2()
    while True:
        next(t1)
        next(t2)


if __name__ == '__main__':
    main()