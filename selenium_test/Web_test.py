from selenium import webdriver
import time as t

# driver = webdriver.Chrome()
# driver.get("http://www.bing.com")
# driver.maximize_window()
# driver.implicitly_wait(30)
# driver.find_element_by_id("sb_form_q").send_keys("selenium\n")
# t.sleep(5)
# driver.find_element_by_id("sb_form_go").click()
# tag_name = driver.find_elements_by_tag_name("input")
# tag_name[0].send_keys("selenium\n")
# driver.quit()

"""测试当前的地址"""
# driver = webdriver.Chrome()
# driver.get("http://www.bing.com")
# driver.current_url
# print(driver.current_url)
# driver.quit()

"""测试出当前title"""
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.title
# print(driver.title)
# driver.quit()

"""测试浏览器前进后退"""
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# t.sleep(3)
# driver.get("http://www.bing.com")
# t.sleep(3)
# driver.back()
# print("back后的地址：",driver.current_url)
# t.sleep(3)
# driver.forward()
# print("前进后的地址：",driver.current_url)
# t.sleep(3)
# driver.quit()

"""多窗口操作"""
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
t.sleep(3)
#对百度登录进行点击
driver.find_element_by_link_text("登录").click()
t.sleep(3)
#点击用户名操作
driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
t.sleep(3)
#获取当前窗口句柄
nowHandle = driver.current_window_handle
t.sleep(3)
#点击当前窗口-->立即注册
driver.find_element_by_link_text("立即注册").click()
t.sleep(3)
#获取所有当前句柄
handles = driver.window_handles
t.sleep(3)
#对所有窗口进行循环 --> 进行判断
for handle in handles:
    #判断不是当前句柄
    if handle != nowHandle:
        #跳转到注册的句柄
        driver.switch_to_window(handle)
        driver.find_element_by_name("userName").send_keys("1111")
        t.sleep(3)
        driver.close()
        t.sleep(3)
#跳转到登录页面的句柄
driver.switch_to_window(nowHandle)
driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("123")
t.sleep(3)
driver.quit()

