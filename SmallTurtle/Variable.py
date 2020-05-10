
# 变量是指向内存地址（可变），而不是数据内容（不变）  id可查看内存地址，不可通过变量名修改其指定空间的内容

x = 12  # 内存中开辟两个空间，一个存放整型12，一个存放整型13，x只不过是指向不同的内存空间，而不是把12修改为13
x = 13
# 变量赋值什么类型，则此变量是什么类型   type可查看类型
import math
import os
import socket
val = math.sin(1 / 2)
print(val)
val = math.pow(3,4)
print(val)

currentdir = os.getcwd()
print(currentdir)
dirs = os.listdir(currentdir)
print(dirs)

baiduip = socket.gethostbyname('www.baidu.com')
print(baiduip)

#  使用规则： 从上往下顺序创建，从下往上搜索，即搜索遵循LEGB原则，如果一直搜索不到则报错。
# builtin
# global
# enclosed
# local
# 只有类,模块.方法才会产生作用域
# 变量的作用域   final_price是局部变量,函数外的变量为全局变量,不要在函数内部修改全局变量的值,不能在函数外部访问/修改局部变量的值
# 在函数内部可以访问全局变量
# .如果修改全局变量，python会自动创建一个名字一样的局部变量代替

def discount(price , count):
    final_price = price * count
    print('这里试图访问全局变量old_price', old_price)
    return final_price


old_price = float(input('请输入原价格;'))
rate = float(input('请输入打几折：'))
new_price = discount(old_price,rate)
print('打折后的价格：',new_price)
# print('试图打印出局部变量',final_price)     NameError: name 'final_price' is not defined

# global关键字 ，把局部变量变为全局变量
# 无声明的情况下，赋值即私有，若外部有相同名称的变量则被遮挡
# 想修改外部变量，需声明（global、nonlocal），或者通过可变对象的内置函数
number = 10
def CountNum():
    global number
    number = 20
    print(number)
CountNum()
print(number)

i = [10]
def lt():
    i.append(2)
lt()
print(i)
