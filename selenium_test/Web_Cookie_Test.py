from selenium import webdriver
import time as t

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("xxxxxxx")
driver.implicitly_wait(10)
driver.find_element_by_id("emp_DomainName").send_keys("xxxxx")
driver.find_element_by_id("emp_Password").send_keys("xxxx")
driver.find_element_by_id("BtnLogin").click()
cookies_test = driver.get_cookies()
for item in cookies_test:
    print(item)
driver.quit()
