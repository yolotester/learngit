#! usr/bin/env python
# -*- coding: utf-8 -*-


# @Time   : 2020/10/27 0:42
# @Author : Yolo
# @Desc   : 
# @File   : 
# @Software:
import xlrd
from Libs.Log_Util import logger


class ExcelUtil(object):
    """
    工作薄  sheet页  单元格  行  列
    """

    def __init__(self, filepath, sheet_name=''):
        """
        初始化对象的同时就设置初始值，通过形参传递数据
        :param filepath: excel文件路径
        :param sheet_name: sheet名称
        """
        self.filepath = filepath
        self.sheet_name = sheet_name
        self.xls_wb = xlrd.open_workbook(self.filepath)  # 打开excel文件，文件名以及路径，如果路径或者文件名有中文给前面加一个r原生字符。
        self.xls_ws = self.xls_wb.sheet_names()  # 返回excel中所有sheet的名称
        # print(xls_ws)
        # xls_ws = xls_wb.sheet_by_name(self.sheet_name)  # 通过名称获取sheet
        # xls_ws = xls_wb.sheet_by_index()  # 通过索引顺序获取sheet
        # xls_ws = xls_wb.sheets[0]  # 通过索引顺序获取sheet
        self.xls_wl = self.xls_wb.sheet_loaded(self.sheet_name)  # 检查某个sheet页是否导入完毕, 导入完毕返回True，否则返回False

    def operate_row(self):
        """
        行的操作
        列的操作相同
        xls_ws, valid_rows等都是局部变量，作用域只在该方法内
        :return:
        """
        try:
            xls_ws = self.xls_wb.sheet_by_name(self.sheet_name)
            valid_rows = xls_ws.nrows  # 获得该sheet页中的有效行数
            valid_cols = xls_ws.ncols  # 获得该sheet页中的有效列数
            row_cell_list = xls_ws.row(1)  # 返回由该行中所有的单元格对象组成的列表, 参数为行号
            row_by_col_cell_list = xls_ws.row_slice(1, 1, 3)   # 返回该行中特定列的单元格对象组成的列表，参数依次为 行号  开始列号  结束列号，列号左闭右开
            row_cell_data_type_list = xls_ws.row_types(1, start_colx=0, end_colx=None)  # 返回该行中所有单元格的数据类型组成的列表
            row_cell_data_list = xls_ws.row_values(1, start_colx=0, end_colx=None)  # 返回该行中所有单元格的数据组成的列表
            col_num = xls_ws.row_len(1)  # 返回该行的有效单元格长度，即列数
            return row_cell_data_list

        except Exception as msg:
            logger.error("【Frame】读取文件异常！", msg, exc_info=True)

    def operate_cell(self):
        """
        单元格的操作
        :return:
        """
        try:
            xls_ws = self.xls_wb.sheet_by_name(self.sheet_name)
            cell_object = xls_ws.cell(1, 1)  # 返回单元格对象，参数为行号，列号
            cell_data_type = xls_ws.cell_type(1, 1)  # 返回单元格中的数据类型
            cell_data = xls_ws.cell_value(1, 1)  # 返回单元格中的数据
            return cell_data
        except Exception as msg:
            logger.error("【Frame】读取文件异常！", msg, exc_info=True)

if __name__ == '__main__':
    excel = ExcelUtil(r'C:\Users\yolo\Desktop\Test_Case.xlsx', 'User')
    logger.info(excel.xls_ws)
    row_list = excel.operate_row()
    logger.info(row_list)
    cell_object = excel.operate_cell()
    logger.info(cell_object)

