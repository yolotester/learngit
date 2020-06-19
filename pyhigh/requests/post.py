import requests
import json

url = 'http://httpbin.org'

def build_url(endpoint):
    return '/'.join([url,endpoint])


def have_data_post_request():
    '''带数据的post请求'''
    data = {'key1':"value1", 'key2':'value2'}
    res = requests.post(build_url('post'), data=data)
    print(res.text)
    print(res.url)

def have_header_post_request():
    '''构造请求头中的数据'''
    headers = {'user-agent':'test request headers'}
    res = requests.post(url=build_url('post'),headers = headers)
    print(res.text)
    js = res.json()
    print(js['headers']['User-Agent'])
    print(res.request.headers)

def have_json_post_request():
    '''构造json数据'''
    json = {
        'site':[
            {'name':'google', 'url':'https://www.google.com'}
        ]
    }
    res = requests.post(url=build_url('post'), json=json)
    print(res.text)
    js = res.json()
    print(js['json']['site'])


def hava_params_post_request():
    '''带参数的post请求'''
    params = {'yolo':'111'}
    res = requests.post(url=build_url('post'), params= params)
    print(res.text)

def upload_file_post_request():
    '''上传普通文件'''
    files= {'file':open(r'C:\Users\yolo\Desktop\111.txt','rb')}
    res = requests.post(url=build_url('post'), files= files)
    print(res.text)

def special_file_post_request():
    '''定制化上传文件'''
    # 自定义文件名 文件类型
    files = {
        'file':('test.png',open(r'D:\photo\down.jpg', 'rb'),'image/png')
    }
    res = requests.post(url=build_url('post'), files=files)
    print(res.text)

def multi_file_post_request():
    '''多文件上传'''
    files = {
        'file1':open(r'C:\Users\yolo\Desktop\111.txt','rb'),
        'file2':('test.png',open(r'D:\photo\down.jpg', 'rb'),'image/png')
    }
    res = requests.post(url=build_url('post'), files=files)
    print(res.text)

def stream_upload_post_request():
    '''流式上传'''
    with open(r'C:\Users\yolo\Desktop\111.txt','rb') as f:
        r = requests.post(url=build_url('post'),data=f)
    print(r.text)
    if r.status_code == 200:
        print('>>>>>>test pass')
    else:
        print('>>>>>>test false')


if __name__ == '__main__':
    #have_data_post_request()
    #　have_json_post_request()
    # hava_params_post_request()
    # upload_file_post_request()
    #　special_file_post_request()
    #　multi_file_post_request()
    # stream_upload_post_request()
    have_header_post_request()