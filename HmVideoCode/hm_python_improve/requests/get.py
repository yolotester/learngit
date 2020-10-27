import requests
import json

url = 'http://httpbin.org'

def build_url(endpoint):
    return '/'.join([url,endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def simple_get_request():
    '''不带参数的get请求'''
    res = requests.get(build_url('get'))

    print(type(res.text))  # str类型
    print(res.reason)

    print('>>>>Response Header:')
    print(res.headers)
    print('>>>>RH Date:')  # 取响应头中的Date数据
    print(res.headers['date'])

    print('>>>>Response Body:')
    print(res.text)

    print(res.request.headers)  # 请求消息头


def use_params_get_request():
    '''构造带参数的get请求'''
    params = {'show_env':"1", 'yolo':'2'}
    res = requests.get(url=build_url('get'),params=params)
    print(res.url)  # get方式带参数的url

    print('>>>>Response Body:')
    print(res.text)


    js = res.json()
    print(js)
    print(js['args'])


def have_header_get_request():
    '''构造请求头中的数据'''
    headers = {'user-agent':'test request headers'}
    res = requests.get(url=build_url('get'),headers = headers)
    print(res.text)
    js = res.json()
    print(js['headers']['User-Agent'])
    print(res.request.headers)




if __name__ == '__main__':
    # simple_get_request()
     use_params_get_request()
    # have_header_get_request()