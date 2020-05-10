 # 定义字符串
str = 'I love python'

 # 字符串切片
print(str[:6])

# 通过索引查询字符串中的字符
print(str[5])

# 修改字符串
str = str[:6] + ' beautiful' + str[6:]
print(str)

# 字符串方法总结
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

# endwith（sub,[,start[,end]]）  检查字符串是否以sub结尾，如果是返回True，否则返回False
print(str.endswith('n'))
print(str.endswith('o'))

# startswith（sub,[,start[,end]]）   检查字符串是否以sub开头，如果是返回True，否则返回False
print(str.startswith('I'))
print(str.startswith('i'))

# expandtabs(tabsize=8)   将字符串中的\t符号，转换为空格，默认空格数为8
str3 = 'I\tlove\tpython'
print(str3.expandtabs())
print(str3.expandtabs(15))

# find(sub,[,start[,end]])    检查sub是否包含在字符串中，如果有返回索引值，否则返回-1
print(str3.find('o'))
print(str3.find('m'))

# rfind(sub,[,start[,end]])   类似于find方法,只不过是从右边开始查找
print(str3.rfind('n'))

# index(sub,[,start[,end]])    与find方法类似，如果sub不在字符串中，返回一个异常
# print(str3.index('k'))

# rindex(sub,[,start[,end]])   与index方法类似,不过是从右边开始


# isalnum()   如果字符串中至少有一个字符并且所有字符都是字母或数字则返回True，否则返回False
str4 = 'yolo2020'
print(str4.isalnum())
str5 = 'yolo-2020'
print(str5.isalnum())

# isalpha()   如果字符串中至少有一个字符并且所有字符都是字母则返回True，否则返回False
str6 = 'yolo'
print(str6.isalpha())

# isdecimal()   如果字符串中只包含十进制数字则返回True，否则返回False
str7 = '0214529'
print(str7.isdecimal())

# isdigit()   如果字符串只包含数字则返回True，否则返回False


# isnumeric()   如果字符串中只包含数字字符则返回True，否则返回False

# islower()     如果字符串中至少包含一个能够区别大小写的字符,且都是小写,则返回True,否则返回False
str8 = 'jjkjlj'
str9 = 'kll0'
print(str8.islower())
print(str9.islower())

# isupper()   如果字符串中至少包含一个能够区别大小写的字符,且都是大写,则返回True,否则返回False
str11 = 'KKK000k'
print(str11.isupper())

# istitle()    如果字符串标题化,即所有单词以大写开始,其余字母均小写,则返回True ,否则返回False
str10 = 'Yolo Double fdd'
print(str10.istitle())

# join(sub)   以字符串作为分隔符,插入到sub中所以字符中间
print(str10.join('123456 '))

#isspace()   如果字符串只包含空格则返回True,否则返回False

# lstrip()  去掉字符串左边的所有空格
str11 = '      Sides'
print(str11.lstrip())

# rstrip()   删除字符串末尾的空格
str13 = '    Dessert         '
print(str13.rstrip())

# strip([chars])   删除字符串前边和后边所有的空格,chars参数可以定制删除的字符
print(str13.strip() )
str15 = str13.strip()
print(str15.strip('t'))

#partition(sub)  找到字符串sub,把字符串分成3元组(pre_sub,sub,fol_sub),如果字符串中不包含sub,则返回('原字符串','','')
print(str11.partition('d'))
print(str11.partition('m'))

# rpartition(sub)   类似于partition()方法,不过是从右边开始查找


# replace(old,new[,count])   把字符串中old字符串替换成new字符串,如果指定count,则替换不超过count次
str12 = 'aaaaaaassssssssaaaaaaa'
print(str12.replace('a','b',3))

# split(sep=None,maxsplit)   不带参数默认是以空格为分隔符切片字符串,返回切片后的子字符串拼接的列表
print(str.split())
print(str.split('i'))

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