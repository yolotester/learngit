# 元组是不可改变的    与列表使用相似
# 创建元组
tuple = (1,2,3,5,5)
for i in tuple:
    print(i)

# 使用索引访问元组
print(tuple[1])

# 创建空元组
tuple1 = ()

# 创建只有一个元素的元组
tuple2 = (3,)
tuple3 = 4,
print(type(tuple2))
print(type(tuple3))

# 小陷阱   重复操作符
print(8*(8))
print((8*(8,)))

# 更新元组/字符串  需要用切片的方式先切开再拼接     PYthon 回收机制会把旧的temp回收掉，temp指针指向新的元组
temp = ('yolo','dou','dou')
temp = temp[:1]+('love',)+temp[1:]
print(temp)

# 删除元组   del语句  （先复制一份temp）
temp1 = temp[:]
print(temp1)
# del temp
# print(temp)      会报错

# 成员运算符
print('yolo' in temp)
print('yolo' not in temp)

# 关系运算符
print(temp > temp1)
print(temp == temp1)
print(temp < temp1)

# 逻辑运算符
print((temp == temp1) and (temp != tuple2))

