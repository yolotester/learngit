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
yl.remove(4)

# del语句   删除具体元素，需要索引查到元素
del yl[0]

# pop方法  删除列表最后一个元素
yl.pop()