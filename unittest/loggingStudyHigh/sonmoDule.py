# coding=utf-8
# 注释，包括记录创建时间，创建人，项目名称
'''
created on 2020/6/19
@author:YOlo
Project:学习logging模块--多模块使用logging
'''

import logging

module_logger = logging.getLogger('fatherModule.son')

class SonModuleClass(object):

    def __init__(self):
        self.logger = logging.getLogger('fatherModule.son.module')
        self.logger.info('creating an instance in SonModuleClass')

    def doSomething(self):
        self.logger.info('do something in sonmodule')
        a = []
        a.append(1)
        self.logger.debug('list a = ' + str(a))
        self.logger.info('finish something in SonModuleClass')

def son_function():
    module_logger.info('call function son_function')