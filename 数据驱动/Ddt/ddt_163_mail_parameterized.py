import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest,time
from parameterized import parameterized

#安装 : pip install parameterized

#数据驱动模型
# ddt excel+ddt yaml+ddt txt+ddt

#@unpack 表示用来解压元组到多个参数
#应用:ui级别的自动化测试中可以实现编写一个测试用例实现多个不同的测试点验证
#例如在163邮箱登录页面中,存在多种测试情况，如用户名和密码为空，用户名为空密码不为空，密码为空用户名不为空返回的错误提示信息


class Mail_163(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://mail.163.com/")

    def tearDown(self) -> None:
        self.driver.quit()

    def login_163(self,username,password):
        #验证登录163邮箱N中情况
        self.driver.find_element(By.ID,"switchAccountLogin").click()
        iframe = self.driver.find_element(By.TAG_NAME,'iframe')
        self.driver.switch_to_frame(iframe)
        self.driver.find_element(By.NAME,'email').send_keys(username)
        self.driver.find_element(By.NAME,'password').send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.ID,"dologin").click()

    #只有一个列表,列表里面有元组
    @parameterized.expand(
        [('', '', '请输入帐号'),
         ('admin', '', '请输入密码'),
         ('', 'admin', '请输入帐号'),
         ('^^^', '', '帐号格式错误')])
    def test_login(self,username,password,result):
        #登录163  --异常处理
        self.login_163(username,password)
        time.sleep(2)
        try:
            divtext = self.driver.find_element(By.CSS_SELECTOR, 'div.ferrorhead').text
            print("错误信息:", divtext)
            self.assertEqual(divtext, result)
        except Exception as msg:
            print("断言失败{}".format(msg))
        self.driver.switch_to_default_content()

if __name__ == '__main__':
    unittest.main(verbosity=2)