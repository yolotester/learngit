class Cat:

    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 爱喝水" % self.name)


# 创建猫对象
tom = Cat()

# 可以使用 对象名.属性名，利用赋值语句就可以了
# 不推荐使用这种方式，因为：对象属性的封装应该封装在类的内部
tom.name = "豆豆"
tom.eat()
tom.drink()
print(tom.name)

#隐患就是，若方法未找到该属性，程序会报错
# tom.name = "豆豆"  # AttributeError: 'Cat' object has no attribute 'name'