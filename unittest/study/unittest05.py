# coding=utf-8
import requests
import unittest,os

class Test_Blog_Login(unittest.TestCase):
    '''测试开源api的登录接口'''

    def setUp(self):
        print('\n case before:')
        pass

    def login(self, key, username, psd):
        '''三个参数，apikey，username， passwd'''
        url = 'https://api.apiopen.top/loginUser'
        params = {'apikey':key,
                  'name':username,
                  'passwd':psd
                  }
        res = requests.post(url=url,data=params)
        print(res.text)
        return res

    @unittest.skip
    def test_success_login(self):
        '''成功案例'''
        key = 'd0058f79caae5300dcba65f128e52855'
        username = 'peakchao'
        psd = '123456'

        result = self.login(key, username, psd)
        js = result.json()
        self.assertEqual(200, js['code'])
        print('接口不通')




    def tearDown(self):
        print('\n case after:')
        pass


if __name__ == '__main__':
    '''自动执行测试用例'''
    case_path = os.path.join(os.getcwd())

    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py', top_level_dir=None)

    runner = unittest.TextTestRunner()

    runner.run(discover)
