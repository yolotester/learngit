#! usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
# @Time   : 2020/10/27 0:42
# @Author : Yolo
# @Desc   : 配置类
# @File   : Config.py
# @Software: PyCharm
import sys
sys.path.append('/Users/zz/Git/API_AutoTest')


import logging
import os
import sys
import threading
import time
from logging.handlers import RotatingFileHandler
from Config.Config import * # 导入Config模块，第一个Config是目录名


class LogSingleton(object):
    def __new__(cls, log_config):
        '''
        1、静态方法，需要主动传参cls
        2、实现单例模式，必须要重写该方法
        :param log_config: 用于接收Config中log_config.ini文件
        :return: 对象的引用（单例模式下，引用相同）
        '''

        mutex = threading.Lock()
        mutex.acquire()  # 上锁，防止多线程下出问题

        if not hasattr(cls, 'instance'):

            # 类属性cls.instance表示对象的引用
            cls.instance = super().__new__(cls)

            # 实例化对象 -- 用于操作配置文件log_config.ini
            config = configparser.ConfigParser()
            config.read(log_config, encoding='utf-8')

            # 如果不存在日志文件的目录，则创建
            if not os.path.exists(Config().log_path):
                os.makedirs(Config().log_path)

            # 为对象创建属性 -- 得到配置文件中log_config.ini 各项的值
            cls.instance.log_filename = os.path.join(Config().log_path, time.strftime('%Y-%m-%d %H-%M-%S'+'.log', time.localtime()))  # 2020-10-27 13-49-11.log
            cls.instance.max_bytes_each = int(config.get('LOGGING', 'max_bytes_each'))
            cls.instance.backup_count = int(config.get('LOGGING', 'backup_count'))
            cls.instance.fmt = config.get('LOGGING', 'fmt')
            cls.instance.log_level = int(config.get('LOGGING', 'log_level'))
            cls.instance.logger_name = config.get('LOGGING', 'logger_name')
            cls.instance.console_log_on = int(config.get('LOGGING', 'console_log_on'))
            cls.instance.logfile_log_on = int(config.get('LOGGING', 'logfile_log_on'))

            # 日志步骤之一：获得logger对象
            cls.instance.logger = logging.getLogger(cls.instance.logger_name)
            cls.instance.__config_logger()  # 判断是否开启了控制台、文件日志

        mutex.release()

        return cls.instance

    # 日志步骤之二：设置日志级别
    def get_logger(self):
        '''用于获取配置文件中日志信息级别,通过更改log配置文件，就可以实现要输出哪个级别的信息'''
        self.logger.setLevel(self.log_level)
        return self.logger

    # 日志步骤之三 ： 设置日志格式
    def __config_logger(self):
        # 设置日志格式
        fmt = self.fmt.replace('|', '%')
        formatter = logging.Formatter(fmt)

        if self.console_log_on == 1:  # 如果开启控制台日志

            # 日志步骤之四 ：获得相应的handler对象
            console = logging.StreamHandler()
            console.setFormatter(formatter)

            # 日志步骤之五 ：logger对象 添加 相应的handler对象
            self.logger.addHandler(console)

        if self.logfile_log_on == 1:  # 如果开启文件日志
            rt_file_handler = RotatingFileHandler(self.log_filename, maxBytes=self.max_bytes_each, backupCount=self.backup_count)
            rt_file_handler.setFormatter(formatter)
            self.logger.addHandler(rt_file_handler)


logsingleton = LogSingleton(Config().log_config_path)
logger = logsingleton.get_logger()  # 如果其他文件需要日志，可直接from Libs.Log_Util import logger

if __name__ == '__main__':
    print(sys.path)
    logger.info('log')