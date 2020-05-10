# 列表，元组，字符串总结    共同点       都是序列！！！！1
'''
1、都可以通过索引值得到每一个元素
2、默认索引值总是从0开始
3、通过分片的方法得到一个范围内的元素集合
4、有很多共同的操作符（成员操作符，关系操作符，逻辑操作符）

'''
# 序列中BIF  builts_in_functions  内置函数
# 迭代：迭代是重复反馈过程的活动，其目的通常是为了接近并到达所需的目标或结果。
# 每一次对过程的重复被称为一次“迭代”，而每一次迭代得到的结果会被用来作为下一次迭代的初始值。
# list()  1、生成空列表   2、list（[iterable]）  把一个可迭代对象转换为列表
a = 'i love dou dou.com'
print(list(a))

b = (1,1,2,3,5,8,13,21,34)
print(list(b))

# tuple()  1、生成空元组   2、list（[iterable]）  把一个可迭代对象转换为元组



# str(obj)   把obj对象转换成字符串    类型转换
c = 2
d = str(2)
print(d)
print(isinstance(d,str))

# len(sub)   返回这个参数的长度
print(len(a))

# max(sub)  返回序列或者参数集合里面的最大值   保证数据类型是统一的
print(max(1,2,3))
print(max(a))

# min（sub)   返回序列或者参数集合里面的最小值    保证数据类型是统一的
print(min(1,2,3))
print(min(a))
chars = '01245125'
print(min(chars))

# sum(iterable[,start=0])  返回序列iterable和可选参数start的总和
print(sum(b))
print(sum(b,12))

# sorted()   从小到大排序，返回一个列表
yolo = [0,5,6,2,8]
print(sorted(yolo))
print(yolo)

# reversed()  返回一个迭代器对象,功能反转
print(reversed(yolo))
print(list(reversed(yolo)))

# enumerate()   返回enumerate对象，功能把元素和元素索引值组成一个元组
print(enumerate(yolo))
print(list(enumerate(yolo)))

# zip  举例说明,返回一个列表，成对打包
f = [1,2,3,4,5,6]
g = [4,5,6]
print(zip(f,g))
print(list(zip(f,g)))



