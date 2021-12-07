'''
需求：
1、开发一个 sum_2_number 的函数
2、函数实现 两个数字求和 的功能
'''


def sum_2_number(num1, num2):  # 形参 --  定义函数时， 小括号中的参数是用来接收参数的， 在函数内部当作变量使用
    """
    对两个数字求和
    :return:
    """
    # num1 = 10
    # num2 = 20
    sum = num1 + num2
    print("%d + %d = %d" % (num1, num2, sum))


sum_2_number(40, 30)  # 实参 --  调用函数时， 小括号中的参数，是用来把数据传递到函数内部的