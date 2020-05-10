 # 字符串定义：有序的字符序列组合，是常量。用单/双/三重引号引起来的字符叫做字符串
str = 'I love python'

 # 字符串操作  + 连接  * 重复 str[i] 索引/index   s[i:j:step] 切片/slice  for循环遍历
 # 字符串切片
print(str[:6])

# 通过索引查询字符串中的字符
print(str[5])

# 连接字符串
str = str[:6] + ' beautiful' + str[6:]
print(str)

# 重复字符串
print(str*2)

# for循环遍历
for val in str:
    print(val)

# 切片，左闭右开
str99 = 'absc'
sub = str99*4     # 输出abscabscabscabsc
print(sub)
print(sub[-4:-1])  # 输出abs
print(sub[-4:])    # 输出absc
print(sub[1:4])    # bsc
print(sub[3:])      # cabscabscabsc
print(sub[1::2])    # bcbcbcbc
print(sub[-1:-4:-1])  # csb
print(sub[8:3:-1])    # acsba  逆序：步长为负数就好
print(sub[:])     # 输出abscabscabscabsc  复制一份
print(sub[-1::-1])  # 逆序显示





# 字符串方法总结
# len（）得出字符串长度
print(len(str99))
# int（s） ord（）将字符转化成ascii码值  chr（） 将ASCII值转化为字符
s3 = 'a123b'
a = int(s3[1:len(s3) -1])
print(a)
a =int(s3[1:-1])
print(a)


#字符串字母变为大小写的方法
# capitalize() 方法，把字符串首字符变为大写
str1 = 'dOuDou'
print(str1.capitalize())

# casefold()  方法，将字符串中所有字符都变为小写
print(str.casefold())

# lower()   转换字符串中所有大写字符为小写
print(str1.lower())

# upper()   转换字符串中所有小写为大写
print(str.upper())

# center(width)  方法，将字符串居中，左右两边以空格填充width的长度
print(str.center(40))

# ljust(width)  左对齐,使用空格填充至长度为width的新字符串
print(str.ljust(60))

# rjust(width)   右对齐,使用空格填充至长度为width的新字符串
print(str.rjust(60))

# count(sub,[,start[,end]])  方法，返回字符串中某字符出现的次数
print(str.count('o'))

# encode(encoding = 'utf-8',errors='strict')  以encoding指定的编码格式，对字符串进行编码






# 检查字符串开头或者结尾的字符串是否是sub，
# endwith（sub,[,start[,end]]）  检查字符串是否以sub结尾，如果是返回True，否则返回False
str100 = 'i lone python'  # 长度12
print(str100.endswith('n',1,6))  # false
print('333')
print(str100.endswith('o',1,12))  # true
s1 = '.com'
s = 'www.baidu.com'
print(s.endswith(s1))  # true
print('.com')

# startswith（sub,[,start[,end]]）   检查字符串是否以sub开头，如果是返回True，否则返回False
print(str100.startswith('I'))  # false
print(str100.startswith('i'))  # true



# 转换字符串中的\t符号的
# expandtabs(tabsize=8)   将字符串中的\t符号，转换为空格，默认空格数为8
str3 = 'I\tlove\tpython'
print(str3.expandtabs())
print(str3.expandtabs(15))




# find(sub,[,start[,end]])    检查sub是否包含在字符串中，如果有返回索引值，否则返回-1
print(str3.find('o',8,12))   # 返回最后一个o字母的索引值11
print(str3.find('m'))        # 返回-1
print(str3[4:4+len(sub)])    # ve	python

# rfind(sub,[,start[,end]])   类似于find方法,只不过是从右边开始查找
print(str3.rfind('n'))      # 返回最右边字母n的索引值12

# index(sub,[,start[,end]])    与find方法类似，如果sub不在字符串中，返回一个异常
# print(str3.index('k'))

# rindex(sub,[,start[,end]])   与index方法类似,不过是从右边开始




# 判断数字和字母的和空格的
# isalnum()   如果字符串中至少有一个字符  并且 所有字符都是字母或数字则返回True，否则返回False
str4 = 'yolo2020'
print(str4.isalnum())   # True
str5 = 'yolo-2020'
print(str5.isalnum())   # False
str66 = ''
print(str66.isalnum())  # fALSE

