# from selenium import webdriver
# import time as t
# driver = webdriver.Chrome()
# url = "file:///D:/Test/TestCase/Selenium_test/baidu-test/testalert.html"
# driver.get(url)
# t.sleep(2)
# driver.find_element_by_id("alert").click()
# t.sleep(2)
# t = driver.switch_to_alert()
# #打印警告框文本内容
# print(t.text)
# #点警告提示框确认
# t.accept()
# #点dismiss取消弹框


# from selenium import webdriver
# import time as t
# driver = webdriver.Chrome()
# url = "file:///D:/Test/TestCase/Selenium_test/baidu-test/testalert.html"
# driver.get(url)
# t.sleep(2)
# driver.find_element_by_id("confirm").click()
# t.sleep(2)
# t = driver.switch_to_alert()
# #打印警告框文本内容
# print(t.text)
# #点警告提示框确认
# t.accept()
# #点dismiss取消弹框

from selenium import webdriver
import time as t
driver = webdriver.Chrome()
url = "file:///D:/Test/TestCase/Selenium_test/baidu-test/testalert.html"
driver.get(url)
t.sleep(2)
driver.find_element_by_id("prompt").click()
t.sleep(2)
t = driver.switch_to_alert()
#打印警告框文本内容
print(t.text)
t.send_keys("selenium")
#点警告提示框确认
t.accept()
#点dismiss取消弹框

