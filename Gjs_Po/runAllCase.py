import os
from TestCase.Gjs_Po.common.HTMLTestRunner import *
import unittest
import time

#定义allCase方法
def AllCase():
    file_path = os.path.join(os.path.dirname(__file__),"testcase")
    # print(file_path) #D:/Project/TestCase/Gjs_Po\testcase
    suite = unittest.defaultTestLoader.discover(
        start_dir=file_path,
        pattern="Gjs_login*.py",
        top_level_dir=None
    )
    return suite

#获取当前系统时间
def getNowtime():
    return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))

#测试报告
def run():
    report_path = os.path.join(os.path.dirname(__file__),"report")
    filename = report_path + "\\" + getNowtime() + "report_test.html"
    fp = open(filename,"wb") #以二进制读取
    runner = HTMLTestRunner(
        stream = fp,
        title = u"广金所登录自动化测试报告",
        description = u"系统环境:Windows7 浏览器:Chrome 用例执行情况:")
    runner.run(AllCase()) #执行测试用例
    fp.close()

#程序入口
if __name__ == '__main__':
    run()