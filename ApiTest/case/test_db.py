'''
    目标：在unittest中使用读取数据库封装类
'''
# 导包 unittest read_database
import unittest
from tools.read_database import ReadDB
import logging

logging.basicConfig(level=logging.INFO, format= '%(asctime)s-%(levelname)s-%(name)s-%(message)s')

logger = logging.getLogger(__name__)


# 创建测试类，继承unittese.TestCase
class TestDB(object):

    # 新建测试方法
    def test_db(self):

        # 要执行的sql语句
        sql = 'select * from goods'

        # 调用数据库封装类的主要方法并接收数据
        data = ReadDB().get_sql_one(sql)

        # 对结果进行断言
        self.assertEqual(1, data[0])




if __name__ == '__main__':
    unittest.main()





