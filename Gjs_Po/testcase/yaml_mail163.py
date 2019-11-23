import yaml
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time,os

#yaml简介 https://www.ibm.com/developerworks/cn/xml/x-cn-yamlintro/index.html

#安装:pip install yaml

def getdata():
    yaml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"data")
    # print(yaml_path) #D:\Project\TestCase\Gjs_Po\common
    yaml_file = os.path.join(yaml_path,'Mail163.yaml')
    # 读取yaml的值
    yamlindex = open(yaml_file,'r',encoding='utf-8')
    # 把文件内容读取出来
    data = yaml.load(yamlindex)
    return data

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

    def Assert_Text(self):
        #断言 :文本断言
        try:
            divtext = self.driver.find_element(By.CSS_SELECTOR, 'div.ferrorhead').text
            return divtext
        except Exception as msg:
            print("断言失败{}".format(msg))
        #退出iframe框架
        self.driver.switch_to_default_content()


    def test_username_password_null(self):
        '''验证:用户名和密码为空的错误信息提示'''
        self.login_163(getdata()['case1']['user'],getdata()['case1']['passwd'])
        self.assertEqual(self.Assert_Text(),getdata()['case1']['errorText'])

    def test_username_null(self):
        '''验证:用户名为空密码不为空的错误信息提示'''
        self.login_163(getdata()['case2']['user'], getdata()['case2']['passwd'])
        self.assertEqual(self.Assert_Text(), getdata()['case2']['errorText'])

    def test_passwd_null(self):
        '''验证:用户名不为空密码为空的错误信息提示'''
        self.login_163(getdata()['case3']['user'], getdata()['case3']['passwd'])
        self.assertEqual(self.Assert_Text(), getdata()['case1']['errorText'])

    def test_username_input_format(self):
        '''验证:用户名输入非法字符的错误信息提示'''
        self.login_163(getdata()['case4']['user'], getdata()['case4']['passwd'])
        self.assertEqual(self.Assert_Text(), getdata()['case4']['errorText'])

if __name__ == '__main__':
    unittest.main(verbosity=2)