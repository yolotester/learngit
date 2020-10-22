try:
    num = int(input("请输入一个整数："))

    result = 8 / num
    print(result)

except ValueError:
    print("请输入正确的数字：")

except ZeroDivisionError:
    print("除0错误")