# encoding=utf-8

# 以访问github为例  get
import requests

URL_IP = 'https://api.github.com/events'
url = "http://httpbin.org/post"
def get_requests():
    response = requests.get(URL_IP)  # 返回response对象，赋值给变量response

    print('>>>>Json:')
    print(response.json())  # 成功调用json并不意味着响应的成功，检查请求是否成功
    print(response.raise_for_status())   # 因为访问成功，所以得到的是None
    print('>>>>Response Headers:')
    print(response.headers)

    # 访问响应头字段，是不区分大小写的
    print('>>>>Content-type')
    print(response.headers['content-type'])

    if response.status_code == 200:
        print('请求成功')
     # print(response.status_code == requests.codes.ok)   200返回True，另一种方式检查请求是否成功


    # 若发送了一个错误请求，可以response.raise_for_status()抛出异常
    bad_r = requests.get('http://httpbin.org/status/404')
    print('>>>>Status Code:')
    print(bad_r.status_code)
    print('>>>>Raise for Status:')
    print(bad_r.status_code == requests.codes.ok)      # 状态码404，返回false
    # print(bad_r.raise_for_status())  # 抛出异常

# Cookie,发送你的cookie到服务器，可以使用cookies参数
    cookies = dict(cookies_are='working')
    r = requests.get('http://httpbin.org/cookies',cookies=cookies)
    print('>>>>Cookie text：')
    print(r.text)

    # Cookie的返回对象为RequestsCookieJar，和字典类似，适合跨域名跨路径使用，可以把CookieJar传到Requests中
    jar = requests.cookies.RequestsCookieJar()
    jar.set('tasty_cookie','yolo',domain = 'httpbin.org',path = '/cookies')
    jar.set('gross_cookie','doudou', domain = 'httpbin.org',path = '/elsewhere')   # 未访问这个地址
    r = requests.get('http://httpbin.org/cookies',cookies=jar)
    print('>>>>Cookie text：')
    print(r.text)

# 重定向与请求历史 ，除了HEAD，Requests会自动处理重定向
# 可以使用响应对象的history来追踪重定向
    r = requests.get('http://github.com')
    print('>>>>History:')
    print(r.history)

    # 使用的是get，post，put，patch，delete，options，可以通过allow_redirects参数禁用重定向处理
    r = requests.get('http://github.com',allow_redirects = False)
    print('>>>>History:')
    print(r.history)

# Timeout  告诉requests在经过timeout设定的秒数时间之后停止等待响应，在timeout秒内没有应答，会引发一个异常
    # requests.get('http://github.com',timeout = 0.001)  requests.exceptions.ConnectTimeout: HTTPConnectionPool(host='github.com', port=80):
    requests.get('http://github.com',timeout = 2)

# 错误与异常
# 网络问题（DNS查询失败，拒绝连接），Requests会抛出一个ConnectionError异常
# 如果http返回了不成功的状态码,Response.raise_for_status会抛出一个httperror异常
# 请求超时，会抛出一个Timeout异常
# 若请求超过了设定的最大重定向次数，会抛出一个TooManyRedirects异常
# 所有Requests显示抛出的异常都继承自requests.exception.RequestsException

# 会话对象
    # 跨请求保持一些cookie，用session（）对象
    s = requests.session()
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    r = s.get('http://httpbin.org/cookies')
    print('>>>>Cookies:')
    print(r.text)

    # 会话也可以用来为请求方法提供缺省数据，通过为会话对象的属性提供数据来实现
    s = requests.session()
    s.auth = ('user','pass')
    s.headers.update({'x-test':'True'})
    s.get('http://httpbin.org/headers',headers = {'x-tests':'True'})
    # both x-test and x-test2 are sent
    r = s.get('http://httpbin.org/headers')
    print(r.text)   # 只显示了x-test

# 请求与响应对象
# 执行了 requests.get()的调用，主要在做两件事情
# 1、构建一个request对象，该对象被发送到某个服务器请求或查询一些资源
# 2、一旦requests得到一个从服务器返回的响应就会产生一个response对象
    r = requests.get('http://en.wikipedia.org/wiki/Monty_Python')




















'''
# post 发送数据，则把字典/元组列表传给data参数
def post_requests():
    load  = {'key1':'value1','key2':'value2'}
    # post 一个多部分编码的文件
    files = {'files': open('report.xlsx', 'rb')}
    r = requests.post(url,data=load)
    print('>>>>Response Body:')
    print(r.text)
    r1 = requests.post(url,files=files)
    print('>>>>Response Body:')
    print(r1.text)
'''

if __name__ == '__main__':
    print('>>>>get requests:')
    get_requests()
    # post_requests()
