# 打开
# w  -- 会覆盖原有文件内容。文件若不存在，则创建
# a  -- 在文件末尾追加内容。文件若不存在，则创建
file = open("README", "w")

# 写入
file.write("hello")

# 关闭
file.close()