from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os,time

'''登录博客'''
option = webdriver.ChromeOptions()
option.add_argument(r"--user-data-dir = C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome(chrome_options=option)
# driver.get("https://passport.cnblogs.com/user/signin")
driver.implicitly_wait(10)

"""账号和密码登录"""
# driver.find_element_by_id("LoginName").send_keys("xxx")
# driver.find_element_by_id("Password").send_keys("xxx")
# driver.find_element_by_id("IsRemember").click()
# login = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,"submitBtn")))
# login.click()
#
# driver.find_element_by_link_text("我的博客").click()
# time.sleep(2)
driver.get("https://www.cnblogs.com/Teachertao/")
time.sleep(2)
driver.find_element_by_link_text("发新随笔").click()
for i in range(10):
    # 点开编辑器图片
    driver.find_element_by_css_selector("img.mceIcon").click()
    time.sleep(3)
    #定位所有iframe,取第二个
    iframe = driver.find_elements_by_tag_name("iframe")[1]
    #切换到iframe上
    driver.switch_to_frame(iframe)
    # print(iframe)
    #点击上传文件按钮
    # submit = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"qq-upload-button")))
    # submit.click()
    time.sleep(3)
    driver.find_element_by_class_name("qq-upload-button").click()
    # js = 'document.getElementByClassName("qq-upload-button").click();'
    # driver.execute_script(js)
    # 执行autoit上传文件
    # os.system(r"C:\Users\Administrator\Desktop\sendfile.exe")
    #批量上传图片
    file_name = "F:\\12\\%s.png"%i
    os.system(r"C:\Users\Administrator\Desktop\send.exe %s"%file_name)
    time.sleep(3)
    # 切回到主页面
    driver.switch_to_default_content()

