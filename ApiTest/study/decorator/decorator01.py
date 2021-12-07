'''
    目标：在闭包知识的前提下，学习装饰器的实现原理
'''
'''
    example
'''
def set_func(func):
    '''
    :param func: 接收参数，可接收数字，列表，函数的引用等
    :return: 内部函数call_func的引用
    '''
    def call_func():
        print('------验证1------')
        print('------验证2------')
        func()
    return  call_func

'''
装饰器的自动实现方式
@set_func 
'''

@set_func  # 具有特殊功能的语句，叫做语法行  等价于：test1 = set_func(test1)
def test1():
    print('-----test1-----')

'''
装饰器的手动实现方式
test1 = set_func(test1)
test1()
'''


