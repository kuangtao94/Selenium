# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# js = 'document.getElementById("setf").target="";'
# driver.execute_script(js)
# driver.find_element_by_id("setf").click()
# time.sleep(3)
# driver.find_element_by_link_text("百度首页").click()

# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get("http://www.baidu.com")
# time.sleep(1)
# driver.find_element_by_id("kw").send_keys(u"博客")
# # 获取百度输入框的
# time.sleep(1)
# bd = driver.find_elements_by_class_name("bdsug-overflow")
# for i in bd:
#     print(i.get_attribute("data-key"))
#
# # 点击其中的一个，如：第二个
# if len(bd) > 1:
#     bd[1].click()
#     # 打印当前页面url
#     print(driver.current_url)
#     print(driver.title)
# else:
#     print("未获取到匹配的词")


# # 导入turtle包的所有内容:
# from turtle import *
#
# # 设置笔刷宽度:
# width(4)
#
# # 前进:
# forward(200)
# # 右转90度:
# right(90)
#
# # 笔刷颜色:
# pencolor('red')
# forward(100)
# right(90)
#
# pencolor('green')
# forward(200)
# right(90)
#
# pencolor('blue')
# forward(100)
# right(90)
#
# # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
# done()

#
# from turtle import *
#
# colormode(255)
#
# lt(90)
#
# lv = 14
# l = 120
# s = 45
#
# width(lv)
#
# r = 0
# g = 0
# b = 0
# pencolor(r, g, b)
#
# penup()
# bk(l)
# pendown()
# fd(l)
#
# def draw_tree(l, level):
#     global r, g, b
#     # save the current pen width
#     w = width()
#
#     # narrow the pen width
#     width(w * 3.0 / 4.0)
#     # set color:
#     r = r + 1
#     g = g + 2
#     b = b + 3
#     pencolor(r % 200, g % 200, b % 200)
#
#     l = 3.0 / 4.0 * l
#
#     lt(s)
#     fd(l)
#
#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     rt(2 * s)
#     fd(l)
#
#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     lt(s)
#
#     # restore the previous pen width
#     width(w)
#
# speed("fastest")
#
# draw_tree(l, 4)
#
# done()



"""HTMLTestRunner 截图版示例 selenium 版"""
from selenium import webdriver
import unittest_1
import time, HTMLTestRunner
import sys


class case_01(unittest_1.TestCase):
    """
    def setUp(cls):
        cls.driver = webdriver.Chrome()
    def tearDown(cls):
        cls.driver.quit()
        """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest_1 运行机制不同，会导致用力失败时截图失败
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass


    def test_case1(self):
        """ 百度搜索
        呵呵呵呵
        """
        print("本次校验没过？")
        print ("超级长"*66)
        self.driver.get("https://www.baidu.com")
        self.add_img()
        self.driver.find_element_by_id('kw').send_keys(u'百度一下')
        self.add_img()
        self.driver.find_element_by_id('su').click()
        time.sleep(1)
        self.add_img()

    def test_case2(self):
        """搜狗首页"""
        self.driver.get("http://www.sogou.com")
        print("本次校验没过？")
        self.assertTrue(False,"这是相当的睿智了")

    def test_case3(self):
        """ QQ邮箱"""
        self.driver.get("https://mail.qq.com")
        self.imgs.append(self.driver.get_screenshot_as_base64())
        print("没法打印？")
        self.assertIn(u"中文", u'中华','小当家？')

    def test_case4(self):
        u""" 淘宝"""
        self.driver.get("http://www.taobao.com/")
        raise Exception
        self.add_img()
        self.assertTrue(True)


class case_02(unittest_1.TestCase):
    """
    def setUp(cls):
        cls.driver = webdriver.Chrome()
    def tearDown(cls):
        cls.driver.quit()
        """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest_1 运行机制不同，会导致用力失败时截图失败
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass


    def test_case1(self):
        """ 百度搜索
        呵呵呵呵
        """
        print("校验了一下")
        self.driver.get("https://www.baidu.com")
        self.add_img()
        self.driver.find_element_by_id('kw').send_keys(u'百度一下')
        self.add_img()
        self.driver.find_element_by_id('su').click()
        time.sleep(1)
        self.add_img()

    @unittest_1.skip('跳过')
    def test_case2(self):
        """搜狗首页"""
        self.driver.get("http://www.sogou.com")
        print("本次校验没过？")
        self.assertTrue(False,"这是相当的睿智了")

    def test_case3(self):
        """ QQ邮箱"""
        self.driver.get("https://mail.qq.com")
        self.imgs.append(self.driver.get_screenshot_as_base64())
        print("没法打印？")
        self.assertIn(u"中文", u'中文')

    def test_case4(self):
        u""" 淘宝"""
        self.driver.get("http://www.taobao.com/")
        self.add_img()
        self.assertTrue(True)

if __name__ == "__main__":
    suite1 = unittest_1.TestLoader().loadTestsFromTestCase(case_01)
    suite2 = unittest_1.TestLoader().loadTestsFromTestCase(case_02)
    suites =  unittest_1.TestSuite()
    suites.addTests([suite2,suite1])
    runer = HTMLTestRunner.HTMLTestRunner(
        title="带截图的测试报告",
        description="小试牛刀",
        stream=open(".sample_test_report.html", "wb"),
        verbosity=2, retry=2, save_last_try=True)
    runer.run(suite1)
    runer.run(suite2)