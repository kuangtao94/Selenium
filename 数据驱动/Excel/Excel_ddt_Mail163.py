import xlrd
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import ddt,data,unpack
import time

#安装:pip install xlrd
#读取的数据存储在list表中
def readExcels():
    table = xlrd.open_workbook('Mail163.xlsx','r')
    sheet = table.sheet_by_index(0)
    nrow = [] #定义空列表
    for row in range(1,sheet.nrows): #从1-N行读取遍历数据
        #sheet.row_values(1,0,2)从0-2列读取数据成列表
        nrow.append(sheet.row_values(row,start_colx=0,end_colx=sheet.ncols))
    return nrow
# print(readExcels())
#[['', '', '请输入账号'], ['admin', '', '请输入密码'], ['', 'admin', '请输入账号'], ['^^^^', '', '账号格式错误']]

@ddt
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

    @data(*readExcels())
    @unpack
    def test_username_password_null(self,username,password,result):
        '''验证:登录163邮箱 N中情况的错误信息提示'''
        self.login_163(username,password)
        self.assertEqual(self.Assert_Text(),result)

    # def test_username_null(self):
    #     '''验证:用户名为空密码不为空的错误信息提示'''
    #     self.login_163(readusername(2),readpassword(2))
    #     self.assertEqual(self.Assert_Text(), readresult(2))
    #
    # def test_passwd_null(self):
    #     '''验证:用户名不为空密码为空的错误信息提示'''
    #     self.login_163(readusername(3), readpassword(3))
    #     self.assertEqual(self.Assert_Text(),readresult(3))
    #
    # def test_username_input_format(self):
    #     '''验证:用户名输入非法字符的错误信息提示'''
    #     self.login_163(readusername(4), readpassword(4))
    #     self.assertEqual(self.Assert_Text(), readresult(4))


if __name__ == '__main__':
    unittest.main(verbosity=2) #详细日志信息