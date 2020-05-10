# 模块是一个包含你所定义的函数和变量的文件，后缀名为.py。模块可以被别的程序引入，以使用该模块的函数等功能
# OS  模块
import os
import time

print(os.getcwd())  # 返回当前工作目录

# os.chdir('E:\\')   改变当前工作目录

print(os.listdir('D:\\'))  # 列举指定目录中的文件夹

# os.makedirs('D:\\A\\B')   # 创建多层目录,目录已存在会报错

# os.mkdir('D:\\C')  # 创建单层目录

# os.remove('D:\\A\\B\\test.txt')    # 删除文件A
#
# os.rmdir('D:\\A\\B')    # 删除单层目录,若目录中不为空则报错
#
# os.removedirs('D:\\A\\B')   # 递归删除目录,从子目录到父目录逐层删除,遇到非空目录抛出异常

# os.rename('D:\\yolo','D:\\yolo1')   #重命名

# os.system('calc')   #调用系统命令

print(os.curdir)      #os.curdir 为常量  表示当前目录    os.paidir  为常量表示上级目录
print(os.pardir)

print(os.listdir(os.curdir))

# os.sep    输出操作系统特定的路径分割符   windows下是\\    linux 下是/

print(os.name)   # 指定当前使用的操作系统


# os.path mudule
print(os.path.basename('D:\\C\\B\\A\\dou.txt'))   # 去掉目录路径，返回文件名
print(os.path.dirname('D:\\C\\B\\A\\dou.txt'))     # 去掉文件名 ,返回路径

print(os.path.join('C','B','A'))   # 将各参数组合成路径名
# os.path.join('C:\\', 'C', 'B', 'A')   未能显示双反斜杠

# split(path)  分割文件名和路径，返回（f_path,f_name）元组。若完全使用目录，会将最后一个目录作为文件名分割
print(os.path.split('D:/C/yolo.txt'))
print(os.path.split('D:/A/B/C'))

# splittext(path)   分离文件名和扩展名，返回（f_name,f_extension）元组
print(os.path.splitext('D:/a/yolo.txt'))

# getsize(file)   返回文件的大小,单位是字节
print(os.path.getsize('yolo.txt'))

# getatime(file)  返回文件最近的访问时间  （浮点型秒数，可用time模块的gmtime（）或localtime（）换算）
# getmtime(file)  返回文件最近的修改时间
# getctime(file)  返回文件的创建时间

print(time.localtime(os.path.getatime('yolo.txt')))
print(time.gmtime(os.path.getctime('yolo.txt')))
print(os.path.getmtime('yolo.txt'))

# exists(path)   判断指定路径是否存在（文件或目录）
print(os.path.exists('D:/Learnpython'))

# isabs(path)   判断指定路径是否为绝对路径
print(os.path.isabs('D:/Learnpython'))

# isdir（path）  判断指定路径存在且是一个目录
print(os.path.isdir('D:/Learnpython/yolo.txt'))

# isfile（path）  判断指定路径存在且是一个文件
print(os.path.isfile('D:/Learnpython/yolo.txt'))

# islink（path）  判断指定路径存在且是一个链接
print(os.path.islink('D:/Learnpython/yolo.txt'))

# ismount（path）  判断指定路径存在且是一个挂载点
print(os.path.ismount('D:/Learnpython/yolo.txt'))
print(os.path.ismount('D:/'))

# samefile（path1，path2）  判断path1和path2两个路径是否指向同一个文件
print(os.path.samefile('D:/Learnpython/yolo.txt','D:/yolo.txt'))