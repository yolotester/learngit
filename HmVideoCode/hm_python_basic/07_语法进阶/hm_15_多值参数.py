def test(num, *args, **kwargs):

    print(num)
    print(args)
    print(kwargs)


test(1)  # 第一个参数永远会给num形参
test(1, 2)  # 其他参数会以元组的形式传递给args参数
test(1, 2, name="小明", age=18)  # 指定参数名的参数永远会给kwargs参数