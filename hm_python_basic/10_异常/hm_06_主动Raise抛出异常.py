def input_password():

    # 1、提示用户输入密码
    password = input("请输入密码：")

    # 2、判断密码长度 >= 8, 返回用户输入的密码
    if len(password) >= 8:
        return password

    # 3、如果 < 8, 主动抛出异常
    # print("主动抛出异常")
    # 1>创建异常对象 --  可以使用错误信息字符串作为参数
    e = Exception("密码长度不够")

    # 2>主动抛出异常
    raise e


# 在主程序中，可以捕获到主动抛出的异常
try:
    accept = input_password()
    print(accept)
except Exception as result:
    print(result)