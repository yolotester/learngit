#! usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Dict

import jsonpatch, jsonpointer, json
from Libs.Log_Util import logger

"""
https://www.runoob.com/python/python-json.html
json.loads  --  将已编码的json字符串解码为python对象，对象（object）可以用.来调用属性
json.dumps  --  将 Python 对象编码成 JSON 字符串， 字符串（str）只能用字符串相应方法

https://python-json-pointer.readthedocs.io/en/latest/mod-jsonpointer.html
https://python-json-patch.readthedocs.io/en/latest/mod-jsonpatch.html
"""

person_dict1: Dict[str, str] = {"name": "hangman", "sex": "男", "age": "24"}
logger.info("person_dict的类型为：{}".format(type(person_dict1)))

person_dict_to_str = json.dumps(person_dict1, indent=4, ensure_ascii=True)
logger.info("person_dict_to_str的类型为：{}".format(type(person_dict_to_str)))

person_str1 = '{"name": "hangman", "sex": "男", "age": "24"}'
logger.info("person_str的类型为：{}".format(type(person_str1)))

person_str_to_dict = json.loads(person_str1)
logger.info("person_str_to_dict的类型为：{}".format(type(person_str_to_dict)))

try:
    result = jsonpointer.resolve_pointer(person_dict1, '/name')
    logger.info("获取到的value为：{}".format(result))
except Exception as err:
    raise Exception("获取json信息异常：{}".format(err))

try:
    patch = [{
        "op":"add",
        "path":"/address",
        "value":"SH"
    }]
    person_dict1 = jsonpatch.apply_patch(person_dict1, patch)
    # print(result)
except Exception as err:
    raise Exception("写入json信息异常：.{}".format(err))

logger.info(person_dict1)

for data_ in person_dict1:
    print(data_)

logger.info(person_dict1.items()) # 返回
set_like = ('filter', {'ID': 'I001'})
for set_ in set_like:
    print(set_like[set_])



