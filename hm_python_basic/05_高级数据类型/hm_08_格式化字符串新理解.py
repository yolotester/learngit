info_tuple = ("zhang", 18 ,1.72)

# 格式化字符串后面的 ‘()’ 本质上就是元组
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

# 使用 % 可以把字符串 和 元组 拼接起来
info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple
print(info_str)