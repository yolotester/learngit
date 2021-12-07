def test1():
    print("*" * 10)


def test2():
    print("-" * 10)

    # 函数的嵌套调用
    # 执行完test1函数内的代码后，会返回到函数调用的位置
    test1()

    print("+" * 10)


test2()