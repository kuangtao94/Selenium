from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class GjsLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://www.gjfax.com/")
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


#页面元素操作方法
#定位器定位元素的方式

# loginBut_loc = (By.CSS_SELECTOR,"span.footer-right >a") #首页页面元素登录按钮
# username_loc = (By.CSS_SELECTOR,"#mobilePhone") #输入账号
# password_loc = (By.ID,"password") #输入密码
# loginButton_loc = (By.CSS_SELECTOR,"#loginBtn") #登录页面点击登录按钮
# loginError_loc = (By.CSS_SELECTOR,"span.error") #获取错误信息
# loginInfo_loc = (By.CSS_SELECTOR,'#realName') #登录后验证信息
# logout_loc = (By.CSS_SELECTOR,"a.fc-blue.mr-5") #点击安全退出按钮

#点击登录按钮,跳转到登录页面
def click_but_login(driver):
    driver.find_element(By.CSS_SELECTOR,"span.footer-right >a").click()
#输入账号
def input_username(driver,username): #可变长不能放形参前面
    driver.find_element(By.CSS_SELECTOR,"#mobilePhone").send_keys(username)
#输入密码
def input_password(driver,password):
    driver.find_element(By.ID,"password").send_keys(password)
#登录页面点击登录按钮
def login_button(driver):
    driver.find_element(By.CSS_SELECTOR,"#loginBtn").click()
#获取错误信息
def GetErrorText(driver):
    return driver.find_element(By.CSS_SELECTOR,"span.error").text
#断言登录后验证信息
def Assert_Info(driver):
    return driver.find_element(By.CSS_SELECTOR,'#realName').text
#点击安全退出按钮
def logout_button(driver):
    driver.find_element(By.CSS_SELECTOR,"a.fc-blue.mr-5")