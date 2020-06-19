# coding=utf-8

import logging

logger = logging.getLogger(__name__)

logger.setLevel(level=logging.INFO)

# 获得输出到文件的handler对象
handler = logging.FileHandler('log1.txt')

handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

handler.setFormatter(formatter)


# 将日志同时输出在屏幕和日志文件中
# 获得输出到屏幕的handler对象
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

#　添加handler对象
logger.addHandler(handler)
logger.addHandler(console)

logger.info('Start study logging')
logger.debug('Something is fail')
logger.warning('Do something')
logger.info('Finish')

