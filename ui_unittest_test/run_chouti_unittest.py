from TestCase.Selenium_test.ui_unittest_public.Login_Chouti import *
import unittest
import time as t

class Web_login(Login):
    def test_login_null(self):
        """登录测试：测试用户名和密码为空"""
        Clickbotton(self.driver)
        Clicklogin(self.driver)
        text = GetErrorText(self.driver)
        self.assertEqual(text,"手机号不能为空")

    def test_login_passwd_null(self):
        """登录测试：测试用户名不为空密码为空"""
        Clickbotton(self.driver)
        self.driver.find_element_by_id("mobile").send_keys("18797815816")
        Clicklogin(self.driver)
        text = GetErrorText(self.driver)
        self.assertEqual(text, "密码不能为空")

    def test_login_success(self):
        """登录测试：测试用户名和密码正确;验证用户名"""
        Clickbotton(self.driver)
        self.driver.find_element_by_id("mobile").clear()
        UserName(driver=self.driver)
        Clicklogin(self.driver)
        text = GetUserInfo(self.driver)
        self.assertEqual(text, "TeacherTa...")

    def test_pulink(self):
        Clickbotton(self.driver)
        self.driver.find_element_by_id("mobile").clear()
        UserName(driver=self.driver)
        Clicklogin(self.driver)
        pulink = self.driver.find_element_by_id("userProNick")
        t.sleep(2)
        action = ActionChains(self.driver)
        t.sleep(2)
        action.move_to_element(pulink).perform()
        self.driver.find_element_by_link_text("我的新热榜").click()
        t.sleep(2)
        self.driver.find_element_by_link_text("发布").click()
        t.sleep(2)
        text = PublicInfo(self.driver)
        self.assertEqual(text,"1211")

if __name__ == '__main__':
    unittest.main(verbosity=2)