from selenium import webdriver
from TestCase.Gjs_Po.page.GjsLoginpage import *
from TestCase.Gjs_Po.common.helper import *
import unittest

#类的继承
class GjsTestLogin(unittest.TestCase,Helper):

    def setUp(self)-> None:
        self.url = 'https://www.gjfax.com/toLogin'
        self.dr = webdriver.Chrome()
        self.dr.implicitly_wait(10)

        #实例化一个对象
        self.loginpage = GjsLoginPage(self.url,self.dr)

    def tearDown(self)-> None:
        self.dr.quit()

    #测试正常的登录
    def test_login_success(self):
        #打开登录页面
        self.loginpage.openLoginPage()
        self.log('测试正常:自动化测试 -->打开登录页面')
        #输入用户名
        self.loginpage.input_username(self.readusername(1))
        self.log('测试正常:自动化测试 -->输入用户名')
        #输入密码
        self.loginpage.input_password(self.readpassword(1))
        self.log('测试正常:自动化测试 -->输入密码')
        #点击登录
        self.loginpage.click_btn()
        self.log('测试正常:自动化测试 -->点击登录')
        #断言
        self.assertEqual(self.loginpage.getInfo(),self.readAssertText(1))
        self.log('测试正常:自动化测试 -->断言登录后信息是否符合预期')
        #点击退出
        self.loginpage.logout_btn()
        self.log('测试正常:自动化测试 -->点击安全退出')

    #测试密码为空
    def test_password_null(self):
        # 打开登录页面
        self.loginpage.openLoginPage()
        self.log('测试密码为空:自动化测试 -->点击登录页面')
        # 输入用户名
        self.loginpage.input_username(self.readusername(2))
        self.log('测试密码为空:自动化测试 -->输入用户名')
        # 不输入密码
        self.loginpage.input_password(self.readpassword(2))
        self.log('测试密码为空:自动化测试 -->不输入密码')
        # 点击登录
        self.loginpage.click_btn()
        self.log('测试密码为空:自动化测试 -->点击登录')
        # 断言
        self.assertEqual(self.loginpage.passwordNull(), self.readAssertText(2))
        self.log('测试密码为空:自动化测试 -->断言密码为空信息是否符合预期')

    #测试用户名为空
    def test_username_null(self):
        # 打开登录页面
        self.loginpage.openLoginPage()
        self.log('测试用户名为空:自动化测试 -->点击登录页面')
        # 输入用户名
        self.loginpage.input_username(self.readusername(3))
        self.log('测试用户名为空:自动化测试 -->不输入用户名')
        # 输入密码
        self.loginpage.input_password(self.readpassword(3))
        self.log('测试用户名为空:自动化测试 -->输入密码')
        # 点击登录
        self.loginpage.click_btn()
        self.log('测试用户名为空:自动化测试 -->点击登录')
        # 断言
        self.assertEqual(self.loginpage.usernameNull(), self.readAssertText(3))
        self.log('测试用户名为空:自动化测试 -->断言用户名为空信息是否符合预期')

    #测试用户名输入非法字符
    def test_username_Feifa(self):
        # 打开登录页面
        self.loginpage.openLoginPage()
        self.log('测试用户名输入非法:自动化测试 -->点击登录页面')
        # 输入非法用户名
        self.loginpage.input_username(self.readusername(4))
        self.log('测试用户名输入非法:自动化测试 -->输入非法用户名')
        # 输入密码
        self.loginpage.input_password(self.readpassword(4))
        self.log('测试用户名输入非法:自动化测试 -->输入密码')
        # 点击登录
        self.loginpage.click_btn()
        self.log('测试用户名输入非法:自动化测试 -->点击登录')
        # 断言
        self.assertEqual(self.loginpage.userFeiFa(), self.readAssertText(2))
        self.log('测试用户名输入非法:自动化测试 -->断言用户名输入非法信息是否符合预期')

if __name__ == '__main__':
    unittest.main(verbosity=2)