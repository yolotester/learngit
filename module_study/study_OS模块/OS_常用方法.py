import os
import time

class MyOsPath(object):

    # 1-返回绝对路径 -- D:\Git\learngit\module_study\study_OS模块\OS_常用方法.py
    current_path = os.path.abspath(__file__)

    # 2-返回文件路径 -- D:\Git\learngit\module_study\study_OS模块
    file_file_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # D:\Git\learngit\module_study

    # 3-把目录和文件合并在一起  -- D:\Git\learngit\module_study\study_配置文件
    config_file_path = os.path.join(current_path, 'study_配置文件')
    var_config_path = os.path.join(config_file_path, 'var_config.ini')

    # 4-返回文件名  -- OS_常用方法.py
    return_file_name = os.path.basename(__file__)

    # 5-把路径分割成 dirname 和 basename，返回一个元组  -- ('D:/Git/learngit/module_study/study_OS模块', 'OS_常用方法.py')
    split_path = os.path.split(__file__)

    # 6-返回文件大小，如果文件不存在就返回错误 -- 1251字节
    file_size = os.path.getsize(__file__)

    # 7-判断 -- 是否是目录，如果是目录则返回真，否则返回假
    check_dir = os.path.isdir('test')

    def about_file_info(self):
        '''关于文件的相关信息方法'''

        file = 'D:\Git\learngit\module_study\study_OS模块\OS_常用方法.py'  # 文件路径

        print(os.path.getatime(file))  # 输出文件最近访问时间
        print(os.path.getctime(file))  # 输出文件创建时间
        print(os.path.getmtime(file))  # 输出最近修改时间
        print(time.gmtime(os.path.getmtime(file)))  # 以struct_time形式输出最近修改时间
        print(os.path.getsize(file))  # 输出文件大小（字节为单位）
        print(os.path.abspath(file))  # 输出绝对路径
        print(os.path.normpath(file))  # 规范path字符串形式



if __name__=="__main__":

    print(MyOsPath.config_file_path)
    print(MyOsPath.return_file_name)
    print(MyOsPath.split_path)
    print(MyOsPath.file_size)
    MyOsPath().about_file_info()
    print(MyOsPath.check_dir)