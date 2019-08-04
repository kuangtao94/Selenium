from selenium import webdriver
import unittest,time
from selenium.webdriver.support import expected_conditions as EC

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://passport.cnblogs.com/user/signin")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        '''前面输入账号密码，让正确运行到assert这一步，断言故意设置为False不成功'''
        try:
            self.driver.find_element_by_id("LoginName").send_keys("xxxx")
            self.driver.find_element_by_id("Password").send_keys("xxxx")
            self.driver.find_element_by_id("IsRemember").click()
            self.driver.find_element_by_id("submitBtn").click()
            time.sleep(3)
        # 　判断登录成功页面是否有账号："Teacher涛 - 博客园"
            locator = ("id","header_user_left")
            text = u"Teacher涛 - 博客园"
            result = EC.text_to_be_present_in_element(locator,text)(self.driver)
            self.assertFalse(result)

        except Exception as msg:
            print("异常原因%s"%msg)
            # 图片名称可以加个时间戳
            nowtime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file("%s.jpg"%nowtime)
            raise

if __name__ == '__main__':
    unittest.main(verbosity=2)

