name = "小明"

# python 解释器 只知道下方定义了一个函数


def say_hello():
    """
    打招呼
    :return:
    """
    print("say hello -- 1")
    print("say hello -- 2")
    print("say hello -- 3")


print(name)

# 只有在程序中， 主动调用了函数，才会让函数执行
say_hello()

print(name)
