import logging
from study_配置文件.config import *
import time
from logging.handlers import RotatingFileHandler

class MyLog(object):

    # 相对路径
    log_file_path = Config().log_path + '\\'
    times = time.strftime("%Y-%m-%d" + ".log")
    log_file_name = log_file_path + times

    def set_log(self):
        '''简单日志配置'''

        logging.basicConfig(level=logging.INFO,
                            filename= MyLog().log_file_name,
                            datefmt='%Y/%m/%d %H:%M:%S',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s')

        # 获得logger对象 -- __name__代表本模块，里面存储的是__main__字符串
        logger = logging.getLogger(__name__)

        logger.info('start log')
        logger.info('logging...')
        logger.info('finish log')


    def set_log_to_file(self):
        '''输出日志到文件'''

        # 获得logger对象
        logger = logging.getLogger(__name__)

        # 设置logger对象输出信息级别
        logger.setLevel(logging.INFO)

        # 获得日志输出到文件对象并配置
        file_handler = logging.FileHandler(MyLog().log_file_name)
        formatter = logging.Formatter(fmt='%(levelname)-8s %(asctime)s %(filename)-20s line:[%(lineno)d:] %(message)s')
        file_handler.setFormatter(formatter)

        # 必须添加到logger对象中, 可以添加0到多个handler对象到logger中
        logger.addHandler(file_handler)

        logger.info('This is a log info')
        logger.debug('Dubugging')
        logger.warning('Warning exixts')
        logger.info('Finish')


    def set_log_to_console(self):
        '''输出日志到控制台'''
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)  # logger对象的日志级别

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # 该handler对象的日志级别. 优先级大于logger对象
        formatter = logging.Formatter(fmt='%(levelname)-8s %(asctime)s %(filename)-20s Line:[%(lineno)d:] %(message)s')
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

        logger.info('This is a log info')
        logger.debug('Dubugging')
        logger.warning('Warning exixts')
        logger.info('Finish')

        return console_handler


    def log_rotate(self):
        '''
        日志回滚规范
        日志回滚，意思是：log会写在一个定义好大小的文件中，若日志太多会自动备份log.1, log.2, log.3 ......文件
        '''

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # 获得一个RotatingFileHandler对象，最多备份3个文件，每个文件最大值1K
        log_rotate_handler = RotatingFileHandler(MyLog().log_file_name, maxBytes=1*1024, backupCount=3)
        log_rotate_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(fmt='%(levelname)-8s %(asctime)s %(filename)-20s Line[%(lineno)d:] %(message)s')
        log_rotate_handler.setFormatter(formatter)

        logger.addHandler(log_rotate_handler)

        # 循环构造日志数据 -- 构造日志回滚
        for value in range(10):
            logger.info('This is a log info')
            logger.debug('Dubugging')
            logger.warning('Warning exixts')
            logger.info('Finish')


    def traceback(self):
        '''捕获完整的traceback信息'''

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(fmt='%(levelname)-8s %(asctime)s %(filename)-20s Line:[%(lineno)d:] %(message)s')

        # 在日志文件中查看完整的traceback信息
        file_handler = logging.FileHandler(MyLog().log_file_name)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # 在控制台查看完整的traceback信息
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # Log
        logger.info('Start')
        logger.error('Something may be fail.')

        # 在可能出错的代码上面加日志
        try:
            result = 10 / 0
        except Exception:
            # logger.error('fail to get result', exc_info=True)  # 只需加一个exc_info=True参数
            logger.exception('fail to get result...')
        logger.info('Finished')




if __name__=='__main__':
    MyLog().traceback()