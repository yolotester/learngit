class Person:

    def __init__(self, name, weight):

        # self.属性名 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "%s 的体重是 %.1f 公斤" % (self.name, self.weight)

    # 在对象的方法内部， 是可以直接访问对象的属性的
    def run(self):

        print( "%s爱跑步" % self.name)
        self.weight -= 0.5

    def eat(self):

        print( "%s爱吃饭" % self.name)
        self.weight += 1



# 小明爱跑步
xiaoming = Person("小明", 75)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

# 小美爱跑步
xiaomei = Person("小美", 45)
xiaoming.run()
xiaoming.eat()
print(xiaomei)

# 同一个类创建的 多个对象 之间， 属性互不干扰
print(xiaoming)


