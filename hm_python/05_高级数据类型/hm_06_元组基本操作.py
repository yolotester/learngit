info_tuple = ("zhang", 22, 1.72)

# 1.取值和取索引
print (info_tuple[0])
# 知道数据内容，希望知道该数据在元祖中的索引
print (info_tuple.index("zhang"))

# 2.统计计数
print (info_tuple.count(22))
# 统计元祖中的元素个数
print (len(info_tuple))