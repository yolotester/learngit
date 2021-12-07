# coding=utf-8
'''
    目标：完成登录业务层实现,unittest框架
'''
# 导包 unittest  api_login
import unittest
from api.api_login import Api_Login
import os
from parameterized import parameterized
from tools.read_json import Read_Json

# 读取数据的函数
def get_data_from_json():
    data = Read_Json("/login.json").read_json()

    # 新建空列表，添加读取json数据
    arrs = []

    # 使用字典的get方法好处是：获取不到键对应的值时不会报错
    arrs.append((data.get("url"),
                 data.get("user"),
                 data.get("pwd"),
                 data.get("expect_result"),
                 data.get("status_code"))
                )
    return  arrs


# 新建测试类必须继承unittest.Testcase类
class Test_Login(unittest.TestCase):

    # 初始化工作，可以pass不写
    def setUp(self):
        print('\n case before:')
        self.apiLogin = Api_Login()
        super().setUp()

# 新建测试方法
    @parameterized.expand(get_data_from_json())
    def test_login(self, url, user, pwd, expect_result, status_code):

        # 暂时存放数据 url， user ，pwd
        # url = 'http://localhost:8080/j_acegi_security_check'
        # user = 'admin'
        # pwd = 'aaaa2222'

        # 调用登录方法，Api_Login()意为：实例化一个对象
        s = self.apiLogin.api_post_login(url, user ,pwd)
        #print(s.content)
        print('查看响应结果：')
        print(s.text)
        print('test22222222222222222222----------------------------------')

        # 断言 状态码
        self.assertEqual(status_code, s.status_code)
        print('3333333')

        # 断言html页面含有admin
        import re
        r = re.findall(r'<span class="hidden-xs hidden-sm">([a-z]{5})</span>', s.text)
        print(r)

    # 数据的清理工作
    def tearDown(self):
        print('\n case after:')
        self.apiLogin.close()


if __name__ == '__main__':

    # 单个测试用例的执行
    unittest.main()

    # 手动执行测试用例
    # suite = unittest.TestSuite()  # 创建一个测试集对象
    #
    # suite.addTest(Test_Login('test_login'))  # 调用测试集对象的addTest（）方法，添加用例
    #
    # runner = unittest.TextTestRunner()  # 实例化一个TTR对象
    #
    # runner.run(suite)  #　调用ＴＴＲ对象的ｒｕｎ方法，参数为测试集对象

    # 自动执行测试用例，以ASCII码值排序
    # case_path = os.path.join(os.getcwd())
    #
    # discover = unittest.defaultTestLoader.discover(start_dir=case_path, pattern='test.*', top_level_dir=None)
    #
    # runner = unittest.TextTestRunner()
    #
    # runner.run(discover)
