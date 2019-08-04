from selenium import webdriver
import time as t
driver = webdriver.Chrome()
driver.get("https://www.cnblogs.com/")
print(driver.name)

# 拉到底部
def scroll_foot():
    if driver.name == "chrome":
        js = "var q=document.documentElement.scrollTop=1000"
    else:
        js = "var q=document.body.scrollTop=10000"
    return driver.execute_script(js)

t.sleep(3)

#滚动到底部
js = "window.scrollTo(0,document.documentElement.scrollHeight)"
driver.execute_script(js)
t.sleep(3)

#滚动到顶部
js = "window.scrollTo(0,0)"
driver.execute_script(js)

t.sleep(2)

# 回到顶部
def scroll_top():
    if driver.name == "chrome":
        js = "var q=document.documentElement.scrollTop=0"
    else:
        js = "var q=document.body.scrollTop=0"
    return driver.execute_script(js)

target = driver.find_element_by_css_selector("#pager_bottom>#paging_block>div>a.p_1 current")
driver.execute_script("arguments[0].scrollIntoView();", target)

if __name__ == '__main__':
    scroll_foot()
    scroll_top()