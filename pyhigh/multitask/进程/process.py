# qq.exe程序就是一个二进制文件，运行中的qq才是进程，进程才能调度资源
# 程序：xxx.py这是程序，静态的
# 进程：程序运行起来后，代码+用到的资源为进程
# 多进程实现多任务与多线程实现多任务没有什么太多区别：进程占用资源多，线程占用资源少
# 多任务就是多个函数或者py文件同时执行
import multiprocessing
import time

def test1():
    while True:
        print('1-------------')
        time.sleep(1)


def test2():
    while True:
        print('2-------------')
        time.sleep(1)


def main():
    p1 = multiprocessing.Process(target=test1)  # 创建Process对象
    p2 = multiprocessing.Process(target=test2)
    p1.start()  # 创建子进程
    p2.start()

if __name__ == '__main__':
    main()


# 进程与线程对比
# 进程：电脑上多开的qq，资源分配的单位
# 线程：qq中的多个聊天窗口，操作系统调度的单位