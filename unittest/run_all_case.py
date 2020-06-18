# -*- coding:utf-8 -*-
import unittest
import os
import HTMLTestRunner
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# HTMLTestRunner缺点：1、如果中间中断执行，已经执行完的用例结果不会打印到html文件  2、在用例上加了@unittest.skip，此用例也会被执行


def all_case():
    # 用例路径
    case_path = os.path.join(os.getcwd(), 'study')
    print(case_path)

    print(case_path)

    discover = unittest.defaultTestLoader.discover(case_path, pattern="unittest*.py", top_level_dir=None)

    print(discover)
    return discover

def new_report(test_report):
    '''获得最新的测试报告'''
    lists = os.listdir(test_report)  # 列出目录下的所有文件和文件夹保存到lists变量

    # 列表的sort方法， 按时间排序
    lists.sort(key=lambda fn: os.path.getmtime(test_report + '\\' + fn))

    file_new = os.path.join(test_report, lists[-1] )
    print(file_new)
    return file_new

def send_mail(file_new):
    '''发送文件'''
    # 读取文件
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    # 必要参数
    username = '1085953194@qq.com'  # 发件箱用户名
    password = 'nujqkpekapephbic'  # smtp邮件  qq发件箱的授权码
    sender = '1085953194@qq.com'  # 发件人邮箱
    receiver = '3131677992@qq.com'  # 收件人邮箱

    # 邮件正文是MIMEText类型
    msg = MIMEText(mail_body, 'html', 'utf-8')
    print(msg)

    # 邮件对象
    msg['Subject'] = Header('接口测试报告', 'utf-8').encode()
    msg['From'] = Header(u'测试人员<%s>' % sender)
    msg['To'] = Header(u'测试负责人<%s>' % receiver)
    msg['Date'] = time.strftime('%a,%d %b %Y %H:%M:%S %z')

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect('mail.qq.com')  # 连接邮箱服务器
    smtp.ehlo()
    smtp.starttls()
    smtp.login(username, password)  # 登录邮箱服务器
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送者和接收者
    smtp.quit()
    print('邮件已发出！请查收')


if __name__ == '__main__':
    # 报告存放路径
    report_path = os.path.join(os.getcwd(), 'report')
    print(report_path)

    # 1、获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

    # 2、html报告文件路径
    report_abspath = os.path.join(report_path, "result_"+now+".html")
    print('1111')

    # 3、打开一个文件，将result写入此file中
    fp = open(report_abspath, "wb")
    print('2222')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'接口自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：',
                                           verbosity=2)
    # 4、调用all_case函数返回值
    runner.run(all_case())
    fp.close()

    # 测试报告文件夹
    # test_path = 'D:\\Git\\learngit\\unittest\\report\\'
    # new_report = new_report(test_path)
    # send_mail(new_report)
