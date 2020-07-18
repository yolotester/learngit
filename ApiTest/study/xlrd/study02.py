'''
    目标：对输入的用户名和密码进行参数化，这些数据读取自excel中
'''

import xlrd, unittest

class Data_From_Excel(object):
    '''
        封装在Data_From_Excel类中方便后面使用
    '''
    file_addr = r'C:\Users\yolo\Desktop\studyxlrd.xlsx'
    # 打开excel文件
    def open_excel(self, file=file_addr):
        '''
        :param file: 文件名或者路径
        :return: xlrd.book.Book（）对象
        '''
        try:  # 检验文件有没有被获取到
            self.data = xlrd.open_workbook(file)
            return self.data
        except Exception as e:
            print(file)
            print('打开文件错误')
            print(e)  # [Errno 2] No such file or directory: 'C:\\Users\\yolo\\Desktop\\studyxrd.xlsx'

    # 获取文件中sheet表
    def get_sheet_by_name(self, sheet, colnumindex=0):

        # 获取excel数据
        self.data = self.open_excel()

        # 通过sheet_by_name获取sheet页名叫信息表的sheet对象数据
        self.table = self.data.sheet_by_name(sheet)

        # 获取excel中第一行的所有的数据值,主要是为了后面用len（self.rownames）获得列数
        self.colnums = self.table.row_values(colnumindex)

        # 获得所有的有效行数
        self.nrows = self.table.nrows

        list = []  # 将excel中每一行数据当做列表中的一个元素（以字典的形式）

        # 循环有数据的行数
        for row_line in range(1, self.nrows):
            row_value = self.table.row_values(row_line)  # 获取所有行数每一行的数据
            if row_value:
                app = {}
                for i in range(len(self.colnums)):
                    app[self.colnums[i]] = row_value[i]

                list.append(app)

        print(list)
        return list

    #


if __name__ == '__main__':
    Data_From_Excel().get_sheet_by_name('信息表')

