'''
    目标:自动化执行测试用例
'''

# 导包  unittest  HtmlTestRunner os time
import unittest, os, time, HTMLTestRunner

# import logging
# logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s ')
# logger = logging.getLogger(__name__)

# 组装测试套件--组装所有测试用例
def all_case():

    # 用例目录
    case_path = os.path.join(os.getcwd() , 'case')
    print(case_path)

    # discover方法
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py',top_level_dir=None)
    print(discover)

    return discover

# 定义html报告存放位置
def html_report_path():

    # 报告目录
    report_path = os.path.join(os.getcwd(), 'report')

    # 定义一个now变量存放时间，使得报告不被覆盖
    now = time.strftime('%y-%m-%d_%H_%M_%S', time.localtime())

    # html报告位置
    html_file_path = os.path.join(report_path, "result"+ now + ".html")

    return html_file_path


# 运行测试套件，生成测试报告
def run_all_case():

    # 打开一个文件，将result写入文件中
    fp = open(html_report_path(), 'wb')

    # HTMLTestRunner.HTMLTestRunner类实例化一个对象
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='接口自动化测试报告', description=u'用例执行情况' ,verbosity=2)

    # 调用runner对象的run方法，参数为discover对象
    runner.run(all_case())

    # 关闭文件
    fp.close()

if __name__ == '__main__':
    run_all_case()
    # logger.info(run_all_case())
