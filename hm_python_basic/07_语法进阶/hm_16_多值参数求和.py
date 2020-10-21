# def test(*args):
def test(args):

    sum = 0

    # 循环遍历元组中的元素 并求和
    for k in args:
        sum += k

    print(args)
    return sum

result = test((1, 2, 3))
# result = test(1, 2, 3)
print(result)
