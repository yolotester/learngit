#!/usr/bin/env python
# -*- coding: utf-8 -*-


# @Time    : 2020/10/25 3:08
# @Author  : YOLO
# @Desc    : 配置类
# @File    : Config.py
# @Software: PyCharm

import os
import configparser

# 定制自己的解析器行为
class MyConfig(configparser.ConfigParser):
    def __init__(self):
        configparser.ConfigParser.__init__(self, defaults=None)

    def optionxform(self, optionstr):
        return optionstr


class Config(object):
    def __init__(self):
        '''
        初始化配置 -- 简化使用
        '''
        self.current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config_path = os.path.join(self.current_path, 'study_配置文件')
        self.g_config_path = os.path.join(self.config_path, 'config.ini')
        self.db_config_path = os.path.join(self.config_path, 'db_config.ini')
        # self.log_config_path = os.path.join(self.config_path, 'log_config.ini')
        self.v_config_path = os.path.join(self.config_path, 'var_config.ini')

        self.log_path = os.path.join(os.path.join(self.current_path, 'study_logger日志'), 'out_log')

        # 实例化一个对象，用于操作 var_config.ini
        self.v_config = MyConfig()
        self.v_config.read("var_config.ini", encoding='utf-8')

    def get_variable_config(self, variable_name, section_name='Global_Variable'):
        '''
        返回全局变量的值
        :param variable_name:变量名
        :param section_name: 变量名所在的section
        :return:
        '''
        try:
            return_variable = self.v_config.get(section_name, variable_name)
            return return_variable

        except configparser.NoOptionError as err:
            raise err

    def set_variable_config(self, item_name, item_value, section_name='Global_Variable'):
        '''
        写入全局变量配置
        :param item_name:变量名
        :param item_value:变量值
        :param section_name:变量名所在的section
        :return:
        '''

        self.v_config.set(section_name, item_name, str(item_value))

        with open("var_config.ini", "w+", encoding='utf8') as f:
            self.v_config.write(f)

if __name__=="__main__":
    print(Config().get_variable_config('UserName'))
    Config().set_variable_config('Fund_password', 'yolo02')
