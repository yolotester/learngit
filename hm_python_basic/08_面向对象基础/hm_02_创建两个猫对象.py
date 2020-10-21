

class Cat:

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


# 创建猫对象
tom = Cat()
tom.eat()
tom.drink()

# 再创建一个猫对象
lazy_tom = Cat()
lazy_tom.eat()
lazy_tom.drink()

# tom 和 lazy_tom 虽然都是Cat类创建的对象，但是 是不同的对象
print(tom)
print(lazy_tom)