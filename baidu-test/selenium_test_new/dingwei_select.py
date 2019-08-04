from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time as t
driver = webdriver.Chrome()
url = "https://www.baidu.com"
driver.get(url)
driver.implicitly_wait(10)
# 鼠标移动到“设置”按钮
mouse = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()
# 通过text:select_by_visible_text()
s = driver.find_element_by_id("nr")
Select(s).select_by_visible_text("每页显示50条")
t.sleep(3)
s.click()
driver.find_element_by_link_text("保存设置").click()
t.sleep(2)
#获取alert弹框
t = driver.switch_to_alert()
print(t.text)
t.accept()


# # 分两步：先定位下拉框，再点击选项
# s = driver.find_element_by_id("nr")
# s.find_element_by_xpath("//option[@value='50']").click()

# # 另外一种写法
# driver.find_element_by_id("nr").find_element_by_xpath("//option[@value='50']").click()

# # 直接通过xpath定位
# driver.find_element_by_xpath(".//*[@id='nr']/option[2]").click()

# # 通过索引：select_by_index()
# s = driver.find_element_by_id("nr")
# Select(s).select_by_index(2)

# # 通过value：select_by_value()
# s = driver.find_element_by_id("nr")
# Select(s).select_by_value("20")