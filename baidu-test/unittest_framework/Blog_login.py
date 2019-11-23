from selenium import webdriver
import unittest
import time
class Blog(unittest.TestCase):
    def setUp(self):
        '''登录博客'''
        self.driver = webdriver.Chrome()
        self.driver.get("https://passport.cnblogs.com/user/signin")
        self.driver.implicitly_wait(10)

    def login(self,username,passwd):
        '''这里写了一个登录的方法,账号和密码参数化'''
        self.driver.find_element_by_id("LoginName").send_keys(username)
        self.driver.find_element_by_id("Password").send_keys(passwd)
        self.driver.find_element_by_id("IsRemember").click()
        self.driver.find_element_by_id("submitBtn").click()
        time.sleep(3)

    def is_login_sucess(self):
        '''判断是否获取到登录账户名称'''
        try:
            text = self.driver.find_element("id","header_user_left").text
            print(text)
            return True
        except:
            return False

    def test_01(self):
        '''登录案例参考:账号，密码自己设置'''
        self.login("xxx","xxx")
        # 判断结果
        result = self.is_login_sucess()
        self.assertTrue(result)

    def test_02(self):
        u'''登录案例参考:账号，密码自己设置'''
        self.login(u"xxxx", u"xxxx")  # 调用登录方法
        # 获取登录后的账号名称
        text = self.driver.find_element_by_id("lnk_current_user").text
        print(text)
        # 断言实际结果与期望结果一致
        self.assertEqual(text, u"xxx")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

