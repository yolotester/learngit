# 迭代器：可迭代的对象，返回的引用（实现了__iter__ 和  __next__魔法方法）称之为迭代器
from collections.abc import Iterable,Iterator

# 自定义一个可迭代的类


class classiterable(object):
    def __init__(self):
        self.names = list()  # 创建一个空列表

    def add(self,name):
        return self.names.append(name)

    def __iter__(self):
        return classiterator(self)  # 把classiterable类的引用，给classiterator类


class classiterator(object):

    def __init__(self,obj):
        self.obj = obj   # 用一个属性self.obj接收classiterable类的引用
        self.current = 0
    def __iter__(self):
        pass

    def __next__(self):

        if self.current < len(self.obj.names):
            ret =  self.obj.names[self.current]
            self.current += 1
            return ret
        else:
            raise StopIteration

class1 = classiterable()
class1.add('yolo')
class1.add('dou')
class1.add('dou1')

# class2= iter(class1)  # 将一个可迭代的对象变为迭代器
# print(next(class2))
# print('判断class1是否是可迭代的对象' , isinstance(class1,Iterable))
# print('判断class2是否是迭代器',isinstance(class2,Iterator))

for val in class1:  # 经历的三步：1、class1中实现了__iter__方法  2.class1中__iter__方法调用时，__iter__方法的返回值中的引用实现了__next__方法   3、class1中__iter__方法的返回值就是一个迭代器
    print(val)
