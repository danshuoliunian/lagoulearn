from unittest import TestCase
import unittest
from selenium import webdriver
from time import sleep
from PO.pageObject.one_page import SearchPage


class CaseRun(TestCase):
    def setUp(self):
        path = "/usr/local/bin/chromedriver"
        self.driver = webdriver.Chrome(path)

        sleep(3)
        self.url = "https://cn.bing.com/"

        sleep(3)
        self.content = "墨菲特"

    # 测试步骤
    def test_search(self):
        bing_page = SearchPage(self.driver, self.url)
        bing_page.open()
        sleep(3)
        bing_page.search_content(self.content)
        sleep(3)
        bing_page.btn_click()
        sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
