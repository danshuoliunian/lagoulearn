# coding:utf-8
from PO.basePage.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class LoginPage(BasePage):
    path = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(path)
    url = 'https://stage.unicareer.com/'
    driver.get(url)
    sleep(3)
    longin_weizhi = (By.CLASS_NAME, 'uni-avatar-bread-crumb-item').click()
    longin_name = (By.ID, 'phone')
    pwd = (By.ID, 'password')
    login_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[1]/form/button')

    def input_username(self, user_name):
        self.locator(self.longin_name).send_keys(user_name)

    def input_pwd(self, pwd):
        self.locator(self.pwd).send_keys(pwd)

    def login(self):
        self.locator(self.login_button).click()

    def check(self, user_name, pwd):
        self.visit(self.url)
        self.input_username(user_name)
        self.input_pwd(pwd)
        self.login()


if __name__ == '__main__':
    path = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(path)
    url = 'https://stage.unicareer.com/'
    driver.get(url)
    user_name = '18235465758'
    pwd = 'Test1234'
    lp = LoginPage(driver)
    lp.check(user_name, pwd)
