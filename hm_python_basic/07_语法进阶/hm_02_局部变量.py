def demo1():

    # 定义一个局部变量
    # 出生 -- 定义局部变量的代码执行时 才会被创建
    # 死亡 -- 函数执行结束后，被系统回收
    num = 10

    print("在demo1函数内部定义的局部变量是 %d" % num)


# print("%d" % num)  在函数内部定义的变量，不能在函数外部使用

def demo2():

    num  = 99
    print("demo2 == > %d" % num)
    # print("%d" % num)  在函数内部定义的变量，其他函数不能使用
    pass

# 局部变量  是在 函数内部定义的变量， 只能在函数内部使用

demo1()
demo2()
print("over!")