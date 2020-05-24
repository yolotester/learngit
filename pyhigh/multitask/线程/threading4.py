# 多线程中共享数据带来的资源竞争的问题
# 当多个线程几乎同时修改某一个共享数据的时候，就可能带来资源竞争的问题

'''
import threading
import time


num  = 0

def test1(temp):
    global num
    for i in range(temp):
        num += 1
    print('-----in test1 temp=%d ' % temp)


def test2(temp):
    global num
    for i in range(temp):
        num += 1
    print('-----in test1 temp=%d ' % temp)


def main():
    t1 = threading.Thread(target=test1,args=(1000000,))  # args变量保存的值越大，数据错误的可能性更大
    t2 = threading.Thread(target=test2,args=(1000000,))
    t1.start()
    t2.start()

    time.sleep(2)

    print('-----in main Thread num = %d' % num)


if __name__ == '__main__':
    main()

'''

# 解决资源竞争问题的方法：同步的概念：进程或者线程A和B一块配合，协同操作
# 互斥锁：当多个线程几乎同时修改某一个共享数据的时候，需要进行同步控制，互斥锁为资源引入一个状态：锁定/未锁定

import threading
import time

num  = 0

def test1(temp):
    global num
    # 上锁，如果之前没有被上锁，那么此时 上锁成功
    # 如果已经被上锁，那么此时会被堵塞在这里，知道被解锁

    mutex.acquire()
    for i in range(temp):
        num += 1
    # 解锁
    mutex.release()
    print('-----in test1 temp=%d ' % temp)


def test2(temp):
    global num
    mutex.acquire()
    for i in range(temp):
        num += 1
    mutex.release()
    print('-----in test1 temp=%d ' % temp)


# 创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()

def main():
    t1 = threading.Thread(target=test1,args=(1000000,))  # args变量保存的值越大，数据错误的可能性更大
    t2 = threading.Thread(target=test2,args=(1000000,))
    t1.start()

    t2.start()
    time.sleep(2)

    print('-----in main Thread num = %d' % num)


if __name__ == '__main__':
    main()