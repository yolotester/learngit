#! usr/bin/env python
# -*- coding: utf-8 -*-


# @Time   : 2020/10/27 0:42
# @Author : Yolo
# @Desc   : http协议请求库
# @File   : Http_Util.py
# @Software: PyCharm

import json
import time

import jsonpointer

import jsonpatch
import urllib3
import requests
import traceback
from Libs.Log_Util import logger
from Config.Config import *
from Excel_Util import ExcelUtil
from Common_Util import *

# 禁用安全请求警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_json_value(json_string, json_pointer, error_msg=''):
    """
        获取json值
        :param json_string:
        :param json_pointer: json指针
        :param error_msg:
        :return:
        """
    if isinstance(json_string, str):
        json_dict = json.loads(json_string)  # 将已编码的 JSON 字符串解码为 Python 对象
    else:
        json_dict = json_string

    try:
        result = jsonpointer.resolve_pointer(json_dict, json_pointer)
        return result
    except Exception as error_msg:
        raise Exception('获取json信息异常：【%s】' % error_msg)


def set_json_value(json_string, json_pointer, json_value):
    """
        设置json值
        :param json_string:
        :param json_pointer:
        :param json_value:
        :return:
        """
    if isinstance(json_string, str):  # 判断是否是字符串类型
        json_dict = json.loads(json_string)
    else:
        json_dict = json_string

    result = jsonpatch.apply_patch(json_dict, [{"op": "add", "path": json_pointer, "value": json_value}])
    return result


def warp_request(url, body=None, headers=None, cookies=None, method="POST"):
    """
    使用requests库封装http请求
    :param url:
    :param body:
    :param headers:
    :param cookies:
    :param method:
    :return:
    """
    try:
        if method == "POST":  # data可传输字典
            http_client = requests.post(url=url, data=body, headers=headers, cookies=cookies, verify=False,
                                        allow_redirects=False)
        elif method == "GET":
            http_client = requests.get(url=url, data=body, headers=headers, cookies=cookies, verify=False,
                                       allow_redirects=False)
        else:
            logger.error("不支持的请求方式！")

        if "application/json" in http_client.headers["Content-Type"]:
            rev_msg = http_client.json()
            status_code = str(http_client.status_code)
            rev_msg = json.dumps(rev_msg, ensure_ascii=True, indent=4)
        else:
            rev_msg = http_client.text
            status_code = str(http_client.status_code)
        logger.info("响应消息：{}\n".format(rev_msg))
        logger.info("响应状态码：{}".format(status_code))

        return rev_msg, http_client
    except Exception as err:
        traceback.print_exc(err)
        raise Exception(err)


def get_interface_from_db(temp_path):
    pass


def get_interface_from_excel(temp_path):
    """
    从Excel中获取接口模版
    :param temp_path: 模版路径，例如：登录注册.获取全局Token
    :return: 返回模版
    """
    temp = temp_path.split('.')
    logger.debug("分割数据后：{}".format(temp))
    module_name = temp[0]
    interface_name = temp[1]
    temp = ExcelUtil(Config().template_file_name, 'Interface').excel_interface_info(
        {'ModuleName': module_name, 'InterfaceName': interface_name})[0]  # [{},{}]模版只有一条，列表中取值
    temp_dict = {"url": temp['URL'],
                 "method": temp['Method'],
                 "headers": json.loads(temp['Headers']) if temp['Headers'] else None,
                 "api_type": temp['ApiType'],
                 "body": json.loads(temp['Body']) if temp['Body'] else None,
                 "is_sign": temp['IsSign']}
    logger.debug("获取到的接口模版：{}".format(json.dumps(temp, ensure_ascii=False, indent=4)))
    return temp_dict


def http_request_api(temp_path, api=Config().api_host, **params):
    """
    业务接口请求封装
    :param temp_path: 模版路径，格式：用户模块.登录
    :param api: api接口
    :param kwargs: 字典参数
    :return:
    """
    if Config().data_source:
        temp_dict = get_interface_from_db(temp_path)
    else:
        temp_dict = get_interface_from_excel(temp_path)
    url = api + temp_dict['url']
    method = temp_dict['method']
    is_sign = temp_dict['is_sign']
    headers = temp_dict['headers']
    cookies = {}
    if 'Headers' in params:  # 使用传进来的Headers来替换模版中的Headers
        headers.update(params['Headers'])
        cookies.update(params['Headers'])
    body = temp_dict['body']

    for key_ in params['NewParamsVerify'].keys():  # 循环替换body中的值
        """
        1、遍历新参数字典的key
        2、若body中的key和新参数字段的key相同
            2.1、则替换body该key的值
        3、若新参数字典的key对应的值为 del
            3.1、则删除掉body中对应的key
        """
        if key_ == body.keys():
            body = set_json_value(body, '/' + key_, params['NewParamsVerify'][key_])
        if params['NewParamsVerify'][key_] == 'del':
            body.pop(key_)

    if temp_dict['api_type'] == 'HC':  # 根据不同的接口类型，设置不同的参数传递方式
        body = {'param': json.dumps(body)} if body else {}  # application/json
    else:
        body = json_convert_to_key_value(body) if body else {}
        headers.update({"Content-Type": "application/x-www-form-urlencoded"})

    for retry_time in range(Config().retry_times + 1):  # 重试机制
        if retry_time == Config().retry_times:
            assert False, '多次请求连接未得到响应，请检查...'
        logger.info("获取模版：{}".format(temp_dict))
        rev_msg, http_client = warp_request(url=url, body=body, headers=headers, cookies=cookies, method=method)

        if 'application/json' in http_client.headers['Content-Type']:
            try:
                err_code_result = Config().err_code == (get_json_value(rev_msg, '/code'))
                err_msg_result = any([word in get_json_value(rev_msg, '/data') for word in Config().err_info])
            except Exception:
                err_msg_result = False
                err_code_result = False
            if err_code_result or err_msg_result:
                logger.info("已经尝试重连了{}次，请等待20s后重试...".format(retry_time+1))
                time.sleep(20)
                continue
            else:
                break
        else:
            break


if __name__ == '__main__':
    get_interface_from_excel('登录注册.用户登录')

