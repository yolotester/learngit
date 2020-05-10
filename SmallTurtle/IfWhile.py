# 单分支 if
# 双分支 if else
# 多分支 if elif else
# if 条件构造: 1.布尔表达式,0为假,非0为真  2.关系表达式 >,<,>=,!=  3.逻辑表达式 not and or
if 0:
    print('false0')
else:
    print('true')

if 'yolo':
    print('true')
'''
grade = int(input('请输入你的成绩...:'))
if grade > 60:
    print('你真棒!')
else:
    print('继续加油哦!')

sex = input('请输入你的性别...:')
if sex == 'man' or sex =='m' or sex == 'M':
    print('Man')
else:
    print('Women')
'''

# while循环
n = 0
while True:
    print(n, 'hello world')
    n = n + 1
    if n ==5:
        break
print('out while')

n = 1
s = 0
while n<=100:
    print(s,n)
    s += n
    n += 1
else:
    print('s:', s )

