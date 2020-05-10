# 字典=关系数组    ，python中唯一的映射类型
# yolo 为键key   doudou 为值value   yolo：doudou键值对
dict1 = {'李宁':'一切皆有可能','yolo':'doudou','Nike':'Just do it',1:'one'}
print('yolo的女朋友是：',dict1['yolo'])

# 创建空字典   用关键字创建字典
dict2={}
dict3 = dict(yolo = 'doudou的男朋友',doudou = 'yolo的女朋友')
dict4 = dict((('a',65),('b',66)))

# 访问字典的方法，keys（），values（）,items（）
print(dict1[1])
dict1 = dict1.fromkeys(range(10),'yolo')
for eachKey in dict1.keys():
    print(eachKey)

for eachValue in dict1.values():
    print(eachValue)

for eachItem in dict1.items():
    print(eachItem)

# get()方法访问字典，即使键不存在，也不会报错  例如键11不在字典dict1里，没有报错而是返回了None
print(dict1.get(11))
print(dict1.get(11,'没有这个键'))

# in 和 not in  成员操作符
print(10 in dict1)
print(10 not in dict1)

# 清空字典用clear（）方法   疑问;不是返回的空字典，返回None
print(dict1.clear())

# copy（），浅拷贝只是对表层的复制，赋值是一个内容贴上了两个标签
a = {1:'one',2:'two'}
b = a.copy()
c = a
print(id(a))
print(id(b))
print(id(c))

# pop()弹出删除的键值对，popitem随机删除一对键值对
print(a.pop(1))
print(a)
# print(a.popitem())

# setdefault()  为字典设置键值对   有疑问，打印a并没有把显示出字典a，而是显示的doudou
print(a.setdefault('yolo','doudou'))
print(a)

dict = {'Name': 'Runoob', 'Age': 7}

print("Age 键的值为 : %s" % dict.setdefault('Age', None))
print("Sex 键的值为 : %s" % dict.setdefault('Sex', None))
print("新字典为：", dict)

# update（）方法，用一个字典来更新另一个字典
contact = {'request':'invite','professional':'networking'}
a.update(contact)
print(a)

# 为字典的键赋值，若在字典中查不到该键，则在字典中创建该键
dict1['Nike'] = 'just do it'
print(dict1)
dict1['adidas'] = 'nothing is impossable'
print(dict1)

# fromkeys方法fromkeys(S,[v])   S为字典的键，v为这些键的值
dict5 = {}
print(dict5.fromkeys((1,2,3)))
print(dict5.fromkeys((1,2,3),'yolo'))