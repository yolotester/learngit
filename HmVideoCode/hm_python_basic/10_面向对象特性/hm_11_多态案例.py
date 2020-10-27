class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 快乐的玩耍" % self.name)


class XiaoTianDog(Dog):

    def game(self):
        print("%s 飞到天上去玩耍" % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍" % (self.name, dog.name))

        # 让狗玩耍
        dog.game()


# 创建一个Dog对象
# wangcai = Dog("旺财")
# 创建一个XiaoTianDog对象
wangcai = XiaoTianDog("飞天旺财")

# 创建一个Person对象
xiaomei = Person("小美")

# 让小美调用 game_with_dog 方法
xiaomei.game_with_dog(wangcai)