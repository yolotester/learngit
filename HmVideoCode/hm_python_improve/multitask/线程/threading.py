# 多用户多任务
# 使用多任务-线程：对于程序：一个py文件可以同时执行多个方法
# 查看线程数量：threading.enumerate(),线程的运行没有先后顺序，可以通过适当延迟time.sleep
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中,返回的是一个元组
import time

import threading


def sing():
    ''' 唱歌 5秒钟'''
    for val in range(5):
        print('-----singing....-----')
        time.sleep(1)
    # target指向的函数运行结束，则这个子线程结束。。。


def dance():
    ''' 跳舞 5秒钟'''
    for val in range(10):
        print('-----dancing....-----')
        time.sleep(1)

def main():

    print('-----start=====:%s' %time.ctime())
    t1 = threading.Thread(target=sing)  # 只是创建了Thread类的一个普通实例对象,target不要指向类名，可以通过类来封装各种方法
    t2 = threading.Thread(target=dance)  # 只是创建了Thread类的一个普通实例对象
    t1.start()  # 调用这个方法，才创建线程并执行函数代码，函数代码执行完，线程结束
    t2.start()

    # 循环查看线程数量
    while True:
        print(threading.enumerate())  # 返回一个线程列表
        if len(threading.enumerate()) <= 1:  # 只剩下主线程的时候，跳出循环。主线程结束，说明这个程序结束
            break
        time.sleep(1)



if __name__ == '__main__':
    main()