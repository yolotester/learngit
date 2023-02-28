#! usr/bin/env python
# -*- coding: utf-8 -*-


# @Time   : 2020/10/27 0:42
# @Author : Yolo
# @Desc   : 
# @File   : 
# @Software:
import os

class Y_OS(object):

    def __init__(self):

        '''
        os.path.dirname  返回文件路径
        os.path.abspath  返回绝对路径
        __file__   当前脚本运行的路径
        os.path.join  将目录和文件名合成一个路径
        os.path.exists(path)  如果路径存在则返回true
        os.makedirs  创建目录
        '''
        self.current_path = os.path.dirname((os.path.abspath(__file__)))

        self.json_path = os.path.join(self.current_path, 'y_json.py')

        self.test1_path = os.path.join(self.current_path, 'y_test1.py')

        if os.path.exists(self.test1_path):
            print("路径存在，返回true")
        else:
            os.makedirs(self.test1_path)


y = Y_OS()
print(y.current_path)
print(y.json_path)