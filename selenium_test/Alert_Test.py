from selenium import webdriver
from selenium.webdriver.support.select import Select
import time as t

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com/gaoji/preferences.html")
se = driver.find_element_by_id("nr")
seie = Select(se)
seie.select_by_index(1)
t.sleep(3)
driver.find_element_by_id("save").click()
t.sleep(3)
#alert查看显示文本
db = driver.switch_to_alert().text
print(db)
#接受操作
# driver.switch_to_alert().accept()
# driver.switch_to_alert().dismiss()
# driver.switch_to_alert().send_keys("value")
driver.quit()

