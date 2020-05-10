# -*- coding: gbk -*-

# AssertionError  断言失败
passion = ['yolo']
assert len(passion) >0
# assert len(passion)>2

# AttributeError  尝试访问未知的对象属性
# passion.fishc()   AttributeError: 'list' object has no attribute 'fishc'

# Index Error  索引超过范围
# passion[3] = 1        IndexError: list assignment index out of range

# KeyError   查找字典中不存在的键
impotence ={'yolo':'doudou','doudou':'yolo'}
# print(impotence['yolO'])     KeyError: 'yolO'
# 可以这样处理，找不到键的异常
print(impotence.get('Yolo'))   # 返回None，但不会报错

# NameError   尝试访问不存在的变量
#print(a)             NameError: name 'a' is not defined

# OSError  操作系统产生的异常(这是一个总称)
# creativity = input('请输入一个文件名：')
# f = open(creativity)
# for each_line in f:
#     print(each_line)
#  FileNotFoundError: [Errno 2] No such file or directory: 'readme'

# SyntaxError   python语法错误
# print 'yolo'    SyntaxError: Missing parentheses in call to 'print'. Did you mean print('yolo')?

# TypeError  不同类型间的无效操作
# print(1 + '1')     TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ZeroDivisionError   除数为零
# print(5/0)    ZeroDivisionError: division by zero


# 异常检测  try-except语句和try...finally语句,可以接多个except语句/出现异常后的语句不会被执行
# try:
#     检测范围
# except Exception[as reason]:
#     出现异常（exception）后的处理代码
# finally:
#     无论如何都会被执行的代码

# 初级
# try:
#      investment= open('yolo.txt')
#     print(investment.read())
#     investment.close()
# except OSError:
#     print('文件出错啦......')

# try:
#
#     # int('adc')   ValueError: invalid literal for int() with base 10: 'adc'
#     sum = 1 + '1'
#     investment = open('yolo.txt')
#     print(investment.read())
#     investment.close()
# # except OSError as reason:
# #     print('文件出错啦......\n错误的原因是：' + str(reason))
# # except TypeError as cause:
# #     print('类型出错啦......\n错误的原因是：' + str(cause))
# except (OSError,TypeError):
#     print('出错啦////')

try:
    bartender = open('yolo.txt','w')
    print(bartender.write('YYYYYOOOOOLLLLLOOOOO'))
    sum = 1 + '1'
    bartender.close()
except (OSError,TypeError):
    print('出错啦////')
finally:
    bartender.close()

# raise语句，引发异常
raise ZeroDivisionError