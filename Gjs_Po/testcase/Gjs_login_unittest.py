from TestCase.Gjs_Po.basepage.Gjs_login import *
import unittest
import time

class Gjs(GjsLogin):
    def test_login_null(self):
        """登录测试：测试用户名和密码为空"""
        click_but_login(self.driver)
        login_button(self.driver)
        text = GetErrorText(self.driver)
        self.assertEqual(text,"请输入用户名/手机号")

    def test_login_passwd_null(self):
        """登录测试：测试用户名不为空,密码为空"""
        input_username(self.driver,"18513600235")
        login_button(self.driver)
        text = GetErrorText(self.driver)
        self.assertEqual(text, "请输入密码")

    def test_login_success(self):
        """登录测试：测试用户名和密码正确;验证用户名"""
        input_username(self.driver, "18513600235")
        input_password(self.driver,"a123456")
        login_button(self.driver, )
        text = Assert_Info(self.driver)
        self.assertEqual(text, "185****0235")
        logout_button(self.driver)

if __name__ == '__main__':
    unittest.main(verbosity=2)