#! usr/bin/env python
# -*- coding: utf-8 -*-


# @Time   : 2020/10/27 0:42
# @Author : Yolo
# @Desc   : 测试数据集操作库
# @File   : 
# @Software:

from Libs.Log_Util import logger
from Libs.Excel_Util import ExcelUtil
from Libs.DB_Util import DBUtil
from Libs.Errors import *
from Config.Config import *

def get_data_from_db(script_name, *parameter_name):
    """
    从数据库内获取数据
    :param script_name: 脚本名称
    :param parameter_name: 参数名
    :return:
    """
    db_util = DBUtil()
    env_sql = '''select url,value from t_server_config where type='Running_env';'''
    env_info = db_util.query(env_sql)[0]
    # 下面是根据当前用户的测试环境，匹配选择相应环境下的测试数据
    env_name = env_info['url']
    env_type = env_info['value']

    if env_name == 'test':
        enum_name = '1-%s' % env_type
    elif env_name == 'pre':
        enum_name = '2-%s' % env_type
    elif env_name == 'line':
        enum_name = '3-%s' % env_type

    # 枚举环境标识对应的数据分类
    enum_info = {'1-1': '测试环境-分支1', '1-2': '测试环境-分支2', '2-1': '演示环境-分支1', '2-2': '演示环境-分支2', '3-1': '生产环境-分支1', '3-2': '生产环境-分支2'}

    # 是哪个环境，则从哪个环境的数据获取数据
    class_name = env_info[enum_name]
    class_sql = '''select id from t_data_class where class_name='%s';''' % class_name
    class_id = db_util.query(class_sql)[0]['id']
    logger.info('开始获取【%s】的测试数据... ...' % class_name)

    sql = '''SELECT
                b.data_name AS name,
                b.data_value AS value
            FROM
                t_data_unit a,
                t_data b
            WHERE
                a.id = b.data_unit_id
            AND a.class_id = '%s'
            AND a.data_unit_name = '%s';
            ''' % (class_id, script_name)

    logger.info(sql)
    sql_result = db_util.query(sql)

    return sql_result

def get_case_from_excel_by_filter(file_name, sheet_name_list, filter_name_value):
    """
    从Excel文件获取测试用例/数据
    :param file_name: 数据文件名
    :param sheet_name_list: sheet名称列表（在数据表格内体现为模块名）
    :param filter_name_value: 要过滤的字段字典（如果没有则查询所有数据）
    :return:
    """
    excel_class = ExcelUtil(file_name)
    if not isinstance(sheet_name_list, list):
        raise TypeError('提供的Sheet名必须为列表类型！')
    # 从接口用例文件中获取用例信息
    case_info = excel_class.excel_case_info(sheet_name_list=sheet_name_list, filter_field=filter_name_value) \
            if filter_name_value else excel_class.excel_case_info(sheet_name_list=sheet_name_list)

    if not case_info:
        raise CaseDataNotFound('Excel接口用例数据文件中未找到待匹配的接口用例')
    return case_info

def save_case_result_to_excel(file_name, sheet_name, r_name, c_value, value):
    """
    保存测试结果数据到excel
    :param file_name: 数据文件名
    :param sheet_name: sheet名称
    :param r_name: 查询的字段名 如：ID
    :param c_value: 查询的字段值 如：A001
    :param value: 结果值
    :return:
    """
    excel_class = ExcelUtil(file_name, sheet_name)
    match_value = excel_class.excel_field_name_value_match(r_name, c_value)
    excel_class.write_excel(match_value, excel_class.xls_wb.sheet_by_name(sheet_name).ncols, value)  # 默认取最后一列为结果写入字段


if __name__ == '__main__':
    save_case_result_to_excel(Config().data_file_name,  'User', 'ID', 'A006', 'fuck')
    filter_result = get_case_from_excel_by_filter(Config().data_file_name, ['User'], {'CaseName':'获取公司设置的验证码方式'})
    logger.warning(filter_result)
    '''
    [{'ID': 'A001', 'CaseName': '获取公司设置的验证码方式', 'ScriptName': 'Api_User_IT_GetValidateCodeConfig_001.py', 'Precondition': None, 'NeedLogin': 'NO', 'Desc': None, 'NewVerifParmsData': {}, 'ExpectResult': {'Status': True, 'Info': '请求成功', 'Code': 1}, 'AssociateInterface': '登录注册.获取验证码方式', 'IsRegression': 'YES', 'IsSmoke': 'YES', 'ApplyEnv': '全部', 'RunResult': 'Pass'}]
    '''