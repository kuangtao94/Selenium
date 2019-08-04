# coding:utf-8
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time

# Chrome浏览器配置文件地址
profile_directory = r'--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data'

s = requests.session()  # 新建session
url = "https://home.cnblogs.com/u/Teachertao/"

def get_cookies(url):
    '''启动selenium获取登录的cookies'''
    try:
        # 加载配置
        # option = webdriver.ChromeOptions()
        # option.add_argument(profile_directory)
        # 启动浏览器配置
        driver = webdriver.Chrome()
        driver.get(url)

        time.sleep(3)
        cookies = driver.get_cookies()  # 获取浏览器cookies
        print(cookies)
        driver.quit()
        return cookies
    except Exception as msg:
        print(u"启动浏览器报错了：%s" %str(msg))
def add_cookies(cookies):
    '''往session添加cookies'''
    try:
        # 添加cookies到CookieJar
        c = requests.cookies.RequestsCookieJar()
        for i in cookies:
            c.set(i["name"], i['value'])
        s.cookies.update(c)  # 更新session里cookies
    except Exception as msg:
        print(u"添加cookies的时候报错了：%s" % str(msg))



if __name__ == '__main__':
    cookies = get_cookies(url)
    add_cookies(cookies)


