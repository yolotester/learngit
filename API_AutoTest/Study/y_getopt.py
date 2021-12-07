#! usr/bin/env python
# -*- coding: utf-8 -*-


# @Time   : 2020/11/5 3:42
# @Author : Yolo
# @Desc   : getopt_study
# @File   : y_getopt.py
# @Software: PyCharm

# https://www.jianshu.com/p/a877e5b46b2d
import getopt
import sys
print(getopt.__doc__)


def getopt_func():

    opts, args = getopt.getopt(sys.argv[1:], '-h-f:-v', ['help','filename=','version'])  # 返回结果是两列表的元组
    for opt_name, opt_value in opts:
        if opt_name in ('-h', '--help'):
            print("[*] help info")
            exit()
        if opt_name in ('-v', '--version'):
            print('[*] version is 0.01')
            exit()
        if opt_name in ('-f', '--filename'):
            fileName = opt_value
            print("[*] Filename is ", fileName)
            # do something
            exit()



if __name__=="__main__":
    getopt_func()