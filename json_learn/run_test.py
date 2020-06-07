"""
import unittest
import ddt
from selenium import webdriver
import time
@ddt.ddt
class DoubanTest(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.driver = webdriver.Chrome()

    @classmethod
    def terarDownClass(self) -> None:
        self.driver.quit()

    def setUp(self) -> None:
        self.driver.get("https://www.baidu.com/")
    def tearDown(self) -> None:
        pass

    @ddt.file_data('data.json')
    @ddt.unpack
    def test_baidu(self,value):
        flagDict = {0:'red',1:'00FF00'}
        self.driver.get()
        testdata,expectdata = tuple(value.strip().split("||"))
        time.sleep(3)
        try:
            start = time.time()
            startTime = time.strftime()
            can,yu = value.split('||')
        # print(can,yu)
             time.sleep(3)
             self.driver.find_element_by_id('kw').send_keys(can)
             time.sleep(3)
             self.driver.find_element_by_id('su').click()
             time.sleep(3)
             self.assertEqual(yu,self.driver.page_source)




if __name__ == '__main__':
    unittest.main()
"""
