# 属性访问
# __getattr__(self,name) ,定义当用户试图获取一个不存在的属性时的行为
# __getattribute__(self,name), 定义当该类的属性被访问时的行为
# __setattr__(self,name,value) ,定义当一个属性被设置时的行为
# __delattr__(self,name) , 定义当一个属性被删除时的行为
class Attr():

    def __getattribute__(self, name):
        print('getattribute')

        return super().__getattribute__(name)
    def __getattr__(self,name):
        print("getattr")
    def __setattr__(self, name, value):
        print('setattr')
        super().__setattr__(name,value)
    def __delattr__(self, name):
        print("delattr")
        super().__delattr__(name)
attr = Attr()
print(attr.x)
attr.x = 2
print(attr.x)
del attr.x
print(attr.x)

# 陷阱
class Rectangle():
    def __init__(self,width = 0,height=0):
        self.width = width
        self.height = height
    def __setattr__(self, name,value):  # 重写魔法方法比较好的一种方式,使用super()方法调用父类方法
        if name == "square":
            self.height = value
            self.width = value
        else:
            # self.name = value  无限递归  RecursionError: maximum recursion depth exceeded in comparison
           # super().__setattr__(name,value)
             self.__dict__[name] = value
    def get_area(self):
        return self.width * self.height
rec = Rectangle(5,6)
print(rec.get_area())

# example 1
class Fjs(object):
    def __init__(self,name):
        self.name = name
    def hello(self):
        print('said by :' ,self.name)
    def fjs (self,name):
        if name == self.name:
            print('yes')
        else:
            print("no")
class Wrap_Fjs(object):
    def __init__(self,fjs):
        self._fjs = fjs
    def __getattr__(self, name):
        if name == 'hello':
            print('调用hello方法了...')
        elif name == 'fjs':
            print('调用fjs方法了...')
        return getattr(self._fjs,name)

fjs = Wrap_Fjs(Fjs('fjs'))
fjs.hello()
fjs.fjs('fjs')