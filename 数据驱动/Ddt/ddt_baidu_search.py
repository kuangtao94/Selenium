from ddt import ddt,data,unpack
from selenium import webdriver
from selenium.webdriver.common.by import By
import time,unittest

@ddt
class BaiduSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get('http://www.baidu.com')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @data(['selenium','selenium_百度搜索'],
          ['python','python_百度搜索'],
          ['appium','appium_百度搜索'])
    @unpack

    def test_search_001(self,a,b):
        self.driver.find_element(By.ID,'kw').send_keys(a)
        time.sleep(1)
        self.assertIn(a,b)

    @data({'search':'python','assertText':'python_百度搜索'})
    @unpack
    def test_search_002(self,search,assertText):
        self.driver.find_element(By.ID,'kw').send_keys(search)
        time.sleep(1)
        self.assertIn(search,assertText)

if __name__ == '__main__':
    unittest.main(verbosity=2)
