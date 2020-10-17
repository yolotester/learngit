hello_str = "hello Python"

# 1、判断是否以指定字符串开始
print(hello_str.startswith("hello"))

# 2、判断是否以指定字符串结束
print(hello_str.endswith("on"))

# 3、查找指定字符串
# index方法 同样可以查找  指定的字符串  在字符串中的索引
print(hello_str.find("llo"))

# index如果查找的指定字符串不存在，则报错！！！
# find如果查找的指定字符串不存在，则返回 -1
print(hello_str.find("abc"))

# 4、替换字符串
# replace方法执行完成之后，会返回一个新的字符串
# 注意：不会修改原有的字符串
new_hello_str = hello_str.replace("Python", "world")
print(new_hello_str)
print(hello_str)