# 描述符;就是将某种特殊类型的类的实例指派给另一个类的属性
# 实现如下三种方法中其中一种的类:特殊类型的类
# __get__ (self,instance,owner)  用于访问属性,它返回属性的值
# __set__(self,instance,value) 将在属性分配(即赋值)时调用,不返回任何内容
# __delete__(self,instance)   控制删除 操作,不返回任何内容

class Descrit():
    '''
    符合描述符类定义
    '''''
    def __get__(self, instance, owner):
        print('getting...',self,instance,owner)   # self 自身类,instance Test实例对象,owner Test类

    def __set__(self, instance, value):
        print('setting...',self,instance,value)

    def __delete__(self, instance):
        print('deleting...',self,instance)

class Test():
    x = Descrit()

test = Test()
print(test.x)
test.x = 20

# Property 类的实现原理
class MyProperty:
    def __init__(self,fget=None,fset=None,fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance,value)

    def __delete__(self,instance):
        self.fdel(instance)

class Test(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self,value):
        self._x = value

    def delx(self):
        del self._x

    x = MyProperty(getx,setx,delx)
test = Test()
test.x = 'yolo'
print(test.x)
print(test._x)

# 华氏温度与摄氏温度转化
class Hua:
    def __init__(self,value= 36.0):
        self.value = value
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)

class She():
    def __get__(self, instance, owner):
        return instance.hua *1.8 + 32
    def __set__(self, instance, value):
        instance.hua = (float(value/1.8)) - 32

class Test:
    hua = Hua()
    she = She()

test = Test()
print(test.hua)
test.hua = 52
print(test.she)