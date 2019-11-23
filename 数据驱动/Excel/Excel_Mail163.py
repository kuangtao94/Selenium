import xlrd
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#安装:pip install xlrd
def readExcel(nrow):
    '''读取Excel数据'''
    table = xlrd.open_workbook('Mail163.xlsx','r')
    sheet = table.sheet_by_index(0)
    return sheet.row_values(nrow)

def readusername(nrow):
    '''读取用户名数据'''
    return readExcel(nrow)[0]

def readpassword(nrow):
    '''读取密码数据'''
    return readExcel(nrow)[1]

def readresult(nrow):
    '''读取预期结果数据'''
    return readExcel(nrow)[2]

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
        '''验证:用户名和密码为空的错误信息提示'''
        self.login_163(readusername(1),readpassword(1))
        self.assertEqual(self.Assert_Text(),readresult(1))

    def test_username_null(self):
        '''验证:用户名为空密码不为空的错误信息提示'''
        self.login_163(readusername(2),readpassword(2))
        self.assertEqual(self.Assert_Text(), readresult(2))

    def test_passwd_null(self):
        '''验证:用户名不为空密码为空的错误信息提示'''
        self.login_163(readusername(3), readpassword(3))
        self.assertEqual(self.Assert_Text(),readresult(3))

    def test_username_input_format(self):
        '''验证:用户名输入非法字符的错误信息提示'''
        self.login_163(readusername(4), readpassword(4))
        self.assertEqual(self.Assert_Text(), readresult(4))


if __name__ == '__main__':
    unittest.main(verbosity=2) #详细日志信息