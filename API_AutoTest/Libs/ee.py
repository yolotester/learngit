#! usr/bin/env python
# -*- coding: utf-8 -*-


# @Time   : 2020/10/27 0:42
# @Author : Yolo
# @Desc   : 配置类
# @File   : Config.py
# @Softwore: PyCharm

#!/usr/bin/env python
# -*- coding: utf-8 -*-


# @Time    : 2019/1/9 20:34
# @Author  : Kevin Tan
# @Desc    : 日志库
# @File    : Log_Util.py
# @Software: PyCharm


import logging
import threading
import time
from logging.handlers import RotatingFileHandler
from Config.Config import *


class LogSignleton(object):
    def __new__(cls, log_config):
        mutex = threading.Lock()
        mutex.acquire()  # 上锁，防止多线程下出问题
        if not hasattr(cls, 'instance'):
            cls.instance = super(LogSignleton, cls).__new__(cls)
            config = configparser.ConfigParser()
            config.read(log_config, encoding='utf-8')
            if not os.path.exists(Config().log_path):
                os.makedirs(Config().log_path)
            cls.instance.log_filename = os.path.join(Config().log_path, time.strftime('%Y-%m-%d %H-%M-%S'+'.log', time.localtime()))
            cls.instance.max_bytes_each = int(config.get('LOGGING', 'max_bytes_each'))
            cls.instance.backup_count = int(config.get('LOGGING', 'backup_count'))
            cls.instance.fmt = config.get('LOGGING', 'fmt')
            cls.instance.log_level = int(config.get('LOGGING', 'log_level'))
            cls.instance.logger_name = config.get('LOGGING', 'logger_name')
            cls.instance.console_log_on = int(config.get('LOGGING', 'console_log_on'))
            cls.instance.logfile_log_on = int(config.get('LOGGING', 'logfile_log_on'))
            cls.instance.logger = logging.getLogger(cls.instance.logger_name)
            cls.instance.__config_logger()
        mutex.release()
        return cls.instance

    def get_logger(self):
        self.logger.setLevel(self.log_level)
        return self.logger

    def __config_logger(self):
        # 设置日志格式
        fmt = self.fmt.replace('|', '%')
        formatter = logging.Formatter(fmt)

        if self.console_log_on == 1:  # 如果开启控制台日志
            console = logging.StreamHandler()
            console.setFormatter(formatter)
            self.logger.addHandler(console)

        if self.logfile_log_on == 1:  # 如果开启文件日志
            rt_file_handler = RotatingFileHandler(self.log_filename, maxBytes=self.max_bytes_each, backupCount=self.backup_count)
            rt_file_handler.setFormatter(formatter)
            self.logger.addHandler(rt_file_handler)


logsignleton = LogSignleton(Config().log_config_path)
logger = logsignleton.get_logger()
logger.info('log')