# 打开文件(文件名区分大小写)
file = open("README", encoding="utf-8")

# 读取文件(并返回文件中的所有内容)
# 当执行了 read 方法后，文件指针 会移动到 读取内容的末尾
text = file.read()
print(text)
print(len(text))

print("-" * 50)

# 所以再次调用read方法，则不会有任何内容显示
text = file.read()
print(text)
print(len(text))

# 关闭文件
file.close()