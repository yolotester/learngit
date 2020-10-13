def sum_2_num(num1, num2):
    '''
    对两个数字求和
    :return:sum
    '''
    sum = num1 + num2

    # 使用返回值， 告诉调用者函数执行的结果
    return sum


# 使用变量 --  接收函数的返回值
result = sum_2_num(50, 20)

print("计算结果为：%.2f" % result)
