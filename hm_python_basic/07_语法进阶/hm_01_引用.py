def test(num):

    print("在函数内部 %d 对应的内存地址是 %d" % (num, id(num)))

    # 1.定义一个字符串变量，打印这个字符串的内存地址
    result = "hello"
    print("result 变量中保存数据的内存地址是 %d" % id(result))

    # 2.返回这个字符串变量，
    return result

# 定义一个数字的变量
a = 10

print("a 变量中保存数据的内存地址是 %d" % id(a))

# 调用 test 函数，本质上传递的是实参保存数据的引用，而不是实参保存的数据
# 注意：如果函数有返回值，但是没有定义变量接收
# 程序不会报错， 但是无法获得返回结果
r = test(a)
print("%s 的内存地址是 %d" % (r, id(r)))
