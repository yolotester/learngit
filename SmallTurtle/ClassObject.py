# encoding=gbk
import random as r

# 类和对象     类名以大写字母开头/  对象=属性+方法
# class turtle:
#     weight = 10
#     color = 'green'
#     shell = True
#     growth = 3.1415
#
#     def climp(self):
#         print('你正在爬。。。。')
#     def run(self):
#         print('你正在跑。。。。')
#
# # 类的实例化对象赋值给变量yolo
# yolo = turtle()
# yolo.climp()
# yolo.run()

# 面向对象的特征：封装   不知道sort（）方法的内部机制，只知道方法名和传入的参数，便可以使用该方法
list1=[1, 5, 8, 2, 3]
list1 = list1.sort()
print(list1)

# 面向对象的特征：继承   拥有父类的各种方法
class Mylist(list):
    pass
yolo = Mylist()
yolo.append(1)
yolo.append(21)
yolo.append(5)
yolo.sort()
print(yolo)

# 面向对象的特征：多态  方法名相同，实现结果不同
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

# self是什么？ 类可以实例化多个对象，通过self，可以明确是哪个对象,实例化对象A = Ball() 等价于 A = Ball(A) 等价于 A=Ball(self)
class Ball():
    def setName(self,name):
        self.name = name
    def kick(self):
        print('我是%s，谁在踢我哦' % self.name)
A = Ball()
A.setName('AAA')
B = Ball()
B.setName("BBB")
A.kick()
B.kick()

# 魔法方法   __init__(self,parm1,parm2...)  构造方法   实例化一个对象时，该方法自动被调用
# 实例化一个对象时，可以传入参数，该参数会自动地传入到__init__方法中，我们可以通过重写这个方法，来自定义对象的初始化值
class Ball():
    def __init__(self,name):
        self.name = name
    def kick(self):
        print('我是%s，谁在踢我哦' % self.name)

#A = Ball()    TypeError: __init__() missing 1 required positional argument: 'name'
A = Ball('AAA')
A.kick()
B = Ball('BBB')
B.kick()

# 共有和私有  __name  私有变量
# class Person:
#     name = 'yolo'
# A = Person()
# print(A.name)   # 公有变量，可以用 . 调用属性

class Person:
    __name = 'doudou'
    def getName(self):
        return self.__name

C = Person()
print(C.getName())
print(C._Person__name)

# 继承
# 1、子类继承父类所有的方法和属性
class Parent:
    def hello(self):
        print('正在调用父类的方法')
class Child(Parent):
    pass

A = Parent()
A.hello()
B = Child()
B.hello()

#  2、子类中定义与父类相同的方法或属性，则会自动覆盖父类对应的方法或属性，对父类没有影响
class Parent:
    def hello(self):
        print('正在调用父类的方法')
class Child(Parent):
    def hello(self):
        print('覆盖掉父类的方法')
A = Parent()
A.hello()
B = Child()
B.hello()

# 3、解决子类中覆盖了父类的方法，子类的实例化对象调用父类方法报错。（1）调用未绑定的父类方法 （2）使用super方法
class Fish():
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
    def move(self):
        self.x -= 1
        print('我的位置是：',self.x,self.y)

class Salmon(Fish):
    pass
class Crap(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        # Fish.__init__(self)   #（1）调用未绑定的父类方法,这个self是子类的实例对象
        super().__init__()      # （2）使用super方法
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('我想吃东西啊。。。')
            self.hungry = False
        else:
            print('我太撑了。。。')
salmon = Salmon()
salmon.move()
fish = Fish()
fish.move()
shark = Shark()
shark.eat()
#   shark.move()     AttributeError: 'Shark' object has no attribute 'x'   覆盖了父类方法，调用父类方法会报错
shark.move()

# 多重继承
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

# 组合   把类的实例化放在新类里面，把旧类给组合进新类   定义一个水池,水池里有乌龟和鱼类,水池与乌龟鱼类,不是同一物种
# 使用继承不太合适,这时就使用组合
class Turtle():
    def __init__(self,x):
        self.num = x

class Fish():
    def __init__(self,y):
        self.num = y

class Pool():
    def __init__(self,x,y):
        self.turtle = Turtle(x)  #把类的实例化放在新类里面，把旧类给组合进新类
        self.fish = Fish(y)
    def print_num(self):
        print('水池中乌龟 %d 只，小鱼%d 条！' % (self.turtle.num,self.fish.num))
pool = Pool(2,50)
pool.print_num()

# 类定义  类对象   实例化对象
class C:
    count = 0
a = C()   #类C的实例化一个对象
b = C()
print(a.count)
print(b.count)
a.count += 10
print(a.count)
print(b.count)
C.count  += 100  # C为类对象
print(a.count)
print(b.count)


# 1、不要试图在类里面定义出所有能想到的属性和方法，应该利用继承和组合机制来进行扩展
# 2、用不用的词性命名，属性名用名词，方法名用动词
class C:
    def x(self):
        print('X-man!!')
c = C()
c.x()
c.x = 200
# c.x()   TypeError: 'int' object is not callable   属性的名字与方法名相同则会覆盖方法

# 什么是绑定？
# Python严格要求方法需要有实例才能被调用，这种限制其实就是Python所谓的绑定概念
class CC:
    def setXY(self,x,y):
        self.x = x
        self.y = y
    def print_XY(self):
        print(self.x,self.y)
bb = CC()
bb.setXY(4,5)  #等价于bb.setXY(bb,4,5) 即有一个self= bb，这就是python中绑定概念
bb.print_XY()

