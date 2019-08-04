from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:63342/day1/Selenium_test/html/%E5%AE%9A%E4%BD%8D%E9%9A%90%E8%97%8F%E5%85%83%E7%B4%A0.html?_ijt=rt9uftv1kmv50ln7j373ik61ef")

# 定位 type="hidden"隐藏元素
# ele1 = driver.find_element_by_id("yoyo")
# print("打印元素信息：%s" % ele1)
# 获取元素属性
# print(ele1.get_attribute("name"))
# 判断元素是否隐藏
# print(ele1.is_displayed())

js = 'document.getElementById("baidu").click()'
driver.execute_script(js)

