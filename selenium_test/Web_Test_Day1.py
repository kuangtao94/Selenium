# from selenium import webdriver
# import time as t

"""clear的操作"""
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# send = driver.find_element_by_id("kw")
# send.send_keys("selenium")
# t.sleep(3)
# send.clear()
# t.sleep(3)
# driver.quit()

"""页面刷新操作"""
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# t.sleep(3)
# driver.refresh()
# t.sleep(3)
# driver.quit()

"""页面截图操作
1.打开网站之后，也可以对屏幕截屏
2.截屏后设置制定的保存路径+文件名称+后缀
"""
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# t.sleep(3)
# driver.get_screenshot_as_file("D:\\Test\\nice.png")

"""获取属性的值操作"""
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://www.baidu.com")
# such = driver.find_element_by_id("kw")
# such.send_keys("selenium")
# t.sleep(3)
# print(such.get_attribute("value"))
# print(such.get_attribute("title"))
# driver.quit()

"""is_displayed 查看是否可见操作"""
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# such = driver.find_element_by_link_text("关于百度")
# print("关于百度链接是否可见",such.is_displayed())
# driver.quit()

"""is_enabled 是否可编辑操作"""
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://www.baidu.com")
# so = driver.find_element_by_id("kw")
# print("百度输入框是否可编辑",so.is_enabled())
# driver.quit()

"""is_selected 是否可选择"""
# driver = webdriver.Chrome()
# driver.get("https://mail.sina.com.cn/")
# driver.maximize_window()
# select = driver.find_element_by_id("store1")
# print("新浪邮箱自动登录是否选择",select.is_selected())
# driver.quit()



from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#用xpath通过id属性定位
driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")
#用xpath通过name属性定位
driver.find_element_by_xpath("//*[@name='wd']").send_keys("selenium")
#用xpath通过class属性定位
driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys("selenium")

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#xpath逻辑运算
driver.find_element_by_xpath("//*[@id='kw' and @autocomplete='off']")


from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#用xpath通过其他属性定位
driver.find_element_by_xpath("//*[@autocomplete='off']").send_keys("selenium")

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#通过定位它的父亲来定位input输入框
driver.find_element_by_xpath("//span[@id='s_kw_wrap']/input").send_keys("selenium")
#通过定位它的爷爷来定位input输入框
driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys("selenium")


from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#用xpath定位老大
driver.find_element_by_xpath("//select[@id='nr']/option[1]").click()
#用xpath定位老二
driver.find_element_by_xpath("//select[@id='nr']/option[2]").click()
#用xpath定位老三
driver.find_element_by_xpath("//select[@id='nr']/option[3]").click()

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#xpath模糊匹配功能
driver.find_element_by_xpath("//*[contains(text(),'hao123')]").click()
#xpath模糊匹配某个属性
driver.find_element_by_xpath("//*[contains(@id,'kw')]").click()
#xpath模糊匹配以什么开头
driver.find_element_by_xpath("//*[starts-with(@id,'s_kw_')]").click()
#xpath模糊匹配以什么结尾
driver.find_element_by_xpath("//*[ends-with(@id,'kw_wrap')]").click()
#xpath支持正则表达式
driver.find_element_by_xpath("//*[matchs(text(),'hao123')]").click()


from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#用xpath通过id属性定位
driver.find_element_by_css_selector("#kw").send_keys("selenium")
#用xpath通过class属性定位
driver.find_element_by_css_selector(".s_ipt").send_keys("selenium")


from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_css_selector("input[id='kw'][name='wd']").send_keys("selenium")
#用xpath通过autocomplete属性定位
driver.find_element_by_css_selector("[autocomplete='off']").send_keys("selenium")
#用xpath通过name属性定位
driver.find_element_by_css_selector("[name='wd']").send_keys("selenium")
#用xpath通过type属性定位
driver.find_element_by_css_selector("[type='text']").send_keys("selenium")


#选择第一个option
driver.find_element_by_css_selector("select#nr>option：nth-child(1)").click()
#选择第二个option
driver.find_element_by_css_selector("select#nr>option：nth-child(2)").click()
#选择第三个option
driver.find_element_by_css_selector("select#nr>option：nth-child(3)").click()