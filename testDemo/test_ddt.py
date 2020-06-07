import unittest
import ddt
from selenium import webdriver
import time


@ddt.ddt
class DoubanTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")

    def terarDown(self) -> None:
        self.driver.quit()

    @ddt.data(['老胡', '老胡_百度搜索'], ['Demon', 'Demon_百度搜索'], ['laohu', '百度搜索_laohu'])
    @ddt.unpack
    def test_baidu(self, can, yu):
        time.sleep(3)
        self.driver.find_element_by_id('kw').send_keys(can)
        time.sleep(3)
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        self.assertEqual(self.driver.title, yu)


# tastdata1,testdata2,testdata3,exceptdata
# sum = 0
# sum = tastdata1+testdata2+testdata3
# self.assertEqual(sum,exceptdata)


if __name__ == '__main__':
    unittest.main()
