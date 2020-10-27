# encoding=gbk
# https://github.com/psf/requests
# http://httpbin.org/
'''
import requests
URL_ip = 'http://httpbin.org/ip'  # �����������վIP�ӿ�
URL_get = 'http://httpbin.org/get'  # �����������

#  Get ����
def use_simple_requests():

    response = requests.get(URL_ip)
    print('>>>>Response Headers:')
    print(response.headers)
    print('>>>>Response Body:')
    print(response.text)

def use_params_requests():
    params = {'params1':'hello','params2':['world','world']}
    response = requests.get(URL_get,params=params)
    print('>>>>Encoding:')         # �����ʽ
    print(response.encoding)
    print('>>>>Request URL:')      # �����������url
    print(response.url)
    print('>>>>Content:')          # �ı�����
    print(response.content)
    print('>>>>Response Headers:')   # ��Ӧͷ
    print(response.headers)
    print('>>>>Status Code:')        #״̬��
    print(response.status_code)
    print(response.reason)           # ״̬���������
    print('>>>>Response Body:')      # ��Ӧ��
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
    # user ��������ʾ���ǵ�ǰ�û�
    response = requests.get(build_url('user/emails'),auth = ('yolotester','Yolo114963'))
    #print(response.text)
    print(better_print(response.text))

# ʹ��params�������ʹ�����������
def params_methond():
    r = requests.get(build_url('users'),params={'since':'11'})
    print(better_print(r.text))
    print(r.request.headers)
    print(r.url)

# patch�����޸�
def json_request():
    #r = requests.patch(build_url('user'),auth = ('yolotester','Yolo114963'),json = {'name':'yolotester1'})
    r = requests.post(build_url('user/emails'),auth=('yolotester','Yolo114963'),json=['ying31@github.com'])
    print(better_print(r.text))
    print(r.request.headers)
    print()
    print(r.request.body)
    print(r.status_code)

# ��ʱ�쳣/HTTPError�쳣
def timeout_request():
    try:
        response = requests.get(build_url('user/emails'),timeout = 10)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print('��ʱ��' + str(e))
    except exceptions.HTTPError as e:
        print('������' + str(e))
    else:
        print(better_print(response.text))
        print(response.status_code)

# session ������Ҫ��׼������(���Զ�������)��Ȼ�������󣬻����Ӧ
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

# Response����ķ�����status_code ,reason,headers,url,history,elapsed(�õ���Ӧ�����ĵ�ʱ��)
# encoding,content,text,json(��ת�����ֵ�)
def response_request():
    response = requests.get('https://api.github.com')
    print(response.elapsed)
    print(response.json())
    print(response.json()['emails_url'])
    print(response.encoding)

# ����ͼƬ/�ļ����裺ģ�����������-������request��Ϣ-����ȡ������-��д���ļ�
def download_img():
    url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1587156066192&di=66cc0fdb9bdde55d479dea59a5550e9a&imgtype=0&src=http%3A%2F%2Fww1.sinaimg.cn%2Flarge%2F006tNbRwgy1fdnex0ogd5j31jk0ih74t.jpg'
    # α��headers��Ϣ
    headers = {'user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    # ����request����
    response = requests.get(url,headers= headers,stream =True)


    print(response.status_code,response.reason)
    # �������Ĺ���ķ�ʽ������������������Ϻ��Զ��ر���
    # from contextlib import closing
    # with closing(requests.get(url,headers= headers,stream =True)) as response:
    with open('demo1.jpg','wb') as fd:
        # ��ȡ������
        for each in response.iter_content(128):
            # д���ļ�
            fd.write(each)

# �¼����� event hooks�������Դ���ķ�ʽ
# io����-��������-���õ���Ӧ��ֱ�ӽ���ص�����
def get_key_info(response,*args,**kwargs):
    '''
    �ص�����
    :return:
    '''
    print(response.headers['content-type'])

def main():
    requests.get('https://www.baidu.com',hooks = dict(response = get_key_info))

# http��֤  ������֤��auth����
Base_url = 'https://api.github.com'
def build_url(end_point):
    return  '/'.join([Base_url,end_point])
def basic_auth():
    '''
    ������֤
    :return:
    '''

    response = requests.get(build_url('user'),auth = ('yolotester','Yolo114963'))
    print(response.text)
    print(response.request.headers)
    print(response.request.headers['authorization'])  # ��ͨ��base64.b64decode()������������������ҵ��û���������

# oauth ��֤  token
def basic_oauth():
    # �ѻ��tokenֵ������token ��֤
    headers = {'Authorization':'token 0ad9de577e29a9e848612fd972f7adecda3fba44'}
    # '/user/emails'
    response = requests.get(build_url('user/emails'),headers=headers)
    print(response.text)
    print(response.request.headers)
    print(response.status_code,response.reason)

# auth ��֤��
from requests.auth import AuthBase
class Githubauth(AuthBase):
    def __init__(self,token):
        self.token = token
        # ��װ����
    def __call__(self, req):
        # requests add headers
        req.headers['Authorization'] = ' '.join(['token',self.token])
        return req
def auth_advanced():
    auth = Githubauth('0ad9de577e29a9e848612fd972f7adecda3fba44')
    response = requests.get(build_url('user/emails'),auth = auth)
    print(response.text)

# proxy ������Ҫ���ܣ�ת������  �������������heroku������-��������1080�˿�����socks����-��������ת����1080�˿�-����ȡ��Ӧ��Դ
# def proxy_request():
#     proxies = {'http':'socks5://127.0.0.1:1080','https:':'socks5://127.0.0.1:1080'}
#     response = requests.get('https://www.facebook.com',timeout = 10,proxies = proxies)
#     print(response.text)

# Session �� Cookie


if __name__ == '__main__':
    request_methond()