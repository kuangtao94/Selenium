from selenium import webdriver
import time
url = r'D:\Test\TestCase\Selenium_test\baidu-test\html\table.html'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)
t = driver.find_element_by_xpath("//*[@id='MyTable']/tbody/tr[2]/td[1]")
print(t.text)