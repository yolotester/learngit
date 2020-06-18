import unittest
import requests
import json
import os

class TestIF(unittest.TestCase):
    '''继承于unittest.TestCase类'''

    url = 'http://httpbin.org'

    def build_url(self, endpoint):
        return '/'.join([self.url,endpoint])

    def setUp(self):
        print('\n case before:')
        pass


    def test_have_data_post_request(self):
        '''测试带数据的post请求'''
        data = dict(key1 = 'Value1',key2 = 'Value2')
        res = requests.post(url=self.build_url('post'), data=data)
        print('>>>>have data:')
        js = res.json()
        self.assertEqual(js['form']['key1'], 'Value1')


    def test_have_headers_post_request(self):
        '''测试带请求头的post请求'''
        headers = {'user-agent':'test-user-agent'}
        res = requests.post(url=self.build_url('post'), headers=headers)
        print('>>>>have headers:')
        js = res.json()
        self.assertEqual(js['headers']['User-Agent'], 'test-user-agent')


    def tearDown(self):
        print('\ncase after')
        pass


if __name__ == '__main__':
    # 设置执行用例的目录
    test_dir = os.path.join(os.getcwd())

    #　自动搜索指定目录下的ｃａｓｅ，构造用例集，执行顺序是ＡＳＣＩＩ码的顺序
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

    # 实例化TextTestRunner类
    runner = unittest.TextTestRunner()

    #　使用ｒｕｎ（）方法执行测试套件,执行套件中的所有用例
    runner.run(discover)
