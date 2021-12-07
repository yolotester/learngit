'''
    目标：利用装饰器，来统计某个函数的运行时间
'''
import time

def set_func(func):

    def call_func():
        '''
        :return: 返回test1函数的运行时间
        '''
        start_time = time.time()
        print('-----1111------')
        func()
        end_time = time.time()
        print('test1函数的运行时间为 %f '% (end_time - start_time))
    return  call_func

@set_func
def test1():
    for i in range(0, 10000):
        print('-----test1-----')

# 调用test1函数
test1()
