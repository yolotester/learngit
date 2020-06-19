# coding= utf-8

import logging

logger = logging.getLogger('fatherModule')
# 定义了logger'fatherModule'，并进行配置，定义该logger的子logger，都可以共享父logger的定义和配置
# 所谓的父子logger是通过命名来识别，任意以'fatherModule'开头的logger都是它的子logger

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


logger.info('creating an object of sonmodule.SonModuleClass')
a = sonmodule.SonModuleClass()
logger.info('calling sonmodule.SonModuleClass')
a.doSomething()
logger.info('done with sonmodule.SonModuleClass.doSomething')
logger.info('calling sonmodule.some_function')

