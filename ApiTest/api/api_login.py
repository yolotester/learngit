# coding = utf-8
'''
    目标：实现登录接口对象封装
'''
# 导包 requests
import requests


class Api_Login(object):

    def __init__(self):
        self.session = requests.session()

    def api_post_login(self, url, user, pwd):

        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        # url = 'http://localhost:8080/j_acegi_security_check'
        data = {'j_username':user,
                'j_password':pwd,
                'from':'/',
                'Submit':u'登录'}

        # 获得部分session
       #  s = requests.session()

        return self.session.post(url, headers=headers,data=data)

    def close(self):
        self.session.close()

'''
    提示：url， user， pwd 后面从data文件读取出来，做参数化使用，我们动态传参
'''


