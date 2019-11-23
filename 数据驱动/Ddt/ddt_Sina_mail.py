import unittest
from ddt import ddt,unpack,data
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest,time

#数据驱动模型
# ddt excel+ddt yaml+ddt txt+ddt

#@unpack 表示用来解压元组到多个参数
#应用:ui级别的自动化测试中可以实现编写一个测试用例实现多个不同的测试点验证
#例如在新浪邮箱登录页面中,存在多种测试情况，如用户名和密码为空，用户名为空密码不为空，密码为空用户名不为空返回的错误提示信息

@ddt
class Mail_163(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.driver.get("https://mail.sina.com.cn/")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @data(('','','请输入邮箱名'),('admin','','请输入密码'),('','admin','请输入邮箱名'),('^^^','','您输入的邮箱名格式不正确'))
    @unpack
    def test_login_163(self,username,password,result):
        #验证登录新浪邮箱N中情况
        self.driver.find_element(By.CLASS_NAME,'username').clear()
        self.driver.find_element(By.CLASS_NAME,'username').send_keys(username)
        self.driver.find_element(By.CLASS_NAME,'password').send_keys(password)
        self.driver.find_element(By.CLASS_NAME,"loginBtn").click()
        time.sleep(1)
        xpath1 = '/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[2]/form/div[1]/span[1]'
        divtext = self.driver.find_element_by_xpath(xpath1).text
        print('错误信息:',divtext)
        self.assertEqual(divtext,result)


if __name__ == '__main__':
    unittest.main(verbosity=2)


