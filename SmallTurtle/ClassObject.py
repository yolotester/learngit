# encoding=gbk
import random as r

# ��Ͷ���     �����Դ�д��ĸ��ͷ/  ����=����+����
# class turtle:
#     weight = 10
#     color = 'green'
#     shell = True
#     growth = 3.1415
#
#     def climp(self):
#         print('����������������')
#     def run(self):
#         print('�������ܡ�������')
#
# # ���ʵ��������ֵ������yolo
# yolo = turtle()
# yolo.climp()
# yolo.run()

# ����������������װ   ��֪��sort�����������ڲ����ƣ�ֻ֪���������ʹ���Ĳ����������ʹ�ø÷���
list1=[1, 5, 8, 2, 3]
list1 = list1.sort()
print(list1)

# ���������������̳�   ӵ�и���ĸ��ַ���
class Mylist(list):
    pass
yolo = Mylist()
yolo.append(1)
yolo.append(21)
yolo.append(5)
yolo.sort()
print(yolo)

# ����������������̬  ��������ͬ��ʵ�ֽ����ͬ
class A():
    def fun(self):
        print('yolo')
class B():
    def fun(self):
        print('doudou')
a = A()
b = B()
a.fun()
b.fun()

# self��ʲô�� �����ʵ�����������ͨ��self��������ȷ���ĸ�����,ʵ��������A = Ball() �ȼ��� A = Ball(A) �ȼ��� A=Ball(self)
class Ball():
    def setName(self,name):
        self.name = name
    def kick(self):
        print('����%s��˭������Ŷ' % self.name)
A = Ball()
A.setName('AAA')
B = Ball()
B.setName("BBB")
A.kick()
B.kick()

# ħ������   __init__(self,parm1,parm2...)  ���췽��   ʵ����һ������ʱ���÷����Զ�������
# ʵ����һ������ʱ�����Դ���������ò������Զ��ش��뵽__init__�����У����ǿ���ͨ����д������������Զ������ĳ�ʼ��ֵ
class Ball():
    def __init__(self,name):
        self.name = name
    def kick(self):
        print('����%s��˭������Ŷ' % self.name)

#A = Ball()    TypeError: __init__() missing 1 required positional argument: 'name'
A = Ball('AAA')
A.kick()
B = Ball('BBB')
B.kick()

# ���к�˽��  __name  ˽�б���
# class Person:
#     name = 'yolo'
# A = Person()
# print(A.name)   # ���б����������� . ��������

class Person:
    __name = 'doudou'
    def getName(self):
        return self.__name

C = Person()
print(C.getName())
print(C._Person__name)

# �̳�
# 1������̳и������еķ���������
class Parent:
    def hello(self):
        print('���ڵ��ø���ķ���')
class Child(Parent):
    pass

A = Parent()
A.hello()
B = Child()
B.hello()

#  2�������ж����븸����ͬ�ķ��������ԣ�����Զ����Ǹ����Ӧ�ķ��������ԣ��Ը���û��Ӱ��
class Parent:
    def hello(self):
        print('���ڵ��ø���ķ���')
class Child(Parent):
    def hello(self):
        print('���ǵ�����ķ���')
A = Parent()
A.hello()
B = Child()
B.hello()

# 3����������и����˸���ķ����������ʵ����������ø��෽��������1������δ�󶨵ĸ��෽�� ��2��ʹ��super����
class Fish():
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
    def move(self):
        self.x -= 1
        print('�ҵ�λ���ǣ�',self.x,self.y)

class Salmon(Fish):
    pass
class Crap(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        # Fish.__init__(self)   #��1������δ�󶨵ĸ��෽��,���self�������ʵ������
        super().__init__()      # ��2��ʹ��super����
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('����Զ�����������')
            self.hungry = False
        else:
            print('��̫���ˡ�����')
salmon = Salmon()
salmon.move()
fish = Fish()
fish.move()
shark = Shark()
shark.eat()
#   shark.move()     AttributeError: 'Shark' object has no attribute 'x'   �����˸��෽�������ø��෽���ᱨ��
shark.move()

# ���ؼ̳�
class Base1:
    def foo1(self):
        print('foo1')
class Base2:
    def foo2(self):
        print('foo2')
class C(Base1,Base2):
    pass
c = C()
c.foo1()
c.foo2()

# ���   �����ʵ���������������棬�Ѿ������Ͻ�����   ����һ��ˮ��,ˮ�������ڹ������,ˮ�����ڹ�����,����ͬһ����
# ʹ�ü̳в�̫����,��ʱ��ʹ�����
class Turtle():
    def __init__(self,x):
        self.num = x

class Fish():
    def __init__(self,y):
        self.num = y

class Pool():
    def __init__(self,x,y):
        self.turtle = Turtle(x)  #�����ʵ���������������棬�Ѿ������Ͻ�����
        self.fish = Fish(y)
    def print_num(self):
        print('ˮ�����ڹ� %d ֻ��С��%d ����' % (self.turtle.num,self.fish.num))
pool = Pool(2,50)
pool.print_num()

# �ඨ��  �����   ʵ��������
class C:
    count = 0
a = C()   #��C��ʵ����һ������
b = C()
print(a.count)
print(b.count)
a.count += 10
print(a.count)
print(b.count)
C.count  += 100  # CΪ�����
print(a.count)
print(b.count)


# 1����Ҫ��ͼ�������涨����������뵽�����Ժͷ�����Ӧ�����ü̳к���ϻ�����������չ
# 2���ò��õĴ��������������������ʣ��������ö���
class C:
    def x(self):
        print('X-man!!')
c = C()
c.x()
c.x = 200
# c.x()   TypeError: 'int' object is not callable   ���Ե������뷽������ͬ��Ḳ�Ƿ���

# ʲô�ǰ󶨣�
# Python�ϸ�Ҫ�󷽷���Ҫ��ʵ�����ܱ����ã�����������ʵ����Python��ν�İ󶨸���
class CC:
    def setXY(self,x,y):
        self.x = x
        self.y = y
    def print_XY(self):
        print(self.x,self.y)
bb = CC()
bb.setXY(4,5)  #�ȼ���bb.setXY(bb,4,5) ����һ��self= bb�������python�а󶨸���
bb.print_XY()

