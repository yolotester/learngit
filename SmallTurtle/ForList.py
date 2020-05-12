# for variable in sequence（list,tuple,str,files）：
#     循环体

y='fishc'
n = 0
for i in y:
    print('{a} : {b}'.format(a = n ,b =i))
    n += 1
else:
    print('out for')

# 循环列表，len是BIF，返回该数据的长度
member = ['wode ','祖国','aaaaaa','jljlkjlk']
n = 0
for i in member:
    print('{a} : {b}'.format(a = n , b = i))
    print(i,len(i))
    n += 1
else:
    print('out for list')

# range(start,stop,step).左闭右开
n = 0
for val in range(1,4):
    print('{a} : {b}'.format(a=n, b=val))
    n += 1
else:
    print('out for range')

fr = open('d:\\learnpython\\SmallTurtle\\ForList.py','r',encoding='utf-8')
lt = fr.readlines()
for val in lt:
    open('d:\\ddd.txt','a+').write(val)  # 如果用w+ 会覆盖文件内容，a+是在文件内容后追加
else:
    print('out file')

# 结果是自己想要的答案再退出程序
# bingo = 'yolo'
# word = input("请输入一句yolo喜欢的人的名字：")
# while True:
#     if word == bingo:
#         break
#     word=input('错啦，请重新输入')
# print('你可真棒 哦')
# print('对，就是她')




# list数据类型基本特点：1、可修改，可通过索引访问列表元素，也可以切片  2、可使用+ 符号连接成更大的列表
# 3、可动态增减，长度不固定  4、 list数据项可以是同类型/不同类型/也可以包含列表

# 空列表  列表可以包含所有数据对象，
empty = []
print(empty)
li1 = [12,'adv',2.55,[1,2,5]]
val = li1[1].replace('v','c')
print(val,'111111')

lt2 = iter(li1)   # 初次认识迭代器，iter（），迭代器有的方法，next（）方法用于遍历元素
print(type(lt2))
print(next(lt2))







# 列表的方法
# 在末尾插入元素/在任意位置插入元素
# append（）方法  只能增加一个参数    在末尾追加
number = [1,2,3,4]
number.append(3)
print(number,len(number),end='\n  ')   # [1, 2, 3, 4, 3] 5

# insert（）方法   在索引位置插入，前插
yl = [1,2,3,4]
yl.insert(yl.index(2),'yolo')
print(yl,len(yl))    #  [1, 'yolo', 2, 3, 4] 5

# extend()方法    在末尾以列表形式把每一个元素都用放在yolo列表，相当于n次append方法
yolo = [1,2,3,4]
yolo.extend(['yo','lo','sun'])
print(yolo,len(yolo))              # [1, 2, 3, 4, 'yo', 'lo', 'sun'] 7
print(yolo.append(yl))           # 返回NOne




# 通过索引获取列表元素值
print(yl[0])
print(yl[1])
temp = yl[0]
yl[0] = yl[1]
yl[1] = temp
print(yl , len(yl))




# 删除列表中元素的值
# 从列表删除元素
# remove(value)方法   删除列表中第一次出现的value，无返回值
yp = [0,1,3,5,8,4,4]
yp.remove(4)        # [0, 1, 3, 5, 8, 4],删除了第一个数字4
print(yp)
print('88888')

# del[index]语句   通过索引删除具体元素，类似于调用list中__delitem__这个魔法方法，无返回值
del yp[2]
print(yp)     # [0, 1, 5, 8, 4]，删除了索引是2的元素3
print(yp.__delitem__(4))     # 返回None，但已经默默的删除了索引值为4的元素4

# pop[index]方法  删除列表最后一个元素  括号内为索引值1，则删除索引值为1的元素，有返回值
yp.pop(1)      # 删除了索引值为1的元素1
print(yp)     # [0, 5, 8]









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
print(list1 > list2,'2222222')  # false
print((list1 < list2) and (list1 == list3))   # true

# 列表拼接 +  ，可以拼接成更大的列表  幂运算*
print(list1+list2)   # [123,456,234,456]
print(list1*3)       # [123, 456, 123, 456, 123, 456]
list1*=3
print(list1)            # [123, 456, 123, 456, 123, 456]

# 成员运算符  in
print(456 in list1)
print(456 not in list1)
list5 = [123,['yolo','doudou',456],567]
print('yolo' in list5[1])
print(list5[1][2])







