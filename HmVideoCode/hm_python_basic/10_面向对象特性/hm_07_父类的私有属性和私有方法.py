class A:

    def __init__(self):

        self.num1 = 100
        self.__num2 = 200

    def __secret(self):
        print("私有方法中使用属性 %d %d" % (self.num1, self.__num2))


class B(A):

    def demo(self):

        # 在子类的对象方法中， 不能使用父类的私有属性
        # print("访问父类的私有属性 %d" % self.__num2)
        # 在子类的对象方法中， 不能调用父类的私有方法
        # self.__secret()
        pass


# 创建一个子类对象
b = B()
b.demo()
print(b.num1)