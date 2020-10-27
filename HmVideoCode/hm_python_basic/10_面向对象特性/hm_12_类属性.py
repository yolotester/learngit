class Tool(object):

    # 使用 赋值语句 定义类属性， 记录所有  工具对象  的数量
    count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性的值 +1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("锯子")

# 输出工具对象的总数
print(Tool.count)