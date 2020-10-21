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



xiaoming = Person("小明", 75)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

