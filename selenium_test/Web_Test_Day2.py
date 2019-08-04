from selenium import webdriver
from selenium.webdriver.support.select import Select
import time as t

driver = webdriver.Chrome()
driver.maximize_window()
#driver.get("http://sahitest.com/demo/selectTest.htm")
# select_test = driver.find_element_by_id("s3Id")
#实例化Select()
# se = Select(select_test)
#使用select 索引方法
# se.select_by_index(1)
# t.sleep(3)
#使用select value 方法
# se.select_by_value("o4val")
# t.sleep(3)
#使用select 文本方法
# se.select_by_visible_text("With spaces")
# t.sleep(3)
# driver.quit()



#拉钩网select

driver.get("http://www.lagou.com")
t.sleep(2)
driver.find_element_by_id("cboxClose").click()
t.sleep(2)
driver.find_element_by_id("search_input").send_keys("自动化测试")
t.sleep(3)
driver.find_element_by_id("search_button").click()
t.sleep(3)
#定位拉钩月薪
driver.find_element_by_xpath('//*[@id="order"]/li/div[2]/div').click()
t.sleep(3)
#定位 5- 10K
#db = driver.find_element_by_xpath('//*[@id="order"]/li/div[2]/div/ul/li[4]/a').click()
db1 = driver.find_element_by_xpath("//*[@id='order']/li/div[2]/div/ul/li[5]/a").click()
t.sleep(3)
driver.quit()