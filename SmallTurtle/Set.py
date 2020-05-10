# 集合
comeWith = {1,2,3,5}
print(type(comeWith))

# 集合唯一性
sides = {1,1,3,3,4,4}
print(sides)

# 集合的无序性，无法索引

# 使用工厂函数创建集合
dessert = set([1,'d',6])
print(dessert)

# 去除列表中重复的元素
desert = [1,2,3,4,5,4,3,0]
temp = []
for each in desert:
    if each not in temp:
        temp.append(each)
print(temp)

# 第二种方式   set
water = list(set(desert))
print(water)

# 使用for读取集合中的元素
for each in desert:
    print(each)

# 成员运算符 in  not in


# add()方法
desert = dessert.add(7)
print(dessert)

# remove()方法
desert = dessert.remove(6)
print(dessert)


# 不可变集合 frozen
seaFood = frozenset([1,5,'s'])
print(seaFood)

















