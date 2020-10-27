try:
    num = int(input("请输入一个整数："))

    result = 8 / num
    print(result)

except ValueError:
    print("请输入正确的数字：")

# 在开发中，很难预判到所有可能出现的错误。所以增加一个万能异常捕获
except Exception as e:
    print("未知错误 -- %s" % e)