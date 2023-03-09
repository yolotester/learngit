#! usr/bin/env python
# -*- coding: utf-8 -*-


# @Time   : 2020/10/27 0:42
# @Author : Yolo
# @Desc   : http协议请求库
# @File   : Http_Util.py
# @Software: PyCharm

import json
import jsonpointer

import jsonpatch
import urllib3

# 禁用安全请求警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class TestRequests():
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
        except Exception:
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
