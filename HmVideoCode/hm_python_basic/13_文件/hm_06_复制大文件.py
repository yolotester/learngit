# 打开
file_read = open("README")
file_write = open("README[复件]", "w")

# 读，写
while True:
    text = file_read.readline()

    # 判断是否读取到内容
    if not text:
        break

    # 把每一行读取到的内容，写入到文件中
    file_write.write(text)

# 关闭
file_read.close()
file_write.close()