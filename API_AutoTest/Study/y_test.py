#! usr/bin/env python
# -*- coding: utf-8 -*-


# @Time   : 2020/10/27 0:42
# @Author : Yolo
# @Desc   : 
# @File   : 
# @Software:

# Config模块里使用了import configparser，然后在其他模块导入Config模块，可以直接使用configparser模块
from Config.Config import *

config = configparser.ConfigParser()

print(config)

