'''
    目标：学习xlrd， xlwt模块
'''
'''
    xlrd：读excel
    xlwt：写excel
    安装xlrd： cmd命令行下执行命令：pip install xlrd
    常用单元格中的数据类型：0.empty(空的)， 1.string（text）， 2.number， 3.date， 4.boolean ， 5.error， 6.blank（空格）
'''
# 导入模块
import xlrd

# 打开excel文件读取数据
data = xlrd.open_workbook(r'C:\Users\yolo\Desktop\studyxlrd.xlsx')  # 文件名以及路径，若文件名或路径中包含中文，前面加一个r，表示原生字符

# 常用的函数就是book和sheet的操作
# 1、获取book中的一个工作表
table = data.sheets()[0]  # 通过索引顺序获取
table1 = data.sheet_by_index(1)  # 通过索引顺序获取
table2 = data.sheet_by_name('信息表')  # 通过名称获取

print(table, table1, table2)  # 以上三个函数都会返回一个xlrd.sheet.Sheet()对象

names = data.sheet_names()  # 返回book中所有工作表的名字
print(names)

data.sheet_loaded(sheet_name_or_index=0)  # 检查某个sheet是否导入完毕
print(data.sheet_loaded(1))  # True
print(data.sheet_loaded('成绩表'))  # True


# 2、行的操作
nrows = table.nrows  # 获取该sheet中的有效行数
line1 = table.row(1)  # 返回由该行（这里是第一行）中所有的单元格对象组成的列表
print(line1)  # [text:'yolo', text:'男', number:21.0]
line0 = table.row_slice(0)  # 返回由该行中所有的单元格对象组成的列表

type = table.row_types(1, start_colx=0, end_colx=2)  # 返回由该行中所有单元格的数据类型组成的列表， 可选参数start_colx, end_colx
print(type)  # array('B', [1, 1, 2])
value = table.row_values(2)  # 返回由该行中所有单元格的数据组成的列表,可选参数start_colx, end_colx
print(value)

len = table.row_len(1)  # 返回该行的有效单元格长度
print(len)


# 3、列的操作
ncols = table.ncols  # 获取sheet表的有效列数
print(ncols)
col0 = table.col(0, start_rowx=0, end_rowx=None)  # 返回由该列中所有的单元格对象组成的列表
print(col0)
col1 = table.col(1, start_rowx=0, end_rowx=None)  # 返回由该列中所有的单元格对象组成的列表

type = table.col_types(0, start_rowx=0, end_rowx=None)  # 返回由该列中所有单元格的数据类型组成的列表
print(type)  # [1, 1, 1]

value = table.col_values(2, start_rowx=0, end_rowx=None)  # 返回由该列中所有单元格的数据类型组成的列表
print(value)  # ['年龄', 21.0, 20.0]


# 4、单元格操作
cell = table.cell(0, 0)  # 返回单元格对象
print(cell)
type = table.cell_type(0, 0)  # 返回单元格数据类型
print(type)
value = table.cell_value(0, 0)  # 返回单元格中的数据
print(value)
# index = table.cell_xf_index(0, 0)  没有搞懂
# # print(index)