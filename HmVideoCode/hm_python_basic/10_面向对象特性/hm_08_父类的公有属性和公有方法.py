class A:

    def __init__(self):

        self.num1 = 100
        self.__num2 = 200

    def __secret(self):
        print("私有方法中使用公有属性和私有属性 %d %d" % (self.num1, self.__num2))

    def test(self):

        # 可以通过 父类 的 公有方法 间接 访问到 私有属性 或 私有方法
        print("父类的公有方法，间接输出父类的私有属性 %d" % self.__num2)
        self.__secret()


class B(A):

    def demo(self):

        # 在子类的对象方法内部， 不能使用父类的私有属性
        # print("访问父类的私有属性 %d" % self.__num2)
        # 在子类的对象方法内部， 不能调用父类的私有方法
        # self.__secret()

        # 在子类的对象方法内部， 可以使用父类的公有属性
        print("在子类中输出父类的公有属性 %d" % self.num1)

        # 在子类的对象方法内部， 可以调用父类的公有方法
        self.test()

        pass


# 创建一个子类对象
b = B()

# 在外部 可以 访问父类的公有属性/公有方法
# print(b.num1)
# b.test()

b.demo()