# isnumeric()   如果字符串中  只包含数字   则返回True，否则返回False
str6666 = '212'
print(str6666.isnumeric())  # true

# isalpha()   如果字符串中至少有一个字符  并且  所有字符都是字母则返回True，否则返回False
str6 = 'yolo'
print(str6.isalpha())   # true

# isdigit()   如果字符串只包含数字则返回True，否则返回False
str888 = '666'
print(str888.isdigit())     # true

#isspace()   如果字符串   只包含空格   则返回True,否则返回False
str555 = ''       # 空字符串
print(str555.isspace())  # false
print('222')
str666 = '  '   # 空格
print(str666.isspace())  # true




# isdecimal()   如果字符串中只包含十进制数字则返回True，否则返回False
str7 = '0214529'
print(str7.isdecimal())









# 判断是字母是大写还是小写还是标题
# islower()     如果字符串中至少包含一个能够区别大小写的字符,且都是小写  ,则返回True,否则返回False
str8 = 'jjkjlj'
str9 = 'kll0'
print(str8.islower())  # True
print('1111')
print(str9.islower())  # true

# isupper()   如果字符串中至少包含一个能够区别大小写的字符,且都是大写,则返回True,否则返回False
str11 = 'KKK000k'
print(str11.isupper())

# istitle()    如果字符串标题化,即所有单词以大写开始,其余字母均小写,则返回True ,否则返回False
str10 = 'Yolo Double fdd'
print(str10.istitle())






# join(sub)   以字符串作为分隔符,插入到sub中所以字符中间
print(str10.join('123456 '))




# 去除字符串左右两边空格的
# lstrip()  去掉字符串左边的所有空格
str11 = '      Sides'
space = str11.lstrip()
print(space)

# rstrip()   删除字符串末尾的空格
str13 = '    Dessert         '
print(str13.rstrip())

# strip([chars])   删除字符串前边和后边所有的空格,chars参数可以定制删除的字符
print(str13.strip() )
str15 = str13.strip()
print(str15.strip('t'))



# 将字符串用字符串分割的
#partition(sub)  找到字符串sub,把字符串分成3元组(pre_sub,sub,fol_sub),如果字符串中不包含sub,则返回('原字符串','','')
print(str11.partition('d'))
print(str11.partition('m'))

# rpartition(sub)   类似于partition()方法,不过是从右边开始查找





# 替换字符串的，其实是先拷贝旧的字符串，然后再替换后作为新的字符串
# replace(old,new[,count])   把字符串中old字符串替换成new字符串,如果指定count,则替换不超过count次
str12 = 'aaaaaaassssssssaaaaaaa'
print(str12.replace('a','b',3))
print(str12.replace('s','s'.upper()))  # aaaaaaaSSSSSSSSaaaaaaa
s = 'jeapedu'
s1 = s[:3] + s.replace('p','P') + s[4:]
print(s1)





# 分割字符串的这个更广泛
# split(sep=None,maxsplit)   不带参数默认是以空格为分隔符切片字符串,返回切片后的列表
str22 ='hello world my world'
print(str22.split())
print(str22.split('l'))

# splitlines([keepends])   按照'\n'分隔,返回包含各行作为元素的列表,如果keepends参数指定,则返回前keepends行
str14 = 'i \n love \n python'
print(str14.splitlines())




# swapcase()   翻转字符串中的大小写
print(str14.swapcase())

# title()    返回标题化的字符串
print(str14.title())

# translate(table)   根据table 的规则(可以由str.maketrans('a','b')定制)转换字符串中的字符   s,b数字的意思是asii编码
str18 = 'sssssssssaaaaaaasssssssss'
print(str18.translate(str.maketrans('s','b')))
print(str.maketrans('s','b'))

# zfill(width)   返回长度为width的字符串,原字符串右对齐,前边用0填充
print(str18.zfill(100))



# 字符串应用
s = '  12s   4546ff   dffg   '
# 1.strip 去除前后空格
#  2.找到第一个空格
#  3.找到第一个空格后面的第一个非空格字符
#  4.重复2-3步
print(s.split())
print(s.rstrip())
print(s.lstrip())
s = s.strip()
print('after strip s=',s)   # 第一步

a = s.find(' ')    # 第二步
w1 = s[0:a]
print(w1)    # 12s

while s[a] == ' ':
    a +=1
print('not space str a:',a,s[a])

