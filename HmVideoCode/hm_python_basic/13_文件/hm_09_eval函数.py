# *-* coding:utf8 *-*
# input_str = input("请输入一个算术题：")
# print(eval(input_str))

# eval函数将字符串 当成 有效的表达式 来求值 并 返回计算结果
var = eval("[1, 2, 3, 4, 5]")
print(var)

var = eval("{'name': 'xiaoming', 'age': 18}")
print(var)

var = eval("'*' * 10")
print(var)