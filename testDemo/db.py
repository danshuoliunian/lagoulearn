# coding：utf-8

# 操作数据库

import pymysql


class DB:
    def __int__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            post=3306,
            user='root',
            passwd='123456',
            db='api_test'
        )
        self.cur = self.conn.cursor()

    # 析构函数，实力删除时触发
    def __del__(self):
        self.cur.close()
        self.conn.close()

    def query(self, sql):
        self.cur.execute(sql)
        self.conn.commit()

    def exec(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def check_user(self):
        result = self.query("select * from user where name = '{}'".format(name))
        return True if result else False

    def del_user(self):
        self.exec("delete from user where name='{}'".format(name))


"""
from db import DB:

db = DB()  # 实例化一个数据库操作对象
if db.check_user("张三"):
    db.del_user("张三")
"""
