"""
鼠标事件类
鼠标右键单击操作
鼠标双击操作
鼠标悬挂操作
鼠标左键单击操作
鼠标释放操作

1.对类ActionChains进行初始化
2.获取要操作元素属性的对象
3.类ActionChains实例后对象调用它里面的方法，该方法的参数就是已经获取的元素属性的对象
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as t

#鼠标悬挂操作
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://www.baidu.com")
# driver.implicitly_wait(10)
#
# action = ActionChains(driver)
# link = driver.find_element_by_name("tj_briicon")
# action.move_to_element(link).perform()
#
# driver.find_element_by_link_text("音乐").click()
# t.sleep(3)
# WebDriverWait(driver,10).until(EC.url_contains("http://music.taihe.com/"))
# driver.find_element_by_css_selector("body > div.downAppPop-bg.pr.tt.showDownAppPop > div.downApp.pr.section-inner > i").click()
# driver.find_element_by_id("ww").send_keys("123")
# t.sleep(3)
# driver.find_element_by_css_selector("#search_form > div.search > span.s_btn_wr > input").click()
# t.sleep(3)
# driver.quit()


#鼠标右键操作

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("xxxx")
# driver.implicitly_wait(10)
# driver.find_element_by_id("emp_DomainName").send_keys("xxxx")
# t.sleep(2)
# driver.find_element_by_id("emp_Password").send_keys("xxxx")
# t.sleep(2)
# driver.find_element_by_id("RemeberMe").click()
# t.sleep(2)
# driver.find_element_by_id("BtnLogin").click()
#
# WebDriverWait(driver,10).until(EC.url_contains("xxxx"))
# print("登录成功")
#
# action = ActionChains(driver)
# so = driver.find_element_by_class_name("search_input")
# t.sleep(2)
# action.context_click(so).perform()
#
# driver.quit()


#鼠标双击操作

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("xxxx")
driver.implicitly_wait(10)
driver.find_element_by_id("emp_DomainName").send_keys("xxxx")
t.sleep(2)
driver.find_element_by_id("emp_Password").send_keys("xxxx")
t.sleep(2)
driver.find_element_by_id("RemeberMe").click()
t.sleep(2)
driver.find_element_by_id("BtnLogin").click()

WebDriverWait(driver,10).until(EC.url_contains("xxxx"))
print("登录成功")

action = ActionChains(driver)
driver.find_element_by_class_name("search_input").send_keys("xxxx")
t.sleep(2)
so = driver.find_element_by_id("mysearchbtn")
action.double_click(so).perform()
t.sleep(3)


driver.quit()

#鼠标按键操作,然后释放

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("xxxx")
# driver.implicitly_wait(10)
# driver.find_element_by_id("emp_DomainName").send_keys("xxxx")
# t.sleep(2)
# driver.find_element_by_id("emp_Password").send_keys("xxxx")
# t.sleep(2)
# driver.find_element_by_id("RemeberMe").click()
# t.sleep(2)
# driver.find_element_by_id("BtnLogin").click()
#
# WebDriverWait(driver,10).until(EC.url_contains("xxxx"))
# print("登录成功")
#
# action = ActionChains(driver)
# so = driver.find_element_by_class_name("search_input")
# action.click_and_hold(so).perform()
# action.release(so).perform()
#
# driver.quit()