import os

class MyOs(object):

    # 1-获取当前目录
    current_dir = os.getcwd()

    # 2-重命名文件
    def rename_remove_file(self):
        # os.rename("README", "readme")
        # os.remove('readme')
        pass

    def about_dir(self):

        # 1-查看目录列表
        self.list_dir = os.listdir()

        # 2-删除目录
        # os.rmdir('test')

        # 3-创建目录
        # os.mkdir('test')

        # 4-修改工作目录
        os.chdir("test")

        return self.list_dir


if __name__=="__main__":
    print(MyOs.current_dir)
    MyOs().rename_remove_file()
    print(MyOs().about_dir())