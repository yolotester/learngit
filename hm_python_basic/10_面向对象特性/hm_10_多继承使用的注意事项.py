class A:

    def test(self):
        print("A---test 方法")

    def demo(self):
        print("A---demo 方法")


class B:

    def test(self):
        print("B---test 方法")

    def demo(self):
        print("B---demo 方法")


class C(A, B):
    '''多继承可以让子类对象，同时具有多个父类的属性和方法'''
    pass


# 创建一个子类对象
c = C()
c.test()
c.demo()

# 在多继承时判断方法、属性的调用路径
print(C.__mro__)
