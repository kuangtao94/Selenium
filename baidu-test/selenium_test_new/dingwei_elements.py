from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.lagou.com/")
#关闭切换城市
driver.find_element_by_id("cboxClose").click()
driver.implicitly_wait(10)
#获取当前窗口的句柄
hand = driver.current_window_handle
print(hand)
#点击产品经理打开新的标签
# driver.find_element_by_link_text("产品经理").click()
#点击产品经理不打开新的标签 -- js
js = 'document.getElementClassName="highlight".target="";'
driver.execute_script(js)
time.sleep(3)
driver.find_element_by_link_text("产品经理").click()

#获取所有句柄
all_hand = driver.window_handles
print(all_hand)

#切换句柄
#判断当前的句柄不等于首页就切换
for item in all_hand:
    if item != hand:
        driver.switch_to_window(item)
        print(driver.title)

#方法二，直接在list中切换
driver.switch_to_window(all_hand[1])
print(driver.title)

#关闭新窗口
driver.close()

#切换首页
driver.switch_to_window(hand)
#打印当前的title
print(driver.title)
