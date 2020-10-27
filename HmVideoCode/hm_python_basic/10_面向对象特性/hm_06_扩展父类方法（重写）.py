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

    def bark(self):

        # 针对子类特有的需求，编写代码
        print("特定需求要像神一样叫")

        # 在需要的位置，使用super(). ，调用原本在父类中封装的方法
        super().bark()

        # 增加子类其他的代码
        print("这是子类其他的代码")

# 创建一个哮天犬对象
xtq = XiaoTianQuan()

# 如果在子类中，重写了父类的方法
# 在使用子类对象调用方法时， 会调用子类中重写的方法
xtq.bark()
