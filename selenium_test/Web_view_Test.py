from selenium import webdriver
import time as t

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
#使用JS进行滑动屏幕--->翻页
Down_js = "var q=document.documentElement.scrollTop=1000"
Up_js = "var q=document.documentElement.scrollTop=0"

#实现先下滑---上滑
driver.execute_script(Down_js)
t.sleep(2)
driver.execute_script(Up_js)
t.sleep(2)
driver.execute_script(Down_js)
t.sleep(2)
driver.find_element_by_css_selector("#page > a:nth-child(10) > span.pc").click()
t.sleep(2)
driver.quit()

