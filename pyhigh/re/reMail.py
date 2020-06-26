# coding=utf-8
import re


def main():
    '''匹配邮箱'''
    mails = ['4512@163.com','12121212121212A212122@gmail.com','45515@qq.com']
    for mail in mails:
        ret = re.match(r'^[a-zA-Z0-9]{4,20}@(163|gmail|qq)\.com',mail)
        if ret:
            print('邮箱符合要求，邮箱是%s' % ret.group())
        else:
            print('邮箱不符合要求，邮箱是%s' % mail)



if __name__ == '__main__':
    main()