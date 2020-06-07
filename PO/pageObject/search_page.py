# coding:utf-8
from selenium.webdriver.common.by import By

from PO.basePage.base_page import BasePage
from selenium import webdriver


class SearchPage(BasePage):
    # 搜索框
    input_id = (By.ID, 'kw')
    # 百度一下按钮
    click_id = (By.ID, 'su')

    # 对搜索框进行内容的输入
    def input_text(self, input_text):
        self.locator(self.input_id).send_keys(input_text)

    # 点击查询按钮，实现本次搜索
    def click_element(self):
        self.locator(self.click_id).click()

    def check(self, url, input_text):
        self.visit(url)
        self.input_text(input_text)
        self.click_element()


if __name__ == "__main__":
    path = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(path)
    driver.get("https://www.baidu.com")
    driver.maximize_window()
    sp = SearchPage(driver)

    sp.check(url, '软件测试')
