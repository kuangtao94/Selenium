from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.cnblogs.com/Teachertao/")
# 判断title完全等于
title = EC.title_is("Teacher涛 - 博客园")
print(title(driver))

# 判断title包含
title1 = EC.title_contains("Teacher")
print(title1(driver))

#另外两种写法
r1 = EC.title_contains("Teacher")(driver)
r2 = EC.title_is("Teacher涛 - 博客园")(driver)
print(r1,r2)

# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# mouse = driver.find_element("name","tj_briicon")
# ActionChains(driver).move_to_element(mouse).perform()
# # driver.find_element("link text","糯米").click()
# locator = ("link text","糯米")
# text = "糯米"
# result = EC.text_to_be_present_in_element(locator,text)(driver)
# print(result)
#
# # 下面是失败的案例
# text1 = u"糯米网"
# result1 = EC.text_to_be_present_in_element(locator, text1)(driver)
# print(result1)
#
# locator2 = ("id", "su")
# text2 = u"百度一下"
# result2 = EC.text_to_be_present_in_element_value(locator2, text2)(driver)
# print(result2)