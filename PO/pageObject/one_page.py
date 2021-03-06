from selenium.webdriver.common.by import By
from PO.basePage.base_pageo import BasePage


class SearchPage(BasePage):
    # 定位元素
    search_loc = (By.NAME, "q")  # 搜索框
    btn_loc = (By.NAME, "go")  # 搜索按钮

    # 重写父类的open()方法
    def open(self):
        self._open(self.base_url)

    def search_content(self, content):
        # 调用父类的find_emelemt，然后将本类的参数传入
        content1 = self.find_emelemt(*self.search_loc)
        content1.send_keys(content)

    def btn_click(self):
        btn1 = self.find_emelemt(*self.btn_loc)
        btn1.click()
