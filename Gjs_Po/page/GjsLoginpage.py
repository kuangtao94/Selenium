from selenium.webdriver.common.by import By #定位方式
from time import sleep
from TestCase.Gjs_Po.basepage.HomePage import *

#登录页面的类
class GjsLoginPage(HomePage):
    #定位器
    #输入账号
    username_loc = (By.ID,"mobilePhone")
    # 输入密码
    password_loc = (By.ID,"password")
    # 点击登录按钮
    loginButton_loc = (By.CSS_SELECTOR,"#loginBtn")
    # 登录后验证信息
    loginInfo_loc = (By.CSS_SELECTOR,'#realName')
    # 点击安全登录
    logout_loc = (By.CSS_SELECTOR,"a.fc-blue.mr-5")
    #用户名为空 --获取错误信息
    userNull_loc = (By.CSS_SELECTOR, "span.error")
    #密码为空 --获取错误信息
    passwordNull_loc = (By.CSS_SELECTOR, "span.error")
    #用户名输入非法字符--获取错误信息
    usernameFeifa_loc = (By.CSS_SELECTOR, "span.error")


    #打开登录页面
    def openLoginPage(self):
        self.dr.get(self.url)
        self.dr.refresh()
        self.dr.maximize_window()
        sleep(0.5)

    #输入用户名
    def input_username(self,username):
        #注意 self前面加上 *
        self.find_element(*self.username_loc).send_keys(username)

    #输入密码
    def input_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    #点击登录按钮
    def click_btn(self):
        self.find_element(*self.loginButton_loc).click()

    ##登录后验证信息
    def getInfo(self):
        return self.find_element(*self.loginInfo_loc).text

    #点击安全退出
    def logout_btn(self):
        self.find_element(*self.logout_loc).click()

    #用户名为空
    def usernameNull(self):
        return self.find_element(*self.userNull_loc).text

    #密码为空
    def passwordNull(self):
        return self.find_element(*self.passwordNull_loc).text

    #用户名输入非法字符--获取错误信息
    def userFeiFa(self):
        return self.find_element(*self.usernameFeifa_loc).text