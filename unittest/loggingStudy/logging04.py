# coding=utf-8
'''
Created on 2020/6/29
@author:Yolo
Project:学习和使用logging模块--日志回滚，意思是：log会写在一个定义好大小的文件中，若日志太多
会自动备份成log.txt.1, log,txt.2......
'''

import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)

logger.setLevel(level=logging.INFO)

# 获得一个RotatingFileHandler对象，最多备份3个文件，每个文件最大值1K
rhandler = RotatingFileHandler('log.txt', maxBytes=1*1024, backupCount=3)
rhandler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
rhandler.setFormatter(formatter)


consle = logging.StreamHandler()
consle.setLevel(logging.INFO)
consle.setFormatter(formatter)

# 必须要addhandler
logger.addHandler(rhandler)
logger.addHandler(consle)

for value in range(0,100):

    logger.info('Start study logging')
    logger.debug('Something is fail')
    logger.warning('Do something')
    logger.info('Finish')


