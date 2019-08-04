from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time as t

driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("http://www.baidu.com")
driver.get("https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=wf")
driver.implicitly_wait(10)
# driver.find_element_by_id("kw").send_keys("selenium")
# print(driver.find_element_by_id("kw").get_attribute("value"))
# action = ActionChains(driver)
# chepiao = driver.find_element_by_class_name("nav-hd")
# action.move_to_element(chepiao).perform()
# t.sleep(2)
#
# wangfang = driver.find_element_by_link_text("往返")
# action.click(wangfang)
# t.sleep(2)
WebDriverWait(driver,10)
driver.find_element_by_id("wf_label").click()

#开始地点
driver.find_element_by_id("fromStationText").clear()
driver.find_element_by_id("fromStationText").send_keys("东莞\n")
t.sleep(3)

#到达地点
driver.find_element_by_id("toStationText").clear()
driver.find_element_by_id("toStationText").send_keys("广州\n")
t.sleep(3)

#处理时间
#js去掉readonly属性
js = 'document.getElementById("train_date").removeAttribute("readonly");'
driver.execute_script(js)
#js添加时间
js_value = 'document.getElementById("train_date").value="2019-5-1"'
driver.execute_script(js_value)
t.sleep(3)

#处理返程时间
JS = 'document.getElementById("back_train_date").removeAttribute("readonly");'
driver.execute_script(JS)
end_js= 'document.getElementById("back_train_date").value="2019.5.3"'
driver.execute_script(end_js)
t.sleep(3)

#点击查询按钮
driver.find_element_by_id("query_ticket").click()
t.sleep(2)

#关闭窗口
driver.quit()