# 列表中其他方法   list.sort()中.的意思是此方法作用于此对象
list6 = [5,8,22,98,56,78,1,98]

# count（value）方法，返回value元素在列表中出现的次数
print(list6.count(56))     # 1

# index（value，start，stop）方法返回value元素在列表中的索引
print(list6.index(98))

# reverse() 把列表反转一次,逆序
list6.reverse()
print(list6,'9999')    # [98, 1, 78, 56, 98, 22, 8, 5] 9999
print(list6[::-1])     # [5, 8, 22, 98, 56, 78, 1, 98] 逆序回来

# 对列表排序  默认从小到大排序  从大到小排序，则改变参数reverse=True
list6.sort()
print(list6)
list6.sort(reverse=True)
print(list6)











# 补充点   list8 = list7[:]复制一份    list9 = list7 类似于创建了快捷方式
list7 = [1,2,3,1]
list8 = list7[:]
print(list8)      # [1, 2, 3, 1]
print(id(list7))  # 1805131590152  内存地址
print(id(list8))   # 1805131590216  list8与list7内存地址不同，表示是新复制 了一个列表
list9 = list7
print(list9)      # [1, 2, 3, 1]
print(id(list9))   # 1805131590152  list9与list7内存地址相同，表示指向的是同一个列表



# 列表与函数：练习，计算出字符串中有多少个字符，列表可以作为形参，可以作为返回值
s = 'www.baidu.com-'
s1 = list(s)        # 将字符串转化为列表
s2 = list(s)
s3 = list(s)
def count_pop(listchars):    # 用pop方法
    while '.' in listchars:         # 不知道循环次数就使用while
        dl = listchars.pop(listchars.index('.'))     # s1为列表，就可以使用列表的方法
        print(dl)
    n = len(listchars)
    print('没有“.”在s中')
    return n                      # 返回列表的长度

def count_remove(listchars):
    while  '.' in listchars:
        print('remove.....')
        listchars.remove('.')
    n = len(listchars)
    print('没有“.”在s中')
    return n  # 返回列表的长度

def count_del(listchars):    # 用pop方法
    while '.' in listchars:         # 不知道循环次数就使用while
        del listchars[(listchars.index('.'))]     # s3为列表，就可以使用列表的方法
        print('del....')
    n = len(listchars)
    print('没有“.”在s中')
    return n                      # 返回列表的长度

def only_char(listchars ,sep):
    while sep in listchars:
        del listchars[(listchars.index(sep))]  # s4为列表，就可以使用列表的方法
        print('del....')
    return listchars         # 返回一个列表

s4 = list(s)
val = only_char(s4,'.')      # 用变量接收一个返回值列表
print(val)


val = count_pop(s1)                # 用一个变量来接收count_pop（）方法的返回值
print('in %s has %d char' % (s,val))

val = count_remove(s2)                # 用一个变量来接收count_pop（）方法的返回值
print('in %s has %d char' % (s,val))

val = count_del(s3)                # 用一个变量来接收count_pop（）方法的返回值
print('in %s has %d char' % (s,val))






# 列表与文件
# 读取文件
fe = open(r'D:\Git\learngit\test2.txt')
line = fe.readlines()    # readlines会返回一个列表，也会读取‘\n’
print(line)

i = 1  # 标识读取的行号
for val in line:
    val = val.rstrip('\n')    # 读取的时候，去除‘\n’
    print('i:',i,val)
    i += 1

# 写入文件
fe = open(r'D:\Git\learngit\test2.txt','w')
li = ['dou','doudou1','doudou2','doudou3']
li2 = range(1,10)
li3 = li + [li2]    # li3这个列表包含字符串和数字
print(li,'11111')
print(li2)
print(li3)

i = 0 # 构造一个循环控制变量，控制循环次数，构造循环条件的变量，用i做判断条件，这里做初始化
while i <= len(li) -1:
    fe.write(li[i] + '\n')    # write(str),这个方法只能写入字符串，且会覆盖文件中的原有内容
    i = i + 1           # 这里做修正

i = 0
while i <= len(li2) -1:
    fe.write(str(li2[i]) + '\n')
    i += 1

# isinstance(obj,type)  如果obj是type类型，返回true
i = 0
while isinstance(li3[i] ,int):
    fe.write(str(li3[i]) + '\n')
    i += 1
else:
    fe.write(li3[i] + '\n')



fe.close()


