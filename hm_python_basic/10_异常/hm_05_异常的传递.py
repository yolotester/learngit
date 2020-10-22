def demo1():
    return  int(input("请输入整数:"))


def demo2():
    # 调用demo1方法
    return  demo1()


try:
    print(demo2())
except Exception as e:
    print("未知错误 --  %s" % e)