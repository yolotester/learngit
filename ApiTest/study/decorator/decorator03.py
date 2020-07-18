'''
    目标：对装饰器的再研究
                1、对无参数、无返回值的函数进行装饰，上例中test1函数就是例子
                2、对有参数、无返回值的函数进行装饰
'''

# 对有参数、无返回值的函数进行装饰
def set_func(func):
    def call_func(a):
        print('------验证1------')
        print('------验证2------')
        func(a)
    return  call_func

@set_func
def test1(num):
    print('-----test1-----%d' % num)

# 调用test1函数
test1(100)


# 对不定长参数进行装饰
def set_func(func):
    def call_func(*args, **kwargs):
        print('------验证1------')
        print('------验证2------')
        func(*args, **kwargs)
    return  call_func

@set_func
def test1(num, *args, **kwargs):
    print('-----test1-----%d' % num)
    print('-----test1-----', args)  # args里面存的是元祖
    print('-----test1-----', kwargs)  # kwargs里面存的是字典

# 调用test1函数
test1(100)
test1(100, 200)
test1(100, 200, 300, mm = 100)


# 对有返回值的函数进行装饰
def add_func(func):
    def inner_func(*args, **kwargs):
        print('----add----')
        return func()
    return inner_func

@add_func
def test1():
    print('----test1----')
    return 'ok' , 200

ret = test1()
print(ret)


# 多个装饰器装饰同一个函数
def add_func1(func):
    print('----开始装饰addfunc1----')
    def inner_func(*args, **kwargs):
        print('----add01----')
        func()
    return inner_func

def add_func2(func):
    print('----开始装饰addfunc2----')
    def inner_func(*args, **kwargs):
        print('----add02----')
        func()
    return inner_func

@add_func1
@add_func2
def test1():
    print('----test1----')

test1()

print('*' * 50)

# 用类装饰函数
class Test(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('----权限认证1----')
        return  self.func()

@Test  # 等价于test1 = Test（test1）
def test1():
    print('----test1----')

test1()  # 实例对象加小括号，代表调用魔法方法__call__