# encoding=gbk
# https://github.com/psf/requests
# http://httpbin.org/
'''
import requests
URL_ip = 'http://httpbin.org/ip'  # 测试请求此网站IP接口
URL_get = 'http://httpbin.org/get'  # 构建请求参数

#  Get 方法
def use_simple_requests():

    response = requests.get(URL_ip)
    print('>>>>Response Headers:')
    print(response.headers)
    print('>>>>Response Body:')
    print(response.text)

def use_params_requests():
    params = {'params1':'hello','params2':['world','world']}
    response = requests.get(URL_get,params=params)
    print('>>>>Encoding:')         # 编码格式
    print(response.encoding)
    print('>>>>Request URL:')      # 带参数请求的url
    print(response.url)
    print('>>>>Content:')          # 文本内容
    print(response.content)
    print('>>>>Response Headers:')   # 响应头
    print(response.headers)
    print('>>>>Status Code:')        #状态码
    print(response.status_code)
    print(response.reason)           # 状态码解释内容
    print('>>>>Response Body:')      # 响应体
    print(response.text)

if __name__ == '__main__':
    print('>>>Use simple requests:')
    use_simple_requests()
    print()
    print('>>>use params requests:')
    use_params_requests()
'''
import json
import requests
from requests import exceptions

URL = 'https://api.github.com'
def build_url(endpoint):
    return '/'.join([URL,endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_methond():
    # user 单数，表示的是当前用户
    response = requests.get(build_url('user/emails'),auth = ('yolotester','Yolo114963'))
    #print(response.text)
    print(better_print(response.text))

# 使用params参数发送带参数的请求，
def params_methond():
    r = requests.get(build_url('users'),params={'since':'11'})
    print(better_print(r.text))
    print(r.request.headers)
    print(r.url)

# patch方法修改
def json_request():
    #r = requests.patch(build_url('user'),auth = ('yolotester','Yolo114963'),json = {'name':'yolotester1'})
    r = requests.post(build_url('user/emails'),auth=('yolotester','Yolo114963'),json=['ying31@github.com'])
    print(better_print(r.text))
    print(r.request.headers)
    print()
    print(r.request.body)
    print(r.status_code)

# 超时异常/HTTPError异常
def timeout_request():
    try:
        response = requests.get(build_url('user/emails'),timeout = 10)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print('超时了' + str(e))
    except exceptions.HTTPError as e:
        print('出错了' + str(e))
    else:
        print(better_print(response.text))
        print(response.status_code)

# session 对象，需要先准备请求(可自定义请求)，然后发送请求，获得响应
def hard_request():
    from requests import Request,Session
    s = Session()
    headers = {'user-agent':'yoloooooo'}
    req = Request('GET',build_url('user/emails'),auth=('yolotester','Yolo114963'),headers=headers)
    prepped = req.prepare()
    print(prepped.body)
    print(prepped.headers)

    rsend = s.send(prepped,timeout = 2)
    print(rsend.status_code)
    print(better_print(rsend.text))

# Response对象的方法，status_code ,reason,headers,url,history,elapsed(得到响应所消耗的时间)
# encoding,content,text,json(被转换成字典)
def response_request():
    response = requests.get('https://api.github.com')
    print(response.elapsed)
    print(response.json())
    print(response.json()['emails_url'])
    print(response.encoding)

# 下载图片/文件步骤：模拟浏览器请求-》构建request信息-》读取流数据-》写入文件
def download_img():
    url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1587156066192&di=66cc0fdb9bdde55d479dea59a5550e9a&imgtype=0&src=http%3A%2F%2Fww1.sinaimg.cn%2Flarge%2F006tNbRwgy1fdnex0ogd5j31jk0ih74t.jpg'
    # 伪造headers信息
    headers = {'user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    # 构建request对象
    response = requests.get(url,headers= headers,stream =True)


    print(response.status_code,response.reason)
    # 以上下文管理的方式，在流开启，传输完毕后，自动关闭流
    # from contextlib import closing
    # with closing(requests.get(url,headers= headers,stream =True)) as response:
    with open('demo1.jpg','wb') as fd:
        # 读取流数据
        for each in response.iter_content(128):
            # 写入文件
            fd.write(each)

# 事件钩子 event hooks，非线性处理的方式
# io请求-》服务器-》得到响应，直接进入回调函数
def get_key_info(response,*args,**kwargs):
    '''
    回调函数
    :return:
    '''
    print(response.headers['content-type'])

def main():
    requests.get('https://www.baidu.com',hooks = dict(response = get_key_info))

# http认证  基本认证：auth参数
Base_url = 'https://api.github.com'
def build_url(end_point):
    return  '/'.join([Base_url,end_point])
def basic_auth():
    '''
    基本认证
    :return:
    '''

    response = requests.get(build_url('user'),auth = ('yolotester','Yolo114963'))
    print(response.text)
    print(response.request.headers)
    print(response.request.headers['authorization'])  # 可通过base64.b64decode()方法解码出来，就是我的用户名和密码

# oauth 认证  token
def basic_oauth():
    # 已获得token值，进行token 认证
    headers = {'Authorization':'token 0ad9de577e29a9e848612fd972f7adecda3fba44'}
    # '/user/emails'
    response = requests.get(build_url('user/emails'),headers=headers)
    print(response.text)
    print(response.request.headers)
    print(response.status_code,response.reason)

# auth 认证库
from requests.auth import AuthBase
class Githubauth(AuthBase):
    def __init__(self,token):
        self.token = token
        # 类装饰器
    def __call__(self, req):
        # requests add headers
        req.headers['Authorization'] = ' '.join(['token',self.token])
        return req
def auth_advanced():
    auth = Githubauth('0ad9de577e29a9e848612fd972f7adecda3fba44')
    response = requests.get(build_url('user/emails'),auth = auth)
    print(response.text)

# proxy 代理，主要功能：转发请求  启动代理服务器heroku或其他-》在主机1080端口启动socks服务-》将请求转发到1080端口-》获取相应资源
# def proxy_request():
#     proxies = {'http':'socks5://127.0.0.1:1080','https:':'socks5://127.0.0.1:1080'}
#     response = requests.get('https://www.facebook.com',timeout = 10,proxies = proxies)
#     print(response.text)

# Session 和 Cookie


if __name__ == '__main__':
    request_methond()