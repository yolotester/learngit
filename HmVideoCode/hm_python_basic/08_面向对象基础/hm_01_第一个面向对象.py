'''
需求： 小猫 爱 吃鱼  小猫 爱 喝水
'''

class Cat:

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


# 创建猫对象
tom = Cat()
tom.eat()
tom.drink()

print(tom)  # <__main__.Cat object at 0x000001903E6198D0>

addr = id(tom)
print("%x" % addr)