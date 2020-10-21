class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("会飞哦")


class Cat(Animal):

    def catch(self):
        print("抓老鼠")


# 创建一个哮天犬对象
xtq = XiaoTianQuan()
xtq.fly()  # 调用自己类的方法
xtq.bark()  # 调用父类Dog类的方法
xtq.eat()  # 调用爷爷类Animal类的方法

# xtq.catch()  # XiaoTianQuan类并没有直接继承Cat类，所以不能调用Cat类中的方法