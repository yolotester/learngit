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
# print(Tool.count)

# 不推荐使用对象变量访问类属性
# 使用对象名访问 类属性 的问题
# 如果使用 对象.类属性 = 值 赋值语句，只会 给对象添加一个属性，而不会修改到 类属性的值
tool1.count = 3
print("使用对象变量访问类属性--- %d" % tool1.count)

# 并不会修改到 类属性的值
print("使用对象变量访问类属性--- %d" % Tool.count)