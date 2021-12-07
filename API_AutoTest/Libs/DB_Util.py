#! usr/bin/env python
# -*- coding: utf-8 -*-


# @Time   : 2020/10/27 0:42
# @Author : Yolo
# @Desc   : 数据库（Mysql、sqlServer）和缓存（redis）操作库
# @File   : 
# @Software:
import pymysql
import pymssql  # 操作SqlServer库
import decimal
import datetime
from Libs.Log_Util import logger
from Config.Config import *
from DBUtils.PooledDB import PooledDB
class DBUtil(object):
    def __init__(self, db_alias='MSSQL'):
        self.config = configparser.ConfigParser()
        self.config.read(Config().db_config_path, encoding='utf-8')  # 读取db_config.ini配置文件
        # 获取每一个配置的值，以便后续使用
        self.DB_HOST = self.config.get('%s' % db_alias, 'DBHOST')
        self.DB_PORT = self.config.get('%s' % db_alias, 'DBPORT')
        self.DB_USER = self.config.get('%s' % db_alias, 'DBUSER')
        self.DB_PASSWORD = self.config.get('%s' % db_alias, 'DBPASSWORD')
        self.DB_SCHEMA = self.config.get('%s' % db_alias, 'DBSCHEMA')

        try:
            if db_alias.startswith('MSSQL'):  # SqlServer 不需要port参数，不清楚原因
                self.db_pool = PooledDB(creator=pymssql, mincached=2, maxcached=40, host=self.DB_HOST, user=self.DB_USER, password=self.DB_PASSWORD,
                         database=self.DB_SCHEMA, charset='utf8')  # 实例化池对象

            elif db_alias.startswith('MYSQL'):
                self.db_pool = PooledDB(creator=pymssql, mincached=2, maxcached=40, host=self.DB_HOST, user=self.DB_USER, password=self.DB_PASSWORD,
                         database=self.DB_SCHEMA, charset='utf8', port=self.DB_PORT)
            else:
                raise ValueError('不支持的数据库类型：{}'.format(db_alias))
        except Exception as err:
            logger.error('错误，数据库连接失败！原因：{}'.format(err))

    def query(self, sql_):
        """
        数据库查询操作：
        1、连接数据库,返回数据库对象
        2、创建游标
        3、执行sql语句
        4、获取查询结果
        5、关闭游标
        6、关闭数据库连接
        :param sql_:
        :return:
        """
        conn = self.db_pool.connection()
        cur = conn.cursor()
        cur.execute(sql_)  # 调用方法
        rows = cur.fetchall()
        cur.close()
        conn.close()

        return rows

    def execute(self, sql_):
        try:
            conn = self.db_pool.connection()
            cur = conn.cursor()
            count = cur.execute(sql_)
            conn.commit()  # 提交后执行语句才生效
            cur.close()
            conn.close()

        except Exception as err:
            logger.error('数据库操作出错！可能是当前用户没有数据库修改权限...请检查：{}'.format(err))

    @staticmethod  # 类名.静态方法 调用
    def sql_result_to_json(sql_result, fill_field_list, decimal_type_convert_to=1):
        """
        数据库查询结果转json
        :param sql_result: 数据库查询结果
        :param fill_field_list: 填充的json字段列表 如：["SessionId", "IsAgent"]
        :param decimal_type_convert_to: decimal类型的字段转换后的类型 （默认1：转成float类型 2：int类型）
        :return: 字典数据放在列表里面
        """
        result_json_list = []

        if isinstance(sql_result, list) and isinstance(fill_field_list, list):
            for result in sql_result:
                json_dic = {}
                if len(fill_field_list) != len(result):
                    raise ValueError('查询结果和填充参数不匹配，无法转化！')
                for i in range(len(result)):
                    fill_field_value = result[i]
                    # decimal.Decimal 没有参数默认返回Decimal('0') digit
                    if isinstance(result[i], decimal.Decimal) and decimal_type_convert_to == 1:
                        fill_field_value = float(result[i])
                    if isinstance(result[i], decimal.Decimal) and decimal_type_convert_to == 2:
                        fill_field_value = int(result[i])
                    if isinstance(result[i], datetime.datetime):  # 如果数据库查询返回的值为时间类型，则需要转化
                        fill_field_value = str(result[i])
                    json_dic.update({fill_field_list[i]:fill_field_value})
                result_json_list.append(json_dic)

        else:
            raise TypeError('查询结果和填充参数必须为列表类型！')
        return result_json_list


class RedisUtil:
    def __init__(self, redis_alias='', redis_port=''):
        """
        :param redis_alias: db_config配置文件中，若有多个redis服务器，则可以通过改参数默认值就可以确定使用哪个redis服务器
        :param redis_port: redis服务器端口
        """
        # 用实例属性的原因是，可能有多个redis服务器，要实例化不同的对象
        self.config = configparser.ConfigParser()
        self.config.read(Config().db_config_path, encoding='utf-8')
        self.DB_PORT = self.config.get('%s' % redis_alias, 'REDISPORT')
        self.DB_HOST = self.config.get('%s' % redis_alias, 'REDISHOST')
        self.config.read(Config().g_config_path, encoding='utf-8')

