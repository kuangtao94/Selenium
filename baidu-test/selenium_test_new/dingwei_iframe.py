from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://mail.163.com/")
driver.implicitly_wait(10)
#点击密码登录在这里
driver.find_element_by_id("lbNormal").click()

#切换iframe
# driver.switch_to_frame("x-URS-iframe1559570723916.8506")
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to_frame(iframe)
#输入Email账号
driver.find_element_by_name("email").send_keys("123")
#输入passwd
driver.find_element_by_name("password").send_keys("111")
# 没点击操作前，判断选项框状态
s = driver.find_element_by_id("un-login").is_selected()
print(s)
#点击十天免登录--- 复选框单选
driver.find_element_by_id("un-login").click()
# 点击后，判断元素是否为选中状态
r = driver.find_element_by_id("un-login").is_selected()
print(r)
#点击登录
driver.find_element_by_id("dologin").click()

# 释放iframe，重新回到主页面上
driver.switch_to_default_content()
#点击登录
driver.find_element_by_id("dologin").click()
#退出浏览器
driver.quit()