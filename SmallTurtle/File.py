# open函数，参数
# r 读,若文件不存在,会报无此文件
# w 写，若文件不存在，则创建新文件
# b 二进制模式
# + 打开一个文件进行更新可读可写
# a 追加内容,若文件不存在,则创建新文件
# t 文本模式（默认）
# x 写模式，若文件已存在则会报错

# 文件系统与计算机结构有关:1.cpu:运行程序的地方  2.内存:存储数据的地方  3.磁盘: 永久存储数据的地方 4.i/o接口
# 程序在是cpu中执行的一段指令,返回回来的数据会放在RAM中,因为ram访问速度比较快,ram缺点断电后数据会丢失
# 磁盘可以永久保存文件,程序通过文件来访问磁盘,也可以通过文件写入磁盘

# 把ram里面的数据存放到磁盘中,或者从磁盘中读取数据到ram中,必要的三步骤
# 1.打开文件:以读方式/写方式打开
# 2.读写文件: read readline readlines   write  writelines
# 3,关闭文件.为什么要关闭文件,原因1,因为写入文件时是放到缓冲区,只有保存的时候才是真正的写入文件
# 原因2,每个文件都有一个文件id,打开多次会占用多个内存  原因3,第一次打开文件可读写,第二次打开相同文件只可读



f = open('D:\\yolo.txt',encoding='utf-8',errors='ignore')
print(f.read())

# 文件对象方法   f.read() 读取文件，
print(f.read(5))   # 读取文件中5个字节数
f.seek(0,0)
print(f.read(5))

# f.tell()   返回当前在文件中的位置
f.seek(0,0)
print(f.tell())

# f.seek(offset,from)   from:0代表文件起始位置，1代表当前位置，2代表末尾,偏移 offset 个字符
# f.seek(2,0)
# print(f.readline())

# f.readline([size]) 读取整行，会一直读到一个\n字符结尾,会打印出一行空行,可以用字符串rstrip方法移除,就不会显示该空行
f1 = f.readline()
f1 = f1.rstrip('\n')
print(f1)


#f.readlines([size]) 读取所有行并返回列表,有换行会在内容中显示\n符
print(f.readlines())


# 用list将文件转化为列表
print(list(f))
f.seek(0,0)
for each_line in f:
    print(each_line)   # 包含换行

# f.write  对文件进行写入,写入的是字符串,可在内容后面加上'\n',换行显示好看
f = open('D:\\test','w')
print(f.write('i love python' + '\n'))
print(f.write('i love doudou'))
f.close()

# f.writelines  只有一个参数,对文件进行写入,如果需要换行,需要写上\n符,写入的是序列(字典,元组,列表)
f = open('D:\\yl.txt','w')
seq = ['i love python \n','love doudou\n']
f.writelines(seq)
f.writelines(('yolo\n','doudou\n'))
f.close()

# 爬取http://httpbin.org/post这个网站上的内容,写入到doudou.txt中,字节流传输b
import  requests
url = 'http://httpbin.org/post'
req = requests.get(url)
contents = req.content
f = open('D:\\doudou','wb')
f.write(contents)
f.close()

# 格式化写入文件
fe = open('D:\\dd.txt','w')
head = '%10s%10s%10s\n'%('ID',"Name",'Record')
fe.write(head)
cont = '%10d%10s%10.2f\n' % (6522523,'Yolo',52.25235)
fe.write(cont)
fe.close()

# 循环体与文件  while和readline    for 和file_obj
fr = open('D:\\dd.txt','r')
line = fr.readline()       # readline读到文件尾部，返回一个‘’空字符串
while line !='':
    line = line.rstrip('\n')
    print(line)
    line = fr.readline()

fr.close()


