from selenium import webdriver
from PIL import Image

# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument("disable-infobars")
#打开浏览器
driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")

driver.save_screenshot("button.png")
element = driver.find_element_by_id("su")
#打印出元素的坐标
print(element.location)
#打印出元素的大小
print(element.size)

left = element.location["x"]
top = element.location["y"]
right = element.location["x"] + element.size["width"]
botton = element.location["y"] + element.size["height"]

im = Image.open("button.png")
im = im.crop((left,top,right,botton))
im.save("button.png")

driver.quit()