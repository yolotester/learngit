 # coding:utf-8
import requests
# 先打开登录首页，获取部分session
url = "http://localhost:8080/jenkins/j_acegi_security_check"
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
         }  # get方法其它加个ser-Agent就可以了
d = {"j_username": "admin",
  "j_password": "aaaa2222",
    "from": "/",
     "Submit": u"登录",
    "remember_me": "on"
    }
s = requests.session()
r = s.post(url=url, headers=headers, data=d)
print(r.content)
 #print (r.content.decode('utf-8'))
# 正则表达式提取账号和登录按钮
import re
t = re.findall(r'<b>(.+？)</b>', r.content.decode('utf-8'))   # 用python3的这里r.content需要解码
print(t[0])
print(t[1])