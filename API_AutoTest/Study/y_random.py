import random
from Libs.Log_Util import logger

list = ['1', '2', '3', '4', '5']
'''
random.sample(p, k)
从p序列中，随机获取k个元素，生成一个新序列。 sample不改变原来序列。
'''
str = random.sample(list, 3)
logger.info(str)

'''
random.choice(seq)序列中随机选取一个元素。seq需要是一个序列，比如list、元组、字符串
'''
str1 =random.choice(list)
logger.info(str1)
