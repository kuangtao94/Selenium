from selenium import webdriver
import time as t

driver = webdriver.Chrome()
driver.get(r"D:\Test\TestCase\Selenium_test\baidu-test\html\div.html")

#纵向底部
js1 = 'document.getElementById("nice").scrollTop=10000'
driver.execute_script(js1)
t.sleep(5)

#纵向顶部
js2 = 'document.getElementById("nice").scrollTop=0'
driver.execute_script(js2)
t.sleep(4)

#横向向右
js3 = 'document.getElementById("nice").scrollLeft=10000'
driver.execute_script(js3)
t.sleep(4)

#横向向左
js4 = 'document.getElementById("nice").scrollLeft=0'
driver.execute_script(js4)
t.sleep(3)

#获取class返回的是list对象,取list的第一个
js5 = 'document.getElementsByClassName("scroll")[0].scrollTop=10000'
driver.execute_script(js5)
t.sleep(5)

#控制横向滚动条的位置
js6 = 'document.getElementsByClassName("scroll")[0].scrollLeft=10000'
driver.execute_script(js6)
t.sleep(5)

#关闭窗口
driver.quit()
