name_list = ["zhang", "san", "lisi", "QQQ"]

# len(length 长度)函数可以统计列表中元素的总数
list_len = len(name_list)
print("列表中包含 %d 个元素" % list_len)


# count方法可以统计列表中 某一个数据出现的次数
count = name_list.count("san")
print("san 出现了 %d 次" % count)


# remove方法从列表中删除  第一次出现  的数据，如果数据不存在， 程序会报错！！！
name_list.remove("san")
print(name_list)