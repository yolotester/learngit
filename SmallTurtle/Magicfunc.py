# encoding=gbk
# 1、魔法方法被双下划线包围，__init__（）
# 2、魔法方法能够在适当的时候被调用
# 为什么有时候要重写--init--（）方法，有时候不需要？因为有些类需要先给定义一些必要的参数
# 例如：定义一个矩形类，必要的参数就是长和宽
class Rectangle:
    def __init__(self,length,height):
        self._length = length
        self._height = height
    def getPeri(self):
        return (self._height + self._length) *2
    def getArea(self):
        return self._height *self._length
rect = Rectangle(5,6)
print(rect.getArea())
print(rect.getPeri())

# --new--()方法
class Capstring(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls,string)
a = Capstring('i LOVE doudou')
print(a)

# --del--()方法,当没有 任何变量 引用这个 对象 的时候，垃圾回收机制就会自动把这个对象销毁，销毁对象的时候就会调用--del--方法
class C:
    def __init__(self):
        print('--init--方法被调用了。。。')
    def __del__(self):
        print('--del--方法被调用了。。。')

c = C()


# 魔法方法一：算术运算。工厂函数  int，list是类对象
print(type(int))
print(type(C))
a = int('123')   # 新理解，a为int类对象的实例化对象，传入参数123
# 重写加法，减法
class New_int(int):
    def __add__(self, other):
        return int.__sub__(self,other)
    def __sub__(self, other):
        return int.__add__(self,other)
a = New_int(2)
b = New_int(2)
print(a + b)
print(a - b)

'''
# 改写add，sub方法，会遇到无限递归的情况
class Try_int(int):
    def __add__(self, other):
        return self+ other
    def __sub__(self, other):
        return self - other
a = Try_int(2)
b = Try_int(2)
print(a + b)
print(a - b)     # RecursionError: maximum recursion depth exceeded,达到递归最大值
'''

# mul乘法
class YL_int(int):
    def __mul__(self, other):
        return int.__mul__(self,other)
a = YL_int(2)
b = YL_int(2)
print(a * b)

# truediv  / 除法
# floordiv   //  整除
# mod   %  取余
# divmod  定义当被divmod（）调用时的行为，divmod（a，b） 结果为a//b之后的余数
# pow 当被pow（）调用或**运算时的行为
# lshift  左移 <<
# rshift  右移 >>
# and     按位与
# xor     按位异或
# or      按位或|

# 反运算   当第一个运算符无法执行相应操作时，用第二个运算符的相应操作  在算术运算符方法名前加r字母
class Nint(int):
    def __rsub__(self, other):
        return int.__rsub__(self,other)
a = Nint(3)
b= Nint(5)
print(a - b)
print(1 - b)

# 增量赋值运算符，在算术运算符方法名前加i字母
class Iint(int):
    def __iadd__(self, other):
        return int.__iadd__(self,other)
a = Iint(3)
b = Iint(5)
print(a+b)

# 一元操作符
# neg   +x
# pos   -x
# abs   定义当被abs（）调用时的行为  取绝对值
# invert  定义按位求反的行为

# 定制一个类
# --str--  魔法方法，当被打印的时候，需要字符串输出的时候
# --repr--  魔法方法，直接输入对象名，就可以打印出返回值
# 所有属于实例化对象的变量定义在--init--方法里，就不会出问题
import time as t
class Mytimer(object):

    def __init__(self):
        self.unit = ['年','月','日','时','分','秒']
        self.prompt = '未开始计时'
        self.time = []
        self.end = 0     # 属性名与方法名相同，会覆盖掉方法
        self.begin = 0    # 属性名与方法名相同，会覆盖掉方法   报这个错：TypeError: 'int' object is not callable
                          # 翻译为：整形不能被调用

    def __str__(self):
        return self.prompt
    __repr__ = __str__

    # 两个对象相加显示总共运行了多少秒，重写--add--方法
    def __add__(self, other):
        prompt = '总共运行了'
        result = []
        for index in range(6):
            result.append(self.time[index] + other.time[index])
            if result[index]:
                prompt += str(result[index] + self.unit[index])
        return  prompt

    # 开始计时
    def start(self):    ## 属性名与方法名相同，会覆盖掉方法
        self.begin = t.localtime()
        self.prompt = ' 请先调用stop（） 方法停止计时'
        print('计时开始')

    #停止计时
    def stop(self):  # 属性名与方法名相同，会覆盖掉方法
        if not self.begin:
            print('请先调用start（）方法进行计时')
        else:
            self.end = t.localtime()
            self._calc()
            print('计时结束')

    #内部方法，计算运行时间
    def _calc(self):
        self.time = []
        self.prompt = '一共运行了'
        for index in range(6):
            self.time.append(self.end[index]-self.begin[index])
            if self.time[index]:
                self.prompt += (str(self.time[index]) + self.unit[index])
        print(self.prompt)

        # 为下一轮计时做准备
        self.begin = 0
        self.end = 0

t1 = Mytimer()
t1.start()
t.sleep(3)
t1.stop()

# 属性访问









