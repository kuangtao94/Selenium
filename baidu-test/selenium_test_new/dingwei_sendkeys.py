from selenium import webdriver
from pymouse import *
from pykeyboard import PyKeyboard
import time

driver = webdriver.Chrome()
driver.get("https://www.autoitscript.com/files/autoit3/autoit-v3-setup.exe")

m = PyMouse()
k = PyKeyboard()
time.sleep(3)
# 默认在取消按钮上，先切换到保存文件上
k.release_key(k.tab_key)  # 发送TAB键
time.sleep(3)
# 第一次回车没生效，所以多发一次回车
k.press_key("ENTER")   # 发送回车键
k.press_key("ENTER")   # 发送回车键
