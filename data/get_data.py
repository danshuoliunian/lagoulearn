# coding:utf-8

from testDemo.test_Excel import OperationExcel
from data.data_config import *
from testDemo.operation_json import OperationJson


class GetData:
    def __int__(self):
        self.opera_excel = OperationExcel()

    # case个数
    def get_case_lines(self):
        return self.opera_excel.get_lies()

    def get_is_run(self, raw):

        flag = None
        col = int(data_config.get_run())
        return self.opera_excel.get_cell_value(raw, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def is_header(self, row):
        col = int(data_config.get_header())
        header = self.opera_excel.get_cell_value(row, col)
        if header == 'yes':
            return data_config.get_header_value()
        else:
            return None

    # 获取请求方式
    def get_request_Method(self, row):
        col = int(data_config.get_run_way())
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    def get_request_url(self, row):
        col = int(data_config.get_url())
        url = self.opera_excel.get_cell_value(row, col)
        return url

    def get_request_data(self, row):
        col = int(data_config.get_data())
        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data

    # 通过获取关键字拿到data数据
    def get_data_for_json(self):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    # 获取预期结果
    def get_expect_data(self, row):
        col = int(data_config.get_expect())
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect
