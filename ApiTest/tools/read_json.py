import json

# 打开json文件获取文件流
# with open("../data/login.json", 'r', encoding='utf-8') as f:
#
# # 调用load方法加载文件流
#     data = json.load(f)
#     print('获取的数据', data)

# 进行封装
# def read_json():
#     with open("../data/login.json", 'r', encoding='utf-8') as f:
#         return json.load(f)


# 使用参数替换静态文件名
class Read_Json(object):

    # 初始化获得文件路径
    def __init__(self, filename):
        self.file_path = "../data" + filename

    def read_json(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return json.load(f)


'''
    问题：
        未经过封装无法在别的模块内使用
        有多个json文件，如果写死，则不能读取别的文件
        预期数据格式为列表嵌套元祖，[(user, pwd),(..)], 目前返回的是字典
        
    解决方法：  进行封装
                使用参数替换静态文件名
                读取字典里的内容，并添加到新的列表中
'''
if __name__ == '__main__':

    data = Read_Json("/login.json").read_json()

    # 新建空列表，添加读取json数据
    arrs = []

    # 使用字典的get方法好处是：获取不到键对应的值时不会报错
    arrs.append((data.get("url"),
                 data.get("user"),
                 data.get("pwd"),
                 data.get("expect_result"),
                 data.get("status_code"))
                )

    print(arrs)