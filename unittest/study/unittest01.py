import  HTMLTestRunner
import unittest
import requests
import time
import json

# 必须继承unittest.TestCase类
class TestInterface(unittest.TestCase):

    url = 'http://httpbin.org'

    def build_url(self,endpoint):
        return '/'.join([self.url,endpoint])

# 定义setUp（）方法
    def setUp(self):
        print('\n case before')


# 定义测试用例，assert断言测试结果
    def test_no_params_get_request(self):
        '''测试不带参数的get请求'''
        res = requests.get(url=self.build_url('get'))
        print('>>>>no_params:')
        self.assertEqual(res.status_code, 200)


    def test_have_params_get_request(self):
        '''测试带参数的get请求'''
        params = dict(show_env = "11", yolo = '22')
        res = requests.get(url=self.build_url('get'), params=params)
        js = res.json()
        print(js)
        print('>>>>have_params:')
        self.assertEqual(js['args']['yolo'],'22')


# 定义tearDown（）方法
    def tearDown(self):
        time.sleep(1)
        print('\n case after')




if __name__ == '__main__':
    #　unittest.main()　单个用例的执行
    #　手动执行测试用例集
    #　构造用例集
    suite = unittest.TestSuite()

    # 执行顺序按加载顺序：先执行test_have_params_get_request, 再执行test_no_params_get_request
    suite.addTest(TestInterface('test_have_params_get_request'))
    suite.addTest(TestInterface('test_no_params_get_request'))

    # 实例化runner类
    runner = unittest.TextTestRunner()

    # 执行测试用例
    runner.run(suite)