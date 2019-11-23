import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#未封装的读取文本信息方法
# with open('Mail163.txt', 'r', encoding='utf-8') as fp:
#     file = fp.readlines()
#     aa = ''.join(file).split('\n')
#     print(aa[2],type(aa[2]))


def MailInfo(index):
    '''封装读取文本信息方法,index为读取的行数'''
    with open('Mail163.txt','r',encoding='utf-8') as fp:
        file = fp.readlines()
        aa = "".join(file).split('\n')
        return aa[index]


#报错信息 --添加encoding='utf-8'
#UnicodeDecodeError: 'gbk' codec can't decode byte 0xb7 in position 29: illegal multibyte sequence
# print(MailInfo(2))
#字符串切割\n -->用split('\n')
#['\n', 'admin\n', '^^^^\n', '请输入帐号\n', '请输入密码\n', '帐号格式错误']


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
        self.driver.switch_to_default_content()


    def test_username_password_null(self):
        '''验证:用户名为空密码为空的错误信息提示'''
        self.login_163(MailInfo(0),MailInfo(0))
        self.assertEqual(self.Assert_Text(),MailInfo(3))

    def test_username_null(self):
        '''验证:用户名为空密码不为空的错误信息提示'''
        self.login_163(MailInfo(0),MailInfo(1))
        self.assertEqual(self.Assert_Text(), MailInfo(3))

    def test_passwd_null(self):
        '''验证:用户名不为空密码为空的错误信息提示'''
        self.login_163(MailInfo(1), MailInfo(0))
        self.assertEqual(self.Assert_Text(),MailInfo(4))

    def test_username_input_format(self):
        '''验证:用户名输入非法字符的错误信息提示'''
        self.login_163(MailInfo(2), MailInfo(1))
        self.assertEqual(self.Assert_Text(), MailInfo(5))


if __name__ == '__main__':
    unittest.main(verbosity=2) #详细日志信息