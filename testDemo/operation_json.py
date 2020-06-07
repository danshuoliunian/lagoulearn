# coding:utf-8
import json

"""
fp = open("/Users/wangzhuohui/Documents/login.json")
data = json.load(fp)
print(data['login'])
"""


class OperationJson:

    def __int__(self):
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open("/Users/wangzhuohui/Documents/login.json") as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取数据
    def get_data(self, id):
        self.data[id]


if __name__ == '__main__':
    opjson = OperationJsonta('login')
