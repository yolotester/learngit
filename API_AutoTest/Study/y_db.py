#! usr/bin/env python
# -*- coding: utf-8 -*-


import pymysql, pymysql, configparser, decimal, datetime
from dbutils.pooled_db import PooledDB
from Libs.Log_Util import logger
from Config.Config import *
from rediscluster import StrictRedisCluster
from redis import Redis, StrictRedis


class DBUtil:

    def __init__(self, db_alias='MYSQL'):
        self.conf = configparser.ConfigParser()
        self.conf.read(Config().db_config_path, encoding='UTF-8')
        self.HOST = self.conf.get("%s" % db_alias, "DBHOST")
        self.PORT = self.conf.getint("%s" % db_alias, "DBPORT")
        self.USER = self.conf.get("%s" % db_alias, "DBUSER")
        self.PASSWORD = self.conf.get("%s" % db_alias, "DBPASSWORD")
        self.SCHEMA = self.conf.get("%s" % db_alias, "DBSCHEMA")

        try:
            if db_alias.startswith("MYSQL"):
                self.db_pool = PooledDB(creator=pymysql, mincached=2, maxcached=40, host=self.HOST,
                                        port=self.PORT, user=self.USER, password=self.PASSWORD, database=self.SCHEMA)
            elif db_alias.startswith("MSSQL"):  # sqlserver不需要port
                self.db_pool = PooledDB(creator=pymysql, mincached=2, maxcached=40, host=self.HOST,
                                        user=self.USER, password=self.PASSWORD, database=self.SCHEMA)
            else:
                raise ValueError("不支持的数据库类型：{}".format(db_alias))
        except Exception as err:
            logger.error("数据库连接失败，原因：{}".format(err))

    def query(self, sql_):
        """
        查询数据库通用步骤：
        1、建立连接
        2、获取游标
        3、执行sql语句
        4、获取返回的结果
        5、关闭游标
        6、断开连接
        :param sql_: 待执行的sql语句
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
        执行sql操作
        :param sql_: 待查询的sql语句
        :return: 受影响的行数，即执行结果
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
            logger.error("提交数据库失败，可能是没有修改权限，请检查具体原因：{}".format(err))

    def sql_result_to_json(self, sql_result, field_data_list, data_revert=1):
        """
        数据库查询结果转化为json
      :param sql_result:
      :param field_data_list: 填充的json数据，例如：["id", "title"]
      :param data_revert: decimal类型转化为 1 float类型， 2 int类型
      :return:
      """
        data_list = []
        if isinstance(sql_result, list) and isinstance(field_data_list, list):
            for result in sql_result:
                logger.debug("查询结果列表中的每个元素:{}".format(result))

                if len(result) != len(field_data_list):
                    logger.error("查询出来的结果和填充字段不匹配，无法转化！")
                result_dict = {}
                for i in range(len(result)):
                    field_data_value = result[i]
                    if isinstance(result[i], decimal.Decimal) and data_revert == 1:
                        field_data_value = float(result[i])
                    if isinstance(result[i], decimal.Decimal) and data_revert == 2:
                        field_data_value = int(result[i])
                    if isinstance(result[i], datetime.datetime):
                        field_data_value = str(result[i])
                    result_dict.update({field_data_list[i]: field_data_value})
                data_list.append(result_dict)
        else:
            raise TypeError('查询结果和填充参数必须为列表类型！')

        return data_list


class REDISUtil:

    def __init__(self, alias="REDIS", port=''):
        self.config = configparser.ConfigParser()
        self.config.read(Config().db_config_path, encoding="utf-8")
        self.HOST = self.config.get("%s" % alias, "HOST")
        self.PORT = self.config.get("%s" % alias, "PORT")
        self.PASSWORD = self.config.get("%s" % alias, "PASSWORD")
        self.config.read(Config().g_config_path, encoding="utf-8")
        self.ENV_NAME = self.config.get("default", "env_name")
        self.port = port

    def conn(self):
        if self.port:  # 如果传了端口号
            nodes = [{"host": self.HOST, "port": self.port}, ]
        else:
            nodes = [{"host": self.HOST, "port": self.PORT}, ]

        if self.ENV_NAME == '线上环境':  # 线上环境使用集群模式,跳过版本检查，编码响应类型为str
            redis_client = StrictRedisCluster(startup_nodes=nodes, password=self.PASSWORD,
                                              skip_full_coverage_check=True, decode_responses=True)
        else:
            redis_client = StrictRedis(startup_nodes=nodes, decode_responses=True)

        return redis_client


if __name__ == '__main__':
    sql_ = """select title from test_table"""
    sql1_ = """update test_table set title = 'foodss' where id = 6"""
    result = DBUtil().query(sql_)
    logger.info(result)
    data = DBUtil().sql_result_to_json(result, ['title'])
    logger.info(data)
