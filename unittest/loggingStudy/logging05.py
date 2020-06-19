# coding=utf-8
'''
Created on 2020/6/29
@author:Yolo
Project:学习和使用logging模块--捕获traceback，意思是：跟踪异常返回信息，在日志文件中记录
'''

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

# 故意写个异常
try:
    open('yolo.txt', 'rb')

except (SystemExit, KeyboardInterrupt):
    raise

except Exception:
    # logger.error('Faild to open yolo.txt from logger.error', exc_info =True)
    # 或者用下面这种写法,与上面写法等价
    logger.exception('Faild to open yolo.txt from logger.exception')
