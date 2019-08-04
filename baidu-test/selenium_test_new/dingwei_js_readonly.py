from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time as t

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=wf")
driver.implicitly_wait(10)
WebDriverWait(driver,10)
driver.find_element_by_id("wf_label").click()

#开始地点
driver.find_element_by_id("fromStationText").clear()
driver.find_element_by_id("fromStationText").send_keys("XX\n")
t.sleep(3)

#到达地点
driver.find_element_by_id("toStationText").clear()
driver.find_element_by_id("toStationText").send_keys("XX\n")
t.sleep(3)

# 去掉元素的readonly属性
js = 'document.getElementById("train_date").removeAttribute("readonly");'
driver.execute_script(js)
t.sleep(3)

# 用js方法输入日期
js_value = 'document.getElementById("train_date").value="2019-06-01"'
driver.execute_script(js_value)
t.sleep(3)

#js处理返程时间
JS = 'document.getElementById("back_train_date").removeAttribute("readonly");'
driver.execute_script(JS)
end_js= 'document.getElementById("back_train_date").value="2019.5.3"'
driver.execute_script(end_js)
t.sleep(3)

#点击查询按钮
driver.find_element_by_id("query_ticket").click()
t.sleep(2)

# # 清空文本后输入值
# driver.find_element_by_id("train_date").clear()
# driver.find_element_by_id("train_date").send_keys("2016-12-25")

#关闭窗口
driver.quit()













