# coding=utf-8

import logging
import time
# 目的将日志写入到文件中

# 获得logger对象
logger = logging.getLogger(__name__)

# 配置logger对象
logger.setLevel(level=logging.INFO)

# 获得handle对象，配置输出到文件的level，时间格式

handler = logging.FileHandler('log1.txt')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
handler.setFormatter(formatter)

# logger对象通过addHandle（）方法添加0到多个handler
logger.addHandler(handler)

logger.info('Start study logging')
logger.debug('Something is fail')
logger.warning('Do something')
logger.info('Finish')