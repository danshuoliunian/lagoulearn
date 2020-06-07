import unittest
import time
from selenium import webdriver
from baidu.utils.excel_read import ParseExcel
import ddt

excel_Path = './../data_mange/test_data.xls'
sheetName = 'data_sou'
excel = ParseExcel(excel_Path, sheetName)


@ddt
class Test_baidu_Search(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # path = "/usr/local/bin/chromedriver"
        self.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(self) -> None:
        self.driver.quit()

    def setUp(self) -> None:
        self.driver.get("https://www.baidu.com/")

    def tearDown(self) -> None:
        pass

    @ddt.data(*excel.getDataFromSheet())
    def test_sou(self, data):
        self.driver.find_element_by_id('kw').send_keys('data')
        time.sleep(3)
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        self.assertEqual('思课帮_' + data, self.driver.title)


if __name__ == '__main__':
    unittest.main()
