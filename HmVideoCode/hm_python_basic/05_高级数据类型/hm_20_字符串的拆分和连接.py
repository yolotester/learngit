'''
要求：
1、将字符串中的空白字符全部去掉
2、再使用 " " 作为分隔符，拼接为一个整齐的字符串
'''

poem_str = "百日依山尽\t\n 黄河入海流 \n 欲穷千里目\t 更上一层楼"
print(poem_str)

# 字符串的拆分
# split方法以 空白字符 作为分隔符拆分字符串
poem_list = poem_str.split()
print(poem_list)


# 字符串的连接
# " " 作为分隔符，连接字符串
result = " ".join(poem_list)
print(result)