from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as t

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://cn.bing.com")
driver.implicitly_wait(10)

send = driver.find_element_by_name("q")
t.sleep(2)
send.send_keys("selenium")
#选中后删除
t.sleep(2)
send.send_keys(Keys.CONTROL,"a")
t.sleep(2)
# send.send_keys(Keys.DELETE)
# send.send_keys(Keys.BACKSPACE)

#复制&剪切&粘贴
send.send_keys(Keys.CONTROL,"c")
send.send_keys(Keys.CONTROL,"x")
driver.get("http://www.baidu.com")
sobaidu = driver.find_element_by_id("kw")
t.sleep(2)
sobaidu.send_keys(Keys.CONTROL,"v")
driver.find_element_by_id("su").click()
sobaidu.send_keys(Keys.F5)
t.sleep(2)
sobaidu.send_keys(Keys.F12)
t.sleep(2)
driver.quit()
