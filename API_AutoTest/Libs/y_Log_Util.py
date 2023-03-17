import time
from Config.Config import *
import logging
from logging.handlers import RotatingFileHandler  # 日志回滚


class LogSingleton(object):
    """
    实现单例模式
    1、重写new方法.__new__方法作用：分配空间 和 返回对象的引用
    2、类属性接收返回的对象的引用
    """

    def __new__(cls, log_config):  # log_config作为参数接收实例化对象时log配置文件路径

        # hasattr(object, name) 判断对象是否包含对应的属性，有返回真
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)

            config = configparser.ConfigParser()  # 实例化对象操作log配置文件

            # 需要加上编码格式，不然报错UnicodeDecodeError: 'gbk' codec can't decode byte 0x8f in position 33: illegal multibyte
            # sequence
            config.read(log_config, encoding='utf-8')  # log配置文件位置 Config().log_config_path

            if not os.path.exists(Config().log_path):  # 如果不存在Logs目录，则创建该目录
                os.makedirs(Config().log_path)

            # 为对象设置属性--得到配置文件中log_config.ini 各项的值
            cls.instance.log_filename = os.path.join(Config().log_path,
                                                     time.strftime("%Y-%m-%d %H-%M-%S" + '.log', time.localtime()))
            cls.instance.max_bytes_each = int(config.get('LOGGING', 'max_bytes_each'))
            cls.instance.backup_count = int(config.get('LOGGING', 'backup_count'))
            cls.instance.fmt = config.get('LOGGING', 'fmt')
            cls.instance.log_level = int(config.get('LOGGING', 'log_level'))
            cls.instance.logger_name = config.get('LOGGING', 'logger_name')
            cls.instance.console_log_on = int(config.get('LOGGING', 'console_log_on'))
            cls.instance.logfile_log_on = int(config.get('LOGGING', 'logfile_log_on'))

            # 下面是日志基础步骤
            # 1.获得logger对象，getLogger(__name__) 代表的是此脚本文件
            cls.instance.logger = logging.getLogger(cls.instance.logger_name)

            # 2.调用方法。方法里设置formatter格式 和 输出日志的基本操作
            cls.instance.__config_logger()

        return cls.instance

    # def __init__(self, log_config):  # 初始化方法中，不能有参数，所以需要有参数时，用new方法
    #
    #     config = configparser.ConfigParser()  # 实例化对象操作log配置文件
    #     config.read(Config().log_config_path)
    #
    #     if not os.path.exists(Config().log_path):  # 如果不存在Logs目录，则创建该目录
    #         os.makedirs(Config().log_path)

    # 返回logger对象，用一个全局变量Logger接收，则需要使用日志模块，直接导入该全局变量即可
    # 3.设置日志级别
    def get_logger(self):
        self.logger.setLevel(self.log_level)
        return self.logger

    def __config_logger(self):

        # 设置formatter格式
        fmt = self.fmt.replace('|', '%')
        formatter = logging.Formatter(fmt)

        # 日志输出到控制台基本步骤
        # 1.获得handler
        # 2.调用setFormatter方法设置格式
        # 3. 添加handler
        if self.console_log_on == 1:  # 如果开启了控制台日志文件
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

        if self.logfile_log_on == 1:  # 如果开启文件日志
            # maxBytes  最大字节数   backupCount  备份文件个数
            rt_file_handler = RotatingFileHandler(self.log_filename, maxBytes=self.max_bytes_each,
                                                  backupCount=self.backup_count)
            rt_file_handler.setFormatter(formatter)
            self.logger.addHandler(rt_file_handler)


log_singleton = LogSingleton(Config().log_config_path)
print(log_singleton.logger_name)
logger = log_singleton.get_logger()
logger.info("log")
# 在其他模块导入该logger全局变量，输出日志的时候，文件名就是其他模块
