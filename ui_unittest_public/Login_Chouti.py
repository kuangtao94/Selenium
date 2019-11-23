# ###########分离简化
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time as t
import unittest

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://dig.chouti.com/")
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


#点击页面上的登录
def Clickbotton(driver):
    driver.find_element_by_id("login_btn").click()
    t.sleep(2)


#账号密码分离
def UserName(driver,username="18797815816",passwd="qqq123"):
    driver.find_element_by_id("mobile").send_keys(username)
    t.sleep(2)
    driver.find_element_by_id("mbpwd").send_keys(passwd)
    t.sleep(2)

#点击账号密码上的登录
def Clicklogin(driver):
    driver.find_element(By.CSS_SELECTOR,"button.btn-large.login-btn").click()
    t.sleep(2)

#断言-->获取错误信息
def GetErrorText(driver):
    return driver.find_element(By.CSS_SELECTOR,"div.new-dialog-tips.dialog-common-warn-tips").text

#断言-->获取用户信息
def GetUserInfo(driver):
    return driver.find_element_by_id("userProNick").text

#断言 -- 发布 --文件
def PublicInfo(driver):
    return driver.find_element_by_xpath('//*[@id="newsContent25893116"]/div[1]/a[1]').text
