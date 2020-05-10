# 推导式包括列表推导式，字典推导式，集合推导式
# 列表推导式
# variable = [out_exp_res for out_exp in input_list if out_exp == 2]
# out_exp_res：列表生成元素表达式，可以是有返回值的函数。
# for out_exp in input_list：迭代input_list将out_exp传入out_exp_res表达式中。
# if out_exp == 2：根据条件过滤哪些值可以。
# 举例说明
a = [i for i in range(10) if not(i%2) and i%3]   # 0-9能被2整除并且不能被3整除的数
print(a)

d = {'x':'A','y':'B','z':'C'}
print([k+'='+v for k,v in d.items()])    # 使用两个变量也可以推导出list

L = ['YOLO','douDou','fishC']
list1 = [s.upper() for s in L]    # 使用有返回值的函数也可以推导出list
print(list1)

def squared(x):
    return x *x
multi = [squared(i) for i in range(10) if i % 3 ==0]
print(multi)

print([m+n for m in 'abc' for n in 'xyz'])   # 使用两层循环推导出list,生成全排列

# for前面的if...else是表达式，for后面的if是筛选条件，不能带else
print([i if i %2==0 else -i for i in range(10)])   # 若不带else，会报错

# 练习,列表中有字符串有数字，由于非字符串没有lower（）方法，生成式会报错
L1 = ['Yolo',18,'DOudou']
L2 = [x.lower() for x in L1 if isinstance(x,str)]
print(L2)
if L2 == ['yolo','doudou']:
    print('测试通过！')
else:
    print('测试失败！')

# 生成间隔5分钟的时间列表序列
print(['%02d : %02d' % (h,m) for h in range (0,24) for m in range(0,60,5)])

# 求（x，y），其中x是0-5之间的偶数。y是0-5之间的奇数组成的元组列表
print([(x,y) for x in range(5) if x %2==0 for y in range(5) if y%2 ==1])

# 把字典中age键，按照条件赋新值
bob = {'pay':3000,'age':42}
sue = {'pay':5000,'age':45}
people = [bob,sue]
age1 = [rec['age'] +100 if rec['age'] >=45 else rec['age'] for rec in people]
print(age1)

# 求M中斜线1，5，9组成的列表
M = [[1,2,3],[4,5,6],[7,8,9]]
print([M[i][i]for i in range(len(M))])
# 求M中3，6，9组成的列表
print([row[2] for row in M ])
print([M[row][2] for row in range(len(M))])



# 字典推导式
# 字典推导和列表推导的使用类似，只不过中括号改成大括号。
# 基本格式：{ key_expr: value_expr for value in collection if condition }
# # 举例说明
dict = {i:i %2==0 for i in range(10)}  # 0-9 能被2整除的数为true
print(dict)

# 用字符串和其下标创建字典
str = ['yolo','doudou','ling']
dict = {key:val for val,key in enumerate(str)}  # enumerate(suquence,[start=0])返回元素下标和元素
print(dict)

# 大小写key合并,合并成小写
m = {'a':10,'b':34,'A':7,"Z":3}
mcase_frequency = {k.lower():m.get(k.lower(),0) + m.get(k.upper(),0)
                   # get(self,k),访问字典中键的值，若没有此键，返回NOne，设置默认值返回默认值
                   for k in m.keys()
                   if k.lower() in ['a','b']
                   }
print(mcase_frequency)

# 快速更换key和value
m = {'a': 10, 'b': 34, 'A': 7, "Z": 3}
change = {key:val for val,key in m.items()}
print(change)

# 集合推导式
# 集合推导式跟列表推导式也是类似的。 唯一的区别在于它使用大括号{ }。
# 基本格式：{ expr for value in collection if condition }
# 举例说明
set = {i for i in [1,2,1,2,33,33,4,4]}
print(set)    # 集合中无重复数据

squared = {x**2 for x in range(3)}
print(squared)

# 创建字符串长度的集合
m = ['a','if','us','yolooo','doudou']
set = {len(s) for s in m}
print(set)

# 一个由男人和女热组成的列表，取出姓名中带有两个以上字母的名字，组成列表
lt = [['jeeff','leeff','e'],['deeff','fee','ae']]
lts = []
#用for循环实现
for lst in lt:
    for name in lst:
        if name.count('e') >=2:
            lts.append(name)
print(lts)

# 用列表推导式实现
tem = [name for lst in lt for name in lst if name.count('e') >=2]
print(tem)

# 生成器推导式 用（）
# 举例说明
e = (i for i in range(10))
for each in e:
    print(each)

# 生成器推导式可作为函数参数
# 举例说明
print(sum(i for i in range(10) if i % 2 ))

# __call__ 方法
# 函数是对象，可以被调用（任何通过函数操作符（）来调用的对象）
def foo(x):
    return x
a = foo(3)
print(a)
print(callable(foo))   # 结果为True，表明foo（）是可以被调用的
print(callable(a))     # 结果为False，表明a是不可以被调用的

# 类，python为类提供了名为__call__ 方法，允许程序员创建可调用的实例对象。
# 默认情况下，__call__ 方法是没有实现的，意味着大多数情况下实例是不可被调用的
class Test():
    def method(self):
        return 1
a = Test()
print(callable(a))    # False

class Test():
    def __call__(self, *args, **kwargs):
        return 1
a = Test()
print(callable(a))   # True
print(a())           # 打印1

d = {'a':1,'v':2}
for key in d:
    print(d[key])

lt = [1,5,5,6]
for each in lt:
    print(each)