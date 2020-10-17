import copy

#  对列表的操作

a = [11,22]
b = [33,44]
c = [a,b]
d = copy.deepcopy(c)
print(id(d))  # 3100521054344
print(id(c))  # 3100775825352

print(c)  # [[11, 22], [33, 44]]
print(d)  # [[11, 22], [33, 44]]

a.append(55)

print(c)  # [[11, 22, 55], [33, 44]]
print(d)  # [[11, 22], [33, 44]]

c.append(66)

print(c)  # [[11, 22, 55], [33, 44], 66]
print(d)  # [[11, 22], [33, 44]]


# 对元组的操作

a = (11,22)
d = copy.deepcopy(a)

print(id(a))  # 2693457431112
print(id(d))  # 2693457431112

a = [11,22]
b = [33,44]
c = (a,b)
d = copy.deepcopy(c)

print(id(c))  # 1657847769736
print(id(d))  # 1657847512008

a.append(55)
print(c)
print(d)