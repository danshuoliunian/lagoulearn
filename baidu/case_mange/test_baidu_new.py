import unittest
import time
from selenium import webdriver


class Test_baidu_News(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(self) -> None:
        self.driver.quit()

    def setUp(self) -> None:
        self.driver.get("https://news.baidu.com/")

    def tearDown(self) -> None:
        pass

    def test_sou(self):
        self.driver.find_element_by_id('ww').send_keys('思课帮')
        time.sleep(3)
        self.driver.find_element_by_id('s_btn_wr').click()
        time.sleep(3)

        self.assertEqual('百度资讯搜索_思课帮', self.driver.title)


if __name__ == '__main__':
    unittest.main()
