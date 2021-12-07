import os

# 1、文件操作
# 重命名文件
os.rename("README", "readme")

# 删除文件
try:
    os.remove(r"D:\Git\learngit\hm_python_basic\13_文件\README[复件]")
except FileNotFoundError as e:
    print(e)


# 2、目录操作
# 创建目录
os.mkdir("test")

# 删除目录
#os.rmdir("test")

# 查看目录列表
dir = os.listdir()
print(dir)

# 判断是否是目录 是目录返回真，否则返回假
var = os.path.isdir("hm_01_读取文件")
print(var)

# 获取当前目录
cwd = os.getcwd()
print(cwd)

# 修改工作目录
os.chdir("test")
cwd = os.getcwd()
print(cwd)