'''
练习1--定义一个整数变量age，编写代码判断年龄是否正确
    要求：人的年龄在0-120之间
'''
age = int(input("请输入你的年龄："))
if (age >= 0) and (age <= 120):
    print("你的年龄正确")
else:
    print("你的年龄不正确")

'''
练习2--定义两个整数变量python_score, c_score，编写代码判断成绩
    要求：只要有一门成绩 > 60分就算及格
'''
python_score = float(input("请输入你的python成绩："))
c_score = float(input("请输入你的c成绩："))
if python_score > 60 or c_score > 60:
    print("你的python成绩通过")
else:
    print("你的python 和 c 成绩都没有通过，继续努力！")


'''
练习3--定义一个bool 型变量is_employee， 判断是否是本公司员工
    要求：不是本公司员工，提示不能入内
'''
is_employee = True

# 场景1--在开发中，通常希望某个条件不满足时，执行一些代码，可以使用 not
# 场景2--如果需要拼接复杂的逻辑计算条件，也可能使用到not
if not is_employee:  # 结果 False，不执行下面语句
    print("你不是本公司员工，不能入内！")


