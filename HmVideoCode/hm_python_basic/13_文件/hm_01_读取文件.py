# 打开文件(文件名区分大小写)
file = open("README", encoding="utf-8")

# 读取文件(并返回文件中的所有内容)
text = file.read()
print(text)

# 关闭文件
file.close()