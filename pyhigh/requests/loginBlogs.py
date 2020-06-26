# coding=utf-8
import requests
import json

url = 'https://account.cnblogs.com/signin'

headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

s = requests.session()  # 初始化session对象，获得部分cookie

r = s.get(url=url, headers=headers, verify=False)
print(r.cookies)

# 设置cookie
# 获得cookie对象
coo = requests.cookies.RequestsCookieJar()
coo.set('.CNBlogsCookie', 'BD0F49EBBE380C03A5052C1913CE5981DA7E0F49A71018D71BFED7C176AB9DC822ED7992E3A1A9206DB03CD2472E35235387AC77FBBEC18E0088365B68C551062A3D989A2FD5114F6B0AAC3FF7EDD0CD168794B1')
coo.set('.Cnblogs.AspNetCore.Cookies', 'CfDJ8B9DwO68dQFBg9xIizKsC6TBdFhPXV5IAbzVMx3KCbGKZQSyUzgWKBP9skyGs4isxHG9ZLMYaFqk500DfzGHtGX24-cNNKIspDqwDxxWNSejVwsgfxWjQKp8FUtYmX7f7GpiRSSzX_1g1Z4CXksRD-Ot0lugvr259WA7PASAQmB5czLNY2jKWUo_BFnFI5vWQ2oZ7pAmnx3jVQIL1qVDff70ahoCOQMuL_iabK1N5_pNXkdw_IGKtTZiba7y6iEJT-o9oIuSwM_7R6Kcz15DCvBsyUcAz1gVKlavHph92s2myNotZNFhW50BJAmHneoiOXQZnaNE36OaAVYpus6DmiYBXSQ9PRY2dyPxnVtDwsr7YEVFrDvWSw37X0CtXL484x4Ta7ZlOiQS81qUq9Qp_-FS6E6o8I6EE8mPxBcK5ndu-xMI5vPw2LtwjfIa76dPTSfcfShzRy7o5msH-5fo8ip5J3yN1PQo6Likq3km7bPjhinwkNb0-_aB7wTxT5eqRheMunwbFHhjfEZnxR4PUZCYwADf-UWztS4aqGRWRv3wvhYUI2H3_kws2qSUOOIytw')

s.cookies.update(coo)  # 更新服务器端的cookies信息
print(s.cookies)

# url2 = 'https://home.cnblogs.com/ajax/Set/ProfileSubmit'
#
# headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
#            'Content-Type': 'application/x-www-form-urlencoded'}
# data = {'RealName':'YYY', 'Gender':0}
# res = s.post(url=url2, data=data, headers=headers, verify=False)
# print(res.content)
url2= "https://i.cnblogs.com/api/posts"
body = {'title':'555'
        }
bb = json.dumps(body)
r2 = s.post(url2, json=bb, verify=False)
print (r.content)
# url2的请求没有构建成功