class Tool(object):

    # 使用 赋值语句 定义类属性， 记录所有  工具对象  的数量
    count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性的值 +1
        Tool.count += 1

    # 定义类方法
    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量 %d" % cls.count)


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("锯子")

# 调用类方法
Tool.show_tool_count()
