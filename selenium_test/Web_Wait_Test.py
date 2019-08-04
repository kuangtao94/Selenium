"""
固定等待 time.sleep()
隐形等待 implicitly_wait 长时间等待整个页面，如等待30s，它2s就进入url，显示页面，就不用等待30s
显示等待 WebDriverWait 执行程序会每隔一段时间执行自定义的判断条件，如果条件成立，继续，反则提示错误信息

类主要总结如下：
alert_is_present 是否存在aert
element_located_selection_state_to_be 是否被选中
element_located_to_be_selecte 期望选中
frame_to_be_available_and_switch_to_it 判断frame是否可用
text_to_be_present_in_element 判断text是否出现
text_to_be_present_in_element_value ;text是否出现在value的属性中
url_contains 判断url是否存在
visibility_of_element_located 页面元素对象可见
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time as t

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(30)
# driver.get("http://www.baidu.com")
"""WebDriverWait类中的driver是webdriver实例化得，10 为timeout 显示等待的时间，每隔10s进行操作
until检测URL是否在点击显示后的url，则预期结果
"""
#点击百度推广链接
# driver.find_element_by_link_text("百度推广").click()
#断言点击后的链接是否一致
# WebDriverWait(driver,10).until(
#     EC.url_contains("http://e.baidu.com/?refer=888"))
#对新的url页面进行操作
# driver.find_element_by_id("contactName").send_keys("1234")
# t.sleep(3)
# driver.find_element_by_id("contactCell").send_keys("11111111")
# t.sleep(3)
# driver.quit()


driver = webdriver.Chrome()
driver.maximize_window()
#driver.get("https://www.baidu.com")
driver.implicitly_wait(30)
#页面对象可见
# isGoogle = WebDriverWait(driver,10).until(
#     EC.visibility_of_element_located((By.ID,"kw")))
# isGoogle.send_keys("Google")
# t.sleep(3)
# driver.quit()

#alert 操作
# driver.get("https://www.baidu.com/gaoji/preferences.html")
# driver.find_element_by_id("save").click()
# isbaidu = WebDriverWait(driver,10).until(EC.alert_is_present())
#driver.switch_to_alert().text
# print(isbaidu.text)
# driver.quit()

# 判断错误信息是否存在
# driver.get("http://www.baidu.com")
# driver.find_element_by_link_text("登录").click()
# driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
# driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
# istext = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.ID,"TANGRAM__PSP_10__error"),"请您输入手机/邮箱/用户名"))
# print(istext)
# driver.quit()

#判断元素是否被选中
driver.get("http://www.baidu.com")
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
#人为复选框√取消,程序报错
#driver.find_element_by_id("TANGRAM__PSP_10__memberPass").click()
#默认复选框√勾选
WebDriverWait(driver,10).until(EC.element_located_to_be_selected((By.ID,"TANGRAM__PSP_10__memberPass")))
driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("111111")
t.sleep(3)
driver.quit()
