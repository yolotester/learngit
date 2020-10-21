class Cat:

    def __init__(self, new_name):

        self.name = new_name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 去了" % self.name)

    def __str__(self):

        # 必须返回一个字符串
        return "这是[%s]" % self.name


# tom是一个全局变量，只有全部代码执行后，才会从内存中销毁
tom = Cat("Tom")
print(tom)
