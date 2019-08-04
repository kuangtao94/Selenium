from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome()
driver.get("http://www.cnblogs.com/Teachertao/")
# 定位首页"新随笔"
try:
    element = driver.find_element("id", "blog_nav_newpostxx")
except NoSuchElementException as msg:
    print ("查找元素异常%s"%msg)

# 点击该元素
else:
    element.click()
finally:
    driver.quit()

"""
selenium常见异常
1.NoSuchElementException：没有找到元素
2.NoSuchFrameException：没有找到iframe
3.NoSuchWindowException:没找到窗口句柄handle
4.NoSuchAttributeException:属性错误
5.NoAlertPresentException：没找到alert弹出框
6.lementNotVisibleException：元素不可见
7.ElementNotSelectableException：元素没有被选中
8.TimeoutException：查找元素超时
"""