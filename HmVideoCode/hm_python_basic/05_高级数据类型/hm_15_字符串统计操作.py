str = "hello python"

# 1、统计字符串长度
print(len(str))

# 2、统计 子字符串 在 字符串中出现的次数
print(str.count("o"))
print(str.count("ooo"))  # 子字符串在字符串中不存在，返回0

# 3、某一个 子字符串 第一次出现的 索引
print(str.index("o"))
print(str.index("ooo"))  # 注意：子字符串在字符串中不存在，报错！ValueError: substring not found