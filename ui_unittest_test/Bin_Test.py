import os
import HTMLTestRunner
import time as t
import unittest_1
from appium.webdriver.common.mobileby import MobileBy


def allTest():
    suite = unittest_1.defaultTestLoader.discover(
        start_dir=os.path.dirname(__file__),
        pattern="test_login.py",
        top_level_dir=None
    )
    return suite

def getNowtime():
    return t.strftime("%Y-%m-%d %H_%M_%S",t.localtime(t.time()))

def run():
    HTMLTestRunner.HTMLTestRunner(
        stream=open("Test_Report.html","wb"),
        title="抽屉测试用例",
        description="用例执行情况"
    ).run(allTest())

if __name__ == '__main__':
    run()