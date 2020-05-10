# encoding=gbk
# 1��ħ��������˫�»��߰�Χ��__init__����
# 2��ħ�������ܹ����ʵ���ʱ�򱻵���
# Ϊʲô��ʱ��Ҫ��д--init--������������ʱ����Ҫ����Ϊ��Щ����Ҫ�ȸ�����һЩ��Ҫ�Ĳ���
# ���磺����һ�������࣬��Ҫ�Ĳ������ǳ��Ϳ�
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

# --new--()����
class Capstring(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls,string)
a = Capstring('i LOVE doudou')
print(a)

# --del--()����,��û�� �κα��� ������� ���� ��ʱ���������ջ��ƾͻ��Զ�������������٣����ٶ����ʱ��ͻ����--del--����
class C:
    def __init__(self):
        print('--init--�����������ˡ�����')
    def __del__(self):
        print('--del--�����������ˡ�����')

c = C()


# ħ������һ���������㡣��������  int��list�������
print(type(int))
print(type(C))
a = int('123')   # ����⣬aΪint������ʵ�������󣬴������123
# ��д�ӷ�������
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
# ��дadd��sub���������������޵ݹ�����
class Try_int(int):
    def __add__(self, other):
        return self+ other
    def __sub__(self, other):
        return self - other
a = Try_int(2)
b = Try_int(2)
print(a + b)
print(a - b)     # RecursionError: maximum recursion depth exceeded,�ﵽ�ݹ����ֵ
'''

# mul�˷�
class YL_int(int):
    def __mul__(self, other):
        return int.__mul__(self,other)
a = YL_int(2)
b = YL_int(2)
print(a * b)

# truediv  / ����
# floordiv   //  ����
# mod   %  ȡ��
# divmod  ���嵱��divmod��������ʱ����Ϊ��divmod��a��b�� ���Ϊa//b֮�������
# pow ����pow�������û�**����ʱ����Ϊ
# lshift  ���� <<
# rshift  ���� >>
# and     ��λ��
# xor     ��λ���
# or      ��λ��|

# ������   ����һ��������޷�ִ����Ӧ����ʱ���õڶ������������Ӧ����  �����������������ǰ��r��ĸ
class Nint(int):
    def __rsub__(self, other):
        return int.__rsub__(self,other)
a = Nint(3)
b= Nint(5)
print(a - b)
print(1 - b)

# ������ֵ������������������������ǰ��i��ĸ
class Iint(int):
    def __iadd__(self, other):
        return int.__iadd__(self,other)
a = Iint(3)
b = Iint(5)
print(a+b)

# һԪ������
# neg   +x
# pos   -x
# abs   ���嵱��abs��������ʱ����Ϊ  ȡ����ֵ
# invert  ���尴λ�󷴵���Ϊ

# ����һ����
# --str--  ħ��������������ӡ��ʱ����Ҫ�ַ��������ʱ��
# --repr--  ħ��������ֱ��������������Ϳ��Դ�ӡ������ֵ
# ��������ʵ��������ı���������--init--������Ͳ��������
import time as t
class Mytimer(object):

    def __init__(self):
        self.unit = ['��','��','��','ʱ','��','��']
        self.prompt = 'δ��ʼ��ʱ'
        self.time = []
        self.end = 0     # �������뷽������ͬ���Ḳ�ǵ�����
        self.begin = 0    # �������뷽������ͬ���Ḳ�ǵ�����   �������TypeError: 'int' object is not callable
                          # ����Ϊ�����β��ܱ�����

    def __str__(self):
        return self.prompt
    __repr__ = __str__

    # �������������ʾ�ܹ������˶����룬��д--add--����
    def __add__(self, other):
        prompt = '�ܹ�������'
        result = []
        for index in range(6):
            result.append(self.time[index] + other.time[index])
            if result[index]:
                prompt += str(result[index] + self.unit[index])
        return  prompt

    # ��ʼ��ʱ
    def start(self):    ## �������뷽������ͬ���Ḳ�ǵ�����
        self.begin = t.localtime()
        self.prompt = ' ���ȵ���stop���� ����ֹͣ��ʱ'
        print('��ʱ��ʼ')

    #ֹͣ��ʱ
    def stop(self):  # �������뷽������ͬ���Ḳ�ǵ�����
        if not self.begin:
            print('���ȵ���start�����������м�ʱ')
        else:
            self.end = t.localtime()
            self._calc()
            print('��ʱ����')

    #�ڲ���������������ʱ��
    def _calc(self):
        self.time = []
        self.prompt = 'һ��������'
        for index in range(6):
            self.time.append(self.end[index]-self.begin[index])
            if self.time[index]:
                self.prompt += (str(self.time[index]) + self.unit[index])
        print(self.prompt)

        # Ϊ��һ�ּ�ʱ��׼��
        self.begin = 0
        self.end = 0

t1 = Mytimer()
t1.start()
t.sleep(3)
t1.stop()

# ���Է���









