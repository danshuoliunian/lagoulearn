# coding:utf-8

import unittest


# 当前模块执行前只执行一次
def setUpModule():
    print('===== setUpModule() ====')


# 当前模块执行后只执行一次
def tearDownModule():
    print('===== tearDownModule() ====')


class TestClass1(unittest.TestCase):

    @classmethod
    # 声明为类方法（必须）
    def setUpClass(cls) -> None:
        # 类方法，注意后面是cls，整个类只执行一次
        print('--- setUpClass ---')

    @classmethod
    # 声明为类方法（必须）
    def tearDownClass(cls) -> None:
        print('--- tearDownClass ---')

    def setUp(self) -> None:
        print('...setUp...')

    def tearDown(self) -> None:
        print('...tearDown...')

    def test_a(self):  # 该模块另一个测试类
        print('case_a')

    def test_b(self):
        print('test_b')


class TestClass2(unittest.TestCase):  # 该模块另一个测试类
    def test_B(self):
        print('B')


if __name__ == '__main__':
    unittest.main()
