#! usr/bin/env python
# -*- coding: utf-8 -*-


# @Time    : 2020/10/27 0:42
# @Author  : Yolo
# @Desc    : 配置类
# @File    : Config.py
# @Software: PyCharm

import os
import configparser


class MyConfig(configparser.ConfigParser):

    # 重写初始化方法
    def __init__(self):
        # 调用父类初始化方法
        configparser.ConfigParser.__init__(self, defaults=None)  # defaults : 如果指定默认值，则使用默认值的键值对

    def optionxform(self, optionstr):
        """
        optionxform()，在传递键值对数据时，会将键名 全部转化为小写
        :param optionstr: 在一个实例上重新设置它，对于一个需要字符串参数的函数。例如，将其设置为str，将使选项名称区分大小写
        :return:
        """
        return optionstr


class Config(object):

    def __init__(self):
        """
        初始化配置
        """
        self.current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # D:\Git\learngit\API_AutoTest
        self.config_path = os.path.join(self.current_path, 'Config')  # D:\Git\learngit\API_AutoTest\Config
        self.log_config_path = os.path.join(self.config_path, 'log_config.ini')
        self.v_config_path = os.path.join(self.config_path, 'var_config.ini')
        self.g_config_path = os.path.join(self.config_path, 'config.ini')
        self.db_config_path = os.path.join(self.config_path, 'db_config.txt')

        # 实例化对象，用于操作config.ini
        self.config = MyConfig()
        self.config.read(self.g_config_path, encoding='utf-8')
        self.project_name_tag = self.config.get('default', 'project_name_tag')  # 获得project_name_tag的值
        self.data_path = os.path.join(os.path.join(self.current_path, 'Data'),
                                      'Project_' + self.project_name_tag)  # 测试数据的位置
        self.tool_path = os.path.join(self.current_path, 'Tools')  # 工具包的位置
        self.log_path = os.path.join(self.current_path, 'Logs')  # 日志位置
        self.report_path = os.path.join(self.current_path, 'Reports')  # 报告位置

        # 实例化对象，用于操作var_config.ini
        self.v_config = MyConfig()
        self.v_config.read(self.v_config_path, encoding='utf-8')
        self.html_report_filename = os.path.join(self.report_path, 'result.html')
        self.data_file_name = os.path.join(self.data_path, self.config.get('default',
                                                                           'data_file_name'))  # 把config.ini中data_file_name的值取出，并join一起
        self.tool_file_name = os.path.join(os.path.join(self.tool_path, 'Data'),
                                           self.config.get('default', 'tool_file_name'))
        self.template_file_name = os.path.join(self.data_path, self.config.get('default', 'template_file_name'))
        self.data_source = self.config.getint('default', 'data_source')
        self.err_code = self.config.getint('default', 'err_code')
        self.err_info = self.config.get('default', 'err_info')
        self.retry_times = self.config.get('default', 'retry_times')
        self.is_write_test_result = self.config.getint('default', 'is_write_test_result')
        self.sheet_name_list = self.config.get('rules', 'SheetNameList')
        self.is_regression = self.config.get('rules', 'IsRegression')
        self.is_smoke = self.config.get('rules', 'IsSmoke')
        self.apply_env = self.config.get('rules', 'ApplyEnv')
        self.run_result = self.config.get('rules', 'RunResult')

        self.api_type = int(self.get_option_config('ApiType'))

        # self.config.sections()[self.api_type]  sections()方法以列表形式返回所有section
        # 当api_type为1，则使用的是测试环境的配置，当api_type为2，则使用的是预发布环境的配置
        self.db_cfg_name = self.config.get(self.config.sections()[self.api_type], 'env_db_cfg_item')
        self.facount = self.config.get(self.config.sections()[self.api_type], 'FAcount')
        self.ag_host = self.config.get(self.config.sections()[self.api_type], 'ag_host')
        self.api_host = self.config.get(self.config.sections()[self.api_type], 'api_host')
        self.key = self.config.get(self.config.sections()[self.api_type], 'key')

    def get_option_config(self, option_name, section_name='Global_Variable'):
        """
        返回 var_config.ini中 section=Global_Variable 的配置
        :param variable_name: 变量名
        :param section_name: 变量名所在的section
        :return:
        """
        # 异常捕获，如果Global_Variable中 ，有该option，则返回。无则抛出异常
        try:
            return_variable = self.v_config.get(section_name, option_name)
            return return_variable
        except configparser.NoOptionError as err:
            raise err

    def set_variable_config(self, item_name, item_value, section_name='Global_Variable'):
        """
        写入 var_config.ini中 section=Global_Variable 的配置
        :param item_name: 变量名
        :param item_value: 变量值
        :param section_name: 变量名所在的section
        :return:
        """
        self.v_config.set(section_name, item_name, item_value)

        # 打开var_config.ini文件，会自动关闭该文件
        with open(self.v_config_path, 'w') as f:
            self.v_config.write(f)  # 将配置写入var_config.ini文件

    def get_run_config(self):
        """
        返回全局运行规则字典, 筛选测试用例
        """
        run_rules_dic = {}

        """
        用 update 更新字典 a，会有两种情况：

        （1）有相同的键时：会使用最新的字典 b 中 该 key 对应的 value 值。
        （2）有新的键时：会直接把字典 b 中的 key、value 加入到 a 中。
        """
        if self.is_regression:
            run_rules_dic.update({'IsRegression': self.is_regression})

        if self.is_smoke:
            run_rules_dic.update({'IsSmoke': self.is_smoke})

        if self.apply_env:
            run_rules_dic.update({'ApplyEnv': self.apply_env})

        if self.run_result:
            run_rules_dic.update({'RunResult': self.run_result})

        return run_rules_dic


if __name__ == '__main__':
    print(Config().log_config_path)
    print(Config().get_option_config('UserName'))
    print(Config().api_type)
    print(Config().db_config_path)
