
import time
import getopt
import sys
from Config.Config import *
from Libs.Log_Util import logger


def choose_api_type(environment):
    '''
    选择和切换api
    :param environment:环境名
    :return:
    '''
    if environment == 'test':
        api_type = 1
    elif environment == 'pre':
        api_type = 2
    elif environment == 'line':
        api_type = 3
    else:
        raise Exception("测试环境与API类型不匹配")

    Config().set_variable_config('Apitype', api_type)


def usage():
    """
    工具帮助
    """
    print("""
    该命令行工具实现功能："接口自动化测试入口脚本"
    脚本运行参数说明：
    -h : 查看帮助   
         如：python main_all.py -u zhangsan -e test -r 1
    -u : 测试执行人
    -e : 指定测试环境 (test、pre、line)
    -r : 指定生成测试报告的类型 (1：HTML模板报告  2：BS模板报告  默认1)
    """)
    time.sleep(3)


def main(argv):
    try:
        report_type = 1  # 测试报告类型
        opts, args = getopt.getopt(argv[1:], "hu:e:r:x")
        for opt_name, opt_value in opts:
            if opt_name == '-h':
                usage()
                exit()
            elif opt_name == '-u':
                account = opt_value.strip()  # 用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
            elif opt_name == '-e':
                environment = opt_value.strip()
            elif opt_name == '-r':
                report_type = int(opt_value.strip())

        if account and environment:
            logger.info('当前执行的环境：【%s】  当前执行的用户：【%s】' % (environment, account))

        else:
            logger.error('无法执行：可能是缺少必需的运行参数，请参考帮助信息 -h')

    except getopt.GetoptError as e:
        logger.error("参数错误：{}， 请参考帮助信息 -h".format(e))
    except NameError as e:
        logger.error("运行出错：{}  可能是缺少必需的运行参数，请参考帮助信息 -h".format(e))
    finally:
        exit()



if __name__=='__main__':
    if len(sys.argv) == 1:
        usage()
        sys.argv.append('-u yolo')
        sys.argv.append('-e test')
        sys.argv.append('-r 1')
    main(sys.argv)



