# 全局变量
num = 10


def demo1():

    # 希望 --  修改全局变量的值
    # 在python中， 不允许直接修改全局变量的值
    # 下方代码的意思是  --  如果只会在函数内部使用赋值语句，只会定义一个局部变量num
    num = 99
    print("demo1 ==> %d" % num)


def demo2():
    print("demo2 ==> %d" % num)


demo1()
demo2()
print("over!")