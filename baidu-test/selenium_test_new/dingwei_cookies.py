from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
# 启动浏览器后获取cookies
print(driver.get_cookies())
driver.get("https://www.cnblogs.com/Teachertao/")
# 打开主页后获取cookies
print(driver.get_cookies())
# 登录后获取cookies
driver.get("https://passport.cnblogs.com/user/signin")
#隐形等待
driver.implicitly_wait(10)
driver.find_element_by_id("LoginName").send_keys("user")
driver.find_element_by_id("Password").send_keys("passwd")
driver.find_element_by_id("IsRemember").click()
driver.find_element_by_id("submitBtn").click()
time.sleep(3)
print(driver.get_cookies())

# 获取指定name的cookie
print(driver.get_cookie(name=".Cnblogs.Account.Antiforgery"))

# 清除指定name的cookie
driver.delete_cookie(name=".Cnblogs.Account.Antiforgery")
print(driver.get_cookies())
# 为了验证此cookie是登录的，可以删除后刷新页面
driver.refresh()

# 清除所有的cookie
driver.delete_all_cookies()
print(driver.get_cookies())
