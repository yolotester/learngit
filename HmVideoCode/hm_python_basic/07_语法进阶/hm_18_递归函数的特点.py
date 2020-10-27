def test(num):

    print(num)

    # 递归的出口， 很重要。当参数，满足这个条件后，则函数不再执行
    if num == 0:
        return

    # 特点：自己调用自己, 参数不能相同
    test(num - 1)


test(3)  # 没有递归出口，导致死循环RecursionError: maximum recursion depth exceeded while calling a Python object

