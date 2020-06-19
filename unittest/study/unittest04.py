# coding=utf-8
import requests
import unittest

class TestWeather(unittest.TestCase):
    '''测试天气预报接口和登录接口'''

    def setUp(self):
        print('\n case before:')
        pass

    @unittest.skip
    def test_BJ_weather(self):
        '''requests库的使用'''
        url = 'http://www.apiopen.top/weatherApi'
        params = {'city':'北京'}

        res = requests.post(url=url, params=params)
        print('>>>>Response Body:')
        print(res.text)
        result = res.json()['code']  # 获取状态码
        self.assertEqual(200, result)  # 断言
        self.assertIn('msg', res.text)



    def tearDown(self):
        print('\n case after:')
        pass

if __name__ == '__main__':
    '''手动执行测试用例'''
    suite = unittest.TestSuite()

    suite.addTest(TestWeather('test_BJ_weather'))

    runner = unittest.TextTestRunner()

    runner.run(suite)


