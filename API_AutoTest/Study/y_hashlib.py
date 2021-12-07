import hashlib
import json

"""
https://www.liujiangblog.com/course/python/58
md5摘要算法：
1、调用md5()方法
2、调用hexdigest()方法
"""
md5 = hashlib.md5()
md5.update('待加密的text文本'.encode('utf-8'))
print(md5.hexdigest())

body = {"param":"{\"userName\":\"yolo24\",\"password\":\"8196658ecaeceb870d0ad3053dd579d2\",\"validateCode\":\"\",\"onlyFlag\":\"VUEX21f1f19edff198e2a2356bf4XXXX\",\"clientFlag\":\"WEB\"}"}
f = json.dumps(body)
print(f)