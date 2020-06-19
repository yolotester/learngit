# 生成器是一种特殊的迭代器
# 生成器两种方式：1、列表推导式，把[]换位（），则是一个生成器   2、函数中带yield语句，这此函数的调用成为创建一个生成器对象


def fibonacci(all_num):

    a, b = 0, 1

    current_num = 0
    while current_num < all_num:
        # print(a)
        ret = yield  a  # 代码执行到yield语句，就相当于暂停这个程序
        print('>>>>>',ret)
        a, b = b, a+b
        current_num += 1
    return 'ok====='

obj = fibonacci(2)  # 创建一个生成器对象
ret = next(obj)
print(ret)

ret = obj.send("hahahah")  # send 语句启动生成器的另一种方式   0
                                                            # >>>>> hahahah
                                                            # 1

print(ret)

# while True:
#     try:
#        # ret = next(obj)
#         ret = obj.send('hahaha')
#         print(ret)
#     except StopIteration as ret:  # 当生成器对象中没有值时，及next（obj）没有返回值时，抛出异常
#         val  = ret.value  # 通过异常变量的value值，来获得生成器中return中的返回值
#         print(val)
#         break




# for val in obj:  # in 后面是一个可迭代的对象，生成器是一种特殊的迭代器，迭代器肯定是可迭代的对象
#
#     print(val)

