# 多线程共享全局变量,修改全局变量两个方法：1、global声明   2、 可修改序列的内置方法
# 多线程中可以使用args指定实参传入target指向的函数中
# 共享数据的好处：因为多任务往往配合使用

'''
import threading
import time


num  = 100

def test1():
    global num
    num += 1
    print('-----in test1 g_num=%d ' % num)


def test2():
    print('-----in test2 g_num=%d ' % num)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print('-----in main Thread g_num = %d' % num)


if __name__ == '__main__':
    main()

'''

# 多线程中可以使用args指定实参传入target指向的函数中


import threading
import time

g_nums = [11,22]


def test1(temp):
    temp.append(33)
    print('------in test1 temp = %s ' % str(temp))

def test2(temp):
    print('------in test2 temp = %s ' % str(temp))

def main():
    t1 = threading.Thread(target=test1,args=(g_nums,))  # args变量保存的是一个元组
    t2 = threading.Thread(target=test2,args=(g_nums,))
    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print('------in main g_nums = %s ' % str(g_nums))



if __name__ == '__main__':
    main()


