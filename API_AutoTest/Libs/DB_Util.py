#!/usr/bin/env python
# -*- coding: utf-8 -*-


# @Time    :
# @Author  :
# @Desc    : 数据库(Mysql、SqlServer)和缓存(redis)操作库
# @File    : DB_Util.py
# @Software: PyCharm


import decimal
import datetime
import pymysql
import pymssql
from dbutils.pooled_db import PooledDB
# from redis import StrictRedisCluster
from redis.client import Redis, StrictRedis
from Libs.Log_Util import logger
from Config.Config import *


class DBUtil:
    def __init__(self, db_alias='MSSQL'):
        self.config = configparser.ConfigParser()
        self.config.read(Config().db_config_path, encoding='utf-8')
        self.DB_HOST = self.config.get('%s' % db_alias, 'DBHOST')
        self.DB_PORT = self.config.getint('%s' % db_alias, 'DBPORT')
        self.DB_USER = self.config.get('%s' % db_alias, 'DBUSER')
        self.DB_PASSWORD = self.config.get('%s' % db_alias, 'DBPASSWORD')
        self.DB_SCHEMA = self.config.get('%s' % db_alias, 'DBSCHEMA')

        try:
            if db_alias.startswith('MSSQL'):
                self.db_pool = PooledDB(creator=pymssql, mincached=2, maxcached=40, host=self.DB_HOST, user=self.DB_USER, password=self.DB_PASSWORD, database=self.DB_SCHEMA,
                                        charset="utf8")
                pass
            elif db_alias.startswith('MYSQL'):
                self.db_pool = PooledDB(creator=pymysql, mincached=2, maxcached=40, host=self.DB_HOST, port=self.DB_PORT, user=self.DB_USER, password=self.DB_PASSWORD, database=self.DB_SCHEMA,
                                       charset="utf8")
                pass
            else:
                raise ValueError('不支持的数据库类型： {}'.format(db_alias))
        except Exception as err:
            logger.error('错误，数据库连接失败！原因：{}'.format(err))
            raise

    def query(self, sql_):
        """
        数据库查询通用步骤
        1、建立连接
        2、获取游标
        3、执行sql语句
        4、提交到数据库执行sql
        5、获取返回的结果
        6、关闭游标
        7、断开连接
        :param sql_: 待查询的sql语句
        :return: 查询出来的结果
        """

        conn = self.db_pool.connection()
        cur = conn.cursor()
        cur.execute(sql_)
        rows = cur.fetchall()
        cur.close()
        conn.close()

        return list(rows)

    def execute(self, sql_):
        """
        在数据库中执行sql语句
        :param sql_: 待执行的sql语句
        :return: 受影响的行数即执行结果
        """
        try:
            conn = self.db_pool.connection()
            cur = conn.cursor()
            count = cur.execute(sql_)
            conn.commit()
            cur.close()
            conn.close()

            return count
        except Exception as err:
            logger.error('数据库操作出错！可能是当前用户没有数据库修改权限...请检查: {}'.format(err))

    @staticmethod
    def sql_result_to_json(sql_result, fill_field_list, decimal_type_convert_to=1):
        """
        数据库查询结果转json
        :param sql_result: 数据库查询结果
        :param fill_field_list: 填充的json字段列表  如：["SessionId", "IsAgent"]
        :param decimal_type_convert_to: decimal类型的字段转换后的类型 (默认1: 转成float类型 2：int类型)
        """
        result_json_list = []

        if isinstance(sql_result, list) and isinstance(fill_field_list, list):
            for result in sql_result:
                json_dic = {}
                if len(fill_field_list) != len(result):
                    raise ValueError('查询结果和填充参数不匹配，无法转化！')
                for i in range(len(result)):
                    fill_field_value = result[i]
                    if isinstance(result[i], decimal.Decimal) and decimal_type_convert_to == 1:
                        fill_field_value = float(result[i])
                    if isinstance(result[i], decimal.Decimal) and decimal_type_convert_to == 2:
                        fill_field_value = int(result[i])
                    if isinstance(result[i], datetime.datetime):  # 如果数据库查询返回的值为时间类型，则需要转换
                        fill_field_value = str(result[i])
                    json_dic.update({fill_field_list[i]: fill_field_value})
                result_json_list.append(json_dic)
        else:
            raise TypeError('查询结果和填充参数必须为列表类型！')

        return result_json_list


class RedisUtil:
    def __init__(self, redis_alias='REDIS', redis_port=''):
        self.config = configparser.ConfigParser()
        self.config.read(Config().db_config_path, encoding='utf-8')
        self.DB_HOST = self.config.get('%s' % redis_alias, 'REDISHOST')
        self.DB_PORT = self.config.getint('%s' % redis_alias, 'REDISPORT')
        self.config.read(Config().g_config_path, encoding='utf-8')
        self.env_name = self.config.get('default', 'env_name')
        self.alias_port = redis_port
        logger.info("REDISHOST数据为：{}".format(self.DB_HOST))

    def conn(self):
        if self.alias_port:
            nodes = [{"host": self.DB_HOST, "port": self.alias_port}, ]
            self.DB_PORT = self.alias_port
        else:
            nodes = [{"host": self.DB_HOST, "port": self.DB_PORT}, ]

        if self.env_name == '线上环境':     # 集群redis环境下使用
            # decode_responses=True，返回key/value的value类型为str，否则为字节类型
            rds = Redis(host=self.DB_HOST, port=self.DB_PORT, decode_responses=True)
        else:
            rds = StrictRedis(startup_nodes=nodes, decode_responses=True)
            pass

        return rds


if __name__ == '__main__':
    db = DBUtil()
    sql_ = """select title from test_table"""
    result = db.query(sql_)
    data = db.sql_result_to_json(result, ['title'])
    logger.info(data)