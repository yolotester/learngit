#! usr/bin/env python
# -*- coding: utf-8 -*-


# @Time    : 2020/10/27 0:42
# @Author  : Yolo
# @Desc    : 配置类
# @File    : Config.py
# @Softwore: PyCharm

import os
import configparser

class MyConfig(configparser.ConfigParser):
    def __init__(self):
        configparser.ConfigParser.__init__(self, defaults=None)  # defaults : 如果指定默认值，则使用默认值的键值对

    def optionxform(self, optionstr):
        '''
        optionxform()，在传递键值对数据时，会将键名 全部转化为小写
        :param optionstr: 在一个实例上重新设置它，对于一个需要字符串参数的函数。例如，将其设置为str，将使选项名称区分大小写
        :return:
        '''
        return optionstr


class Config(object):

    def __init__(self):
        '''
        初始化配置 -- 简化使用
        '''
        self.current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # D:\Git\learngit\API_AutoTest
        self.config_path = os.path.join(self.current_path, 'Config')
        self.log_config_path = os.path.join(self.config_path, 'log_config.ini')
        self.v_config_path = os.path.join(self.config_path, 'var_config.ini')
        self.g_config_path = os.path.join(self.config_path, 'config.ini')

        self.log_path = os.path.join(self.current_path, 'Logs')

        # 实例化对象，用于操作config.ini
        self.config = MyConfig()
        self.config.read(self.g_config_path, encoding='utf-8')
        self.project_name_tag = self.config.get('default', 'project_name_tag')

        # 实例化对象，用于操作var_config.ini
        self.v_config = MyConfig()
        self.v_config.read(self.v_config_path, encoding='utf-8')

        # self.l_config = MyConfig()
        # self.l_config.read(self.log_config_path, encoding='utf-8')

        # print(self.current_path)


    def get_variable_config(self, variable_name, section_name='Global_Variable'):
        '''
        返回 var_config.ini中 section=Global_Variable 的配置
        :param variable_name: 变量名
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
        写入 var_config.ini中 section=Global_Variable 的配置
        :param item_name: 变量名
        :param item_value: 变量值
        :param section_name: 变量名所在的section
        :return:
        '''
        self.v_config.set(section_name, item_name, item_value)

        with open(self.v_config_path, 'w') as f:
            self.v_config.write(f)



if __name__=='__main__':
    print(Config().log_config_path)
    c = Config()
    print(c.l_config['LOGGING']['backup_count'])
