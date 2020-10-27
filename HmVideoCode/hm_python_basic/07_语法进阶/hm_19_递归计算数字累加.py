def sum_numbers(num):

    # 递归的出口
    if num == 1:
        return 1

    # 假设sum_numbers这个函数能够处理，1+...+   num-1 的和，则再加上num就可以计算出结果
    temp = sum_numbers(num - 1)
    return num + temp


result = sum_numbers(3)
print(result)
