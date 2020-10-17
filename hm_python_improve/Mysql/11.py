# coding:utf-8
import requests
 # 先打开登录首页，获取部分cookie
url = "https://passport.cnblogs.com/user/signin"
headers = {
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
          }  # get方法其它加个ser-Agent就可以了
s = requests.session()
r = s.get(url, headers=headers,verify=False)
print (s.cookies)
 # 添加登录需要的两个cookie
c = requests.cookies.RequestsCookieJar()
c.set('.CNBlogsCookie', 'XXX')  # 填上面抓包内容
c.set('.Cnblogs.AspNetCore.Cookies','XXX')  # 填上面抓包内容
c.set('AlwaysCreateItemsAsActive',"True")
c.set('AdminCookieAlwaysExpandAdvanced',"True")
s.cookies.update(c)
print (s.cookies)
result = r.content
print(result.decode('utf-8'))
# 登录成功后保存编辑内容
url2= "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body = {"__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR":"FE27D343",
      "Editor$Edit$txbTitle":"这是绕过登录的标题：北京-宏哥",
      "Editor$Edit$EditorBody":"<p>这里是中文内容：http://www.cnblogs.com/duhong/</p>",
       "Editor$Edit$Advanced$ckbPublished":"on",
     "Editor$Edit$Advanced$chkDisplayHomePage":"on",
        "Editor$Edit$Advanced$chkComments":"on",
        "Editor$Edit$Advanced$chkMainSyndication":"on",
       "Editor$Edit$lkbDraft":"存为草稿",
        }
r2 = s.post(url2, data=body, verify=False)
print (r.content.decode('utf-8'))

# 第三步：正则提取需要的参数值
import re
postid = re.findall(r"postid=(.+?)&", r2.url)
print(type(postid))
print (postid) # 这里是 list
# 提取为字符串
print (postid[0])
# 第四步：删除草稿箱
url3 = "https://i.cnblogs.com/post/delete"
json3 = {"postId": postid[0]}
r3 = s.post(url3, json=json3, verify=False)
result = r3.content #content数据是字节输出
print(type(result))
print(result)
#json是经过加码encode成对应python的数据类型
result1 = r3.json()
print (type(result1))
print(result1['isSuccess'])