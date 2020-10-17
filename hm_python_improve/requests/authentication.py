import requests
import json
from requests.auth import HTTPDigestAuth

url = 'http://httpbin.org'

def build_url(endpoint):
    return '/'.join([url,endpoint])

def basic_auth():
    '''基本账户密码认证'''
    res = requests.get(url=build_url('basic-auth/user/passwd'))
    print('未提供用户密码：' + str(res.reason))

    res2 = requests.get(url=build_url('basic-auth/user/passwd'), auth=('user', 'passwd'))
    print('已提供用户名和密码：' + str(res2.status_code))

def digest_auth():
    '''数字认证'''
    res = requests.get(url=build_url('digest-auth/auth/user/pass'),auth=HTTPDigestAuth('user','pass'))
    print(res.status_code)
    print(res.reason)

def proxy_params():
    '''设置代理的第一种方法：使用proxy参数'''
    proxies=dict(https = 'http://41.118.132.69:4433')
    res = requests.post(url=build_url('post'), proxies=proxies)
    print(res.text)

def ssl_auth():
    '''ssl证书认证之关闭验证'''
    res = requests.get('https://kyfw.12306.cn/otn/', verify=False)
    print(res.text)
    print(res.history)

if __name__ == '__main__':
    # basic_auth()
    #　digest_auth()
    # proxy_params()
    ssl_auth()