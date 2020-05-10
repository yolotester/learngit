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

# while循环，重复性内容放在循环体，循环条件，初始化变量n控制循环次数
n = 0
while True:
    print(n, 'hello world')
    n = n + 1   # 循环一次后，需要修正循环次数，n自增1
    if n ==5:   # 判断条件，对n进行一个逻辑上的判断，n==5，则跳出循环
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


# 刷微博阅读次数
import os
from  selenium import webdriver
import time
import random
url = 'https://www.runoob.com/python3/python3-module.html'
count = random.randint(2,4)
j = 1
while j < count:
    i = 0
    while i < 2:
        wd = webdriver.Chrome()
        wd.get(url)
        i += 1
        time.sleep(2)

    else:
        # os.system('taskkill /F /IM chrome.exe')
        print(j,'close 浏览器')
    j +=1




