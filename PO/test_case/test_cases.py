import unittest
from selenium import webdriver
from PO.pageObject.search_page import SearchPage
from time import sleep
from ddt import ddt, data, unpack


@ddt
class TestCases(unittest.TestCase):

    # 前置条件
    def setUp(self) -> None:
        path = "/usr/local/bin/chromedriver"
        driver = webdriver.Chrome(path)

        driver.maximize_window()
        self.sp = SearchPage(driver)

    # 后置条件
    def tearDown(self) -> None:
        self.sp.quit_browaser()

    @data(['http://www.baidu.com', '光头强'], ['http://www.baidu.com', '阳光'])
    @unpack
    def test_1(self, url, input_text):
        sp.check(url, input_text)
        sleep(3)
        self.assertEqual(self.sp.get_title(), '百度一下，你就知道', msg='1234')


if __name__ == '__main__':
    unittest.main()
