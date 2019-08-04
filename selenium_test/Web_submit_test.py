from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time as t

driver = webdriver.Chrome()
driver.get("file:///D:/Test/TestCase/Selenium_test/login.html")
driver.maximize_window()
tags = driver.find_elements_by_tag_name("input")
tags[0].send_keys("admin")
tags[1].send_keys("admin")
tags[2].submit()
t.sleep(3)
driver.quit()