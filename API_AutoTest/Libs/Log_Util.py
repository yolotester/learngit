#! usr/bin/env python
# -*- coding: utf-8 -*-


# @Time    : 2020/10/27 1:37
# @Author  : Yolo
# @Desc    : 日志库
# @File    : Log_Util.py
# @Software: PyCharm


import logging
import threading
import os
import time
from Config.Config import *
from logging.handlers import RotatingFileHandler


class LogSingleton(object):

    def __new__(cls, log_config):
        '''
        实现单例模式，必须重写该内置方法
        :param log_config: 用于接收Config中的var_config.ini
        :return: 对象的引用
        '''
        mutex = threading.Lock()
        mutex.acquire()  # 上锁，防止多线程下出问题
        if not hasattr(cls, 'instance'):

            # cls.instance 可以 理解为 类的引用
            cls.instance = super(LogSingleton, cls).__new__(cls)

            # 实例化对象 -- 用于操作配置文件log_config.ini
            config = configparser.ConfigParser()
            config.read(log_config, encoding='utf-8')

            # 如果不存在日志文件的目录，则创建
            if not os.path.exists(Config().log_path):
                os.mkdir(Config().log_path)

            # 为类创建属性 -- 得到配置文件中log_config.ini 各项的值
            cls.instance.log_filename = os.path.join(Config().log_path, time.strftime('%Y-%m-%d %H:%M:%S' + '.log', time.localtime()))
            cls.instance.max_bytes_each = int(config.get('LOGGING', 'max_bytes_each'))
            cls.instance.backup_count = int(config.get('LOGGING', 'backup_count'))
            cls.instance.fmt = config.get('LOGGING', 'fmt')
            cls.instance.logger_name = config.get('LOGGING', 'logger_name')  # 存储的模块名
            cls.instance.log_level = int(config.get('LOGGING', 'log_level'))
            cls.instance.console_log_on = int(config.get('LOGGING', 'console_log_on'))
            cls.instance.logfile_log_on = int(config.get('LOGGING', 'logfile_log_on'))

            # 日志基本步骤之一 ： 获得logger对象
            cls.instance.logger = logging.getLogger(cls.instance.logger_name)
            cls.instance.__config_logger()
        mutex.release()
        return cls.instance


    # 日志基本步骤之二 ： 设置日志级别
    def get_logger(self):
        '''用于获取配置文件中日志信息级别'''
        self.logger.setLevel(self.log_level)
        return self.logger


    # 日志基本步骤之三 ： 设置日志格式
    def __config_logger(self):
        '''设置日志格式'''
        fmt = self.fmt.replace('|', '%')
        formatter = logging.Formatter(fmt)

        if self.console_log_on == 1:  # 如果开启控制台日志
            # 日志基本步骤之四 ：获得相应的handler对象
            console = logging.StreamHandler()
            console.setFormatter(formatter)
            # 日志基本步骤之四 ：logger对象 添加 相应的handler对象
            self.logger.addHandler(console)

        if self.logfile_log_on == 1:  # 如果开启文件日志
            rt_file_handler = RotatingFileHandler(self.log_filename, maxBytes=self.max_bytes_each, backupCount=self.backup_count)
            rt_file_handler.setFormatter(formatter)
            self.logger.addHandler(rt_file_handler)


c = LogSingleton(Config().log_config_path)
logger = c.get_logger()
logger.info('log...')