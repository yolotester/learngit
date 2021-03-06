#!/usr/bin/env python
# -*- coding: utf-8 -*-


# @Time    : 2019/2/18 11:05
# @Author  : Yolo
# @Desc    : 自定义异常类
# @File    : Errors.py
# @Software: PyCharm


class UserConfigIsInvalid(Exception):
    """
    检查用户配置信息无效时抛出此异常
    """
    pass


class TokenException(Exception):
    """
    获取token失败时抛出此异常
    """
    pass


class CheckApiException(Exception):
    """
    检查api失败时抛出此异常
    """
    pass


class LoginException(Exception):
    """
    登录失败时抛出此异常
    """
    pass


class ApiTempletNotFound(Exception):
    """
    未匹配到接口模板时抛出此异常
    """
    pass


class MultipleApiTempletIsFound(Exception):
    """
    匹配到多个接口模板时抛出此异常
    """
    pass


class CaseDataNotFound(Exception):
    """
    接口用例数据未匹配到时抛出此异常
    """
    pass


class DataFileNotFound(FileNotFoundError):
    """
    测试数据文件未找到时抛出此异常
    """
    pass


class MappingError(Exception):
    """
    api_type映射错误时抛出此异常
    """
    pass


class InterfaceVerifyError(Exception):
    """
    接口校验错误时抛出此异常
    """
    pass


class NotMatchExcelDataError(Exception):
    """
    未匹配到excel数据时抛出此异常
    """
    pass


class NotDBDataError(Exception):
    """
    未取到数据库数据时抛出此异常
    """
    pass