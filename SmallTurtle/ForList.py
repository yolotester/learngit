y='fishc'
for i in y:
    print(i,end=' ')


member = ['wode ','祖国','aaaaaa','jljlkjlk']
for i in member:
    print(i,len(i))
# for循环 有冒号，len是BIF，返回该数据的长度

# 结果是自己想要的答案再退出程序
# bingo = 'yolo'
# word = input("请输入一句yolo喜欢的人的名字：")
# while True:
#     if word == bingo:
#         break
#     word=input('错啦，请重新输入')
# print('你可真棒 哦')
# print('对，就是她')

# 空列表  列表可以包含所有数据对象
empty = []
print(empty)


# append（）方法  只能增加一个参数    在末尾追加
number = [1,2,3,4]
number.append(3)
print(number,len(number),end='\n  ')

# extend()方法    以列表形式来扩展列表   在末尾追加
yolo = [1,2,3,4]
yolo.extend(['yo','lo','sun'])
print(yolo,len(yolo))

# insert（）方法   在索引位置插入
yl = [1,2,3,4]
yl.insert(1,'yolo')
print(yl,len(yl))

# 获取元素值  以index方式
print(yl[0])
print(yl[1])
temp = yl[0]
yl[0] = yl[1]
yl[1] = temp
print(yl , len(yl))

# 从列表删除元素
# remove()方法   直接使用列表元素名字
# yl.remove(4)

# del语句   删除具体元素，需要索引查到元素
# del yl[0]

# pop方法  删除列表最后一个元素  括号内为索引值1，则删除索引值为1的元素
# yl.pop(1)

# slice分片   列表的复制  [start:stop:步长]

spring = yl[:]
print(spring)

print(spring[:3])
print(spring[1:])

print(spring[:4:2])

# 列表的运算符
# 比较运算符 > 逻辑运算符
list1 = [123,456]
list2 = [234,456]
list3 = [123,456]
print(list1 > list2)
print((list1 < list2) and (list1 == list3))

# 列表拼接 +    幂运算*
print(list1+list2)
print(list1*3)
list1*=3
print(list1)

# 成员运算符  in
print(456 in list1)
print(456 not in list1)
list5 = [123,['yolo','doudou',456],567]
print('yolo' in list5[1])
print(list5[1][2])

# 列表中其他方法   list.sort()中.的意思是此方法作用于此对象
list6 = [5,8,22,98,56,78,1,98]

# 返回元素在列表中出现的次数
print(list6.count(56))

# 返回元素在列表中的索引，可设定范围
print(list6.index(98,4,8))

# 把列表反转一次
list6.reverse()
print(list6)

# 对列表排序  默认从小到大排序  从大到小排序，则改变参数reverse=True
list6.sort()
print(list6)
list6.sort(reverse=True)
print(list6)

# 补充点   list8 = list7[:]复制一份    list9 = list7 类似于创建了快捷方式
list7 = [1,2,3,1]
list8 = list7[:]
list8 = list7[:]
list9 = list7
list7.sort()
print(list7,list8,list9)



