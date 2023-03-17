#! usr/bin/env python
# -*- coding: utf-8 -*-
import json
import traceback

import requests
from Libs.Log_Util import logger
from Libs.Http_Util import set_json_value

x = requests.get('https://www.runoob.com/try/ajax/json_demo.json')
logger.info(x.status_code)

logger.info("status code的类型为：{}".format(type(x.status_code)))

person_dict1 = {"name": "hangman", "sex": "del", "age": "24"}
body = {"sex": "女"}
for key_ in person_dict1.keys():
    if key_ in body.keys():
        body = set_json_value(body, '/' + key_, person_dict1[key_])
    if person_dict1[key_] == 'del':
        body.pop(key_)

    logger.info("新body为：{}".format(json.dumps(body)))
logger.info(person_dict1.keys())


class WarpRequests():

    def __int__(self):
        pass

    def warp_requests(self, url, body=None, headers=None, cookies=None, method='post'):
        """
        封装请求方法
        :param url: 请求url
        :param body: 请求体，post请求会用到
        :param headers: 请求头
        :param cookies:
        :param method: 请求方法
        :return:
        """
        try:
            if method == "post":
                http_client = requests.post(url=url, data=body, headers=headers, cookies=cookies, verify=False,
                                            allow_redirects=False)
            elif method == "get":
                http_client = requests.get(url=url, params=body, headers=headers, cookies=cookies)
            else:
                logger.error("请求方式不正确，请检查！")

            if "application/json" in http_client.headers['Content-Type']:
                res_msg = http_client.json()
                res_status_code = str(http_client.status_code)
                res_msg = json.dumps(res_msg, indent=4, ensure_ascii=False)
            else:
                res_msg = http_client.text
                res_status_code = str(http_client.status_code)
            logger.info("响应状态码：{}".format(res_status_code))
            logger.info(("响应信息：{} \n".format(res_msg)))

            return res_msg, http_client

        except Exception as err:
            traceback.print_exc(err)
            raise Exception(err)

    def http_request_api(self, msg):
        pass
