import string
from Libs.Log_Util import logger

num = 125.26
logger.info(type(num))
count = 1
'''
partition() 方法用来根据指定的分隔符将字符串进行分割。
如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。
'''
a, b, c = str(num).partition('.')
c = c[:count]
logger.info('%s  %s  %s' % (a, b, c))

'''
join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
str.join(元组、列表、字典、字符串) 之后生成的只能是字符串。
所以很多地方很多时候生成了元组、列表、字典后，可以用 join() 来转化为字符串。
'''
logger.info('.'.join([a, c]))

'''
https://www.runoob.com/python/att-string-split.html
split(str='', num=string.count(str)) 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
'''
str1 = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print(str1.split('\n'))  # 以空格为分隔符，包含 \n
print(str1.split(' ', 1))  # 以空格为分隔符，分隔成两个
