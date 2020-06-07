from selenium import webdriver

from time import sleep

path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(path)
url = 'https://www.baidu.com//'
driver.get(url)
sleep(3)

driver.find_element_by_id('kw').send_keys('哈哈')
driver.find_element_by_id("su").click()

print(driver.title)
sleep(3)

driver.quit()
