name_list = ["zhang", "san", "lisi"]

# 使用del，关键字（delete） 传递索引，删除列表元素
# 提示：从列表中删除数据，建议使用列表提供的方法
del name_list[1]

# del 关键字本质上是用来将一个变量从  内存中  删除
name = "heima"

del name

# 注意：使用del关键字将变量从内存中删除后
# 后续的代码就不能使用这个变量了
# print(name)  # NameError: name 'name' is not defined

print(name_list)