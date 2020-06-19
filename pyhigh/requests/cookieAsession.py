import requests
import json
url = 'http://www.baidu.com'
host = 'http://httpbin.org'

def build_url(endpoint):
    return '/'.join([url,endpoint])

def build_host(endpoint):
    return '/'.join([host,endpoint])

def get_cookie_request():
    '''获取cookie'''
    # 制定header中的user-agent，不然会报ssl认证错误
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    res  = requests.get(url=url,headers = header)
    print(res.status_code)
    print('>>>>Response Cookies:')
    print(res.cookies)  #　Cookie的返回对象为RequestsCookieJar

    c = requests.utils.dict_from_cookiejar(res.cookies)  # #将RequestsCookieJar对象转换成字典
    print('>>>>Change Dict:')
    print(c)
    print('>>>>Get Value:')
    for a in res.cookies:
        print(a.name,a.value)

def simple_send_cookie():
    '''简单方式发送cookie'''
    cookie = {'cookie':'cookieValue'}
    res = requests.get(url=build_host('cookies'), cookies= cookie)
    print(res.text)
    c = requests.utils.dict_from_cookiejar(res.cookies)
    print(c)

def complex_send_cookie():
    '''复杂发送cookie，适合跨域名路径使用'''
    jar = requests.cookies.RequestsCookieJar()
    jar.set('cookie', 'cookieValue', domain = 'httpbin.org', path = '/cookies')
    res = requests.get(url=build_host('cookies'),cookies=jar)
    print('>>>>Cookie Text:')
    print(res.cookies)

def keep_session_Synchronize():
    '''保持会话同步'''

    s = requests.session()  # 初始化session对象
    r = s.get(url=build_host('cookies/set/cookies/123456'))  # 响应体set-cookie的值
    print(r.text)

def save_session_info():
    '''保存会话信息'''
    header1 = dict(testa ='AAA')
    header2 = dict(testb = "BBB")

    s = requests.session()
    s.headers.update(header1)  # 此操作后，header1的信息则会存在于服务器中
    r = s.get(url=build_host('headers'), headers = header2)  # 发送新的消息
    print(r.text)

def del_session_info():
    '''删除会话信息，即保存为None'''
    header1 = dict(testa='AAA')
    header2 = dict(testb="BBB")

    s = requests.session()
    s.headers.update(header1)  # 此操作后，header1的信息则会存在于服务器中
    r = s.get(url=build_host('headers'), headers=header2)  # 发送新的消息
    print(r.text)

    print('-------------------------')

    s.headers['testa'] = None
    r = s.get(url=build_host('headers'), headers=header2)
    print(r.text)

def default_info():
    '''提供默认数据'''
    s = requests.session()
    s.auth = ('user','pass')
    s.headers.update({'testc':'True'})
    r = s.get(build_host('headers'), headers = {'testc':'True'})
    print(r.text)



if __name__ == '__main__':
    # get_cookie_request()
    # simple_send_cookie()
    #　complex_send_cookie()
   # keep_session_Synchronize()
   save_session_info()
   # del_session_info()
   # default_info()