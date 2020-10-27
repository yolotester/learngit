# 下面这行代码的意思是 -- 解释器会以 utf-8 编码来处理 python 文件
# *-* coding:utf8 *-*

# 字符串前面的u表示 -- 告诉解释器这是一个utf8编码格式的字符串
hello_str = u"hello世界"
print(hello_str)

for i in hello_str:
    print(i)
