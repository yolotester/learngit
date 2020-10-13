name_list = ["zhang", "san", "lisi", "QQQ"]

# 使用迭代遍历列表
'''
迭代 -- 顺序地从列表中获取所有数据，每一次循环过程中，
数据都会保存在 my_name 这个变量中， 在循环体内部可以访问到当前这一次获取到的数据

for my_name in 列表变量:
    print("我的名字是: %s" % my_name)
'''


for my_name in name_list:
    print("我的名字是: %s" % my_name)