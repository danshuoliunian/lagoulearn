# coding=utf-8

import xlrd

"""
data = xlrd.open_workbook('/Users/wangzhuohui/Documents/testExcel.xlsx')
tables = data.sheets()[0]
print (tables.nrows) #打印exce中的行数
print(tables.cell_value(2, 3)) 
"""


class OperationExcel:
    def __int__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id

        else:
            self.file_name = '/Users/wangzhuohui/Documents/testExcel.xlsx'
            self.sheet_id = 0

        self.data = self.get_data()

    # 获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某一单元格的内容
    def get_cell_value(self, row, col):
        return self.data.cell_valuse(row, col)


if __name__ == '__main__':
    opers = OperationExcel()
    print(opers.get_cell_vaue(1, 2))
