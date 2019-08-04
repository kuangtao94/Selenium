from selenium import webdriver
import time as  t

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://mail.sina.com.cn/")
driver.implicitly_wait(10)

driver.find_element_by_id("freename").send_keys("xxxx")
driver.find_element_by_id("freepassword").send_keys("xxxx")
t.sleep(2)
driver.find_element_by_class_name("loginBtn").click()
t.sleep(2)
#    driver.find_element_by_xpath("/html/body/div[9]/div[1]/span[1]/a").click()

driver.find_element_by_class_name("wrWriteBtn").click()
t.sleep(3)
driver.find_element_by_xpath('//*[@id="tr_to"]/td/ul/li/input').send_keys("xxxx")
t.sleep(3)
driver.find_element_by_name("subj").send_keys("Object")
t.sleep(3)
Tag = driver.find_element_by_xpath('//*[@id="SinaEditor"]/iframe')
driver.switch_to_frame(Tag)
driver.find_element_by_xpath("/html/body").send_keys("selenium")
t.sleep(2)
driver.switch_to_default_content()
# js 富文本操作
# body = "这里是通过js发的正文内容"
# Rich_js = 'document.getElementByXpath("//*[@id="SinaEditor"]/iframe").contentWindow.document.body.innerHTML="{0}";'.format(body)
# driver.execute_script(Rich_js)
# t.sleep(3)
driver.find_element_by_class_name("mailPubText").click()
driver.quit()