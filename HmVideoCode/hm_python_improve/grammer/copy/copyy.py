# 赋值语句，copy.copy方法，列表的切片，字典的copy方法，函数的传参都是浅拷贝
import copy

# 赋值语句
b = 45
a = b
print(id(b))
print(id(a))

# 列表
a = [11,22]
b = [33,44]
c = [a,b]
d = copy.copy(c)
print(id(c))
print(id(d))

print(id(c[0]))  # id 值相同
print(id(d[0]))

a = [11,22]
b = [33,44]
c = (a,b)
d = copy.copy(c)
print(id(c))
print(id(d))

print(id(c[0]))  # id 值相同
print(id(d[0]))

# 列表的切片
a = [11,22]
b = [33,44]
c = [a,b]
d = c[:]
print(id(c))
print(id(d))

a.append(44)

print(c)  # 打印结果相同
print(d)


# 字典的copy方法
dict1 = {'yolo':'123',123:'451','doudou':[11,22]}
dict2 = dict1.copy()

print(id(dict1))
print(id(dict2))

dict1['doudou'].append(33)
print(dict1)
print(dict2)


# 函数的传参
def test(nums):
    nums.append(33)

nums = [11,22]
test(nums)

print(nums)  # [11, 22, 33]

test(copy.deepcopy(nums))
print(nums)  # [11, 22, 33]

test(nums)
print(nums)  # [11, 22, 33, 33]