# encoding=gbk
# 与类有关的内置函数
# issubclass(class,classinfo)    判断一个类是否是另一个类的子类
# 1.一个类默认为自身的一个子类
# 2.classinfo可以是类对象组成的元组,只要class是其中任何一个候选类的子类,则返回True
class A:
    pass
class D:
    pass
class B(A):
    pass
print(issubclass(B,A))
print(issubclass(B,B))
print(issubclass(B,D))

# isinstance(object,classinfo)  检查一个实例对象是否属于一个类
# 1.如果第一个参数不是对象,则永远返回false
# 2.如果第二个参数不是类或者由类对象组成的元组,会抛出一个TypeError的异常
b = B()
print(isinstance(b,B))
print(isinstance(b,A))
print(isinstance(b,D))
print(isinstance(b,(A,B)))

# hasattr(object,name)   检查name是否是对象的属性名
class C:
    def __init__(self,x=0):
        self.x = x
c = C()
print(hasattr(c,'x'))
# print(hasattr(c,x))     NameError: name 'x' is not defined

# getattr(o,name,[default])   检查name是否是对象的属性名,若没有该属性且设置了默认值,则显示默认值
print(getattr(c,'x'))
# print(getattr(c,'y'))        AttributeError: 'C' object has no attribute 'y'
print(getattr(c,'y','你所访问的属性不存在...'))

# setattr(o,name,value)       检查name是否是对象的属性名,若没有该属性且设置了value值,则为该对象创建该属性且赋value值
setattr(c,'z','yolo')
print(getattr(c,'z'))

# delattr(o,name)             删除对象指定的属性,若对象中没有该属性.会报出AttributeError的异常
# print(delattr(c,'l'))         AttributeError: l
print(delattr(c,'x'))
print(hasattr(c,'x'))

# property(fget=None,fset=None,fdel=None)  #
class C:
    def __init__(self,size=10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self,value):
        self.size =value
    def delSize(self):
        del self.size
    x= property(getSize,setSize,delSize)

c = C()
print(c.getSize())
print(c.x)   #fget
c.x = 18    #fset
print(c.getSize())
del c.x    #fdel
print()


