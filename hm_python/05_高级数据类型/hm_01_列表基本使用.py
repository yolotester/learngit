name_list = ["zhang", "san", "lisi"]

# 1、取值
# print(name_list[3])  # IndexError: list index out of range -列表索引超出范围
print(name_list[0])

# 1、取索引
# 知道数据内容，想确定数据在列表中的位置
# 使用index 方法注意：如果传递的数据不在列表中，程序会报错！！！
print(name_list.index("lisi"))


# 2、修改
name_list[1] = "YYY"


# 3、增加
# append方法可以向列表末尾追加数据
name_list.append("hhh")

# insert方法可以在列表的 指定索引位置 插入数据
name_list.insert(1, "ooo")

# extend方法可以把其他列表完整内容，追加到当前列表的末尾
temp_list = ["hello", "python"]
name_list.extend(temp_list)


# 4、删除
# remove方法可以从列表中删除 指定的数据
name_list.remove("ooo")
# pop方法默认可以把列表中最后一个元素删除，返回删除的元素
item = name_list.pop()
print(item)
# pop方法也可以指定要删除元素的索引， 返回删除的元素
name_list.pop(3)
# clear方法清空列表
name_list.clear()


print(name_list)
