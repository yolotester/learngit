# coding = utf-8
import logging

# 日志的基本配置
logging.basicConfig(level = logging.DEBUG, format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# 获得logger对象
logger = logging.getLogger(__name__)

logger.info('Start pring log')
logger.debug('Do debug')
logger.warning('Something may be fail')
logger.info('finish')

