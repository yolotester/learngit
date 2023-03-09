#! usr/bin/env python
# -*- coding: utf-8 -*-


# @Time   : 2020/10/27 0:42
# @Author : Yolo
# @Desc   : 
# @File   : 
# @Software:
import os
from Libs.Log_Util import logger


class YOsPath(object):

    def __init__(self):

        """
        os.path.dirname  返回文件路径
        os.path.abspath  返回绝对路径
        __file__   当前脚本运行的路径
        os.path.join  将目录和文件名合成一个路径
        os.path.exists(path)  如果路径存在则返回true
        os.makedirs  创建目录
        os.path.basename(__file__)  返回文件名
        """
        self.current_path = os.path.dirname((os.path.abspath(__file__)))

        self.json_path = os.path.join(self.current_path, 'y_json.py')

        self.test1_path = os.path.join(self.current_path, 'y_test1.py')

        if os.path.exists(self.test1_path):
            logger.info("路径存在，返回true，否则返回false")
            print("y_test1的路径为：{}".format(self.test1_path))
        else:
            os.makedirs(self.test1_path)

        self.file_name = os.path.basename(__file__)


if __name__ == '__main__':

    y = YOsPath()
    print(y.current_path)
    print(y.json_path)
    print(y.file_name)
