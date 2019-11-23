import unittest,os,time,HTMLTestRunner,paramunittest

# @paramunittest.parametrized(
#     ("admin1","1234","true"),
#     ("admin2","1234","true"),
#     ("admin3","1234","true"),
#     ("admin4","1234","true"),
#     ("admin5","1234","true"),
#     ("admin6","1234","true"),
#     ("admin7","1234","true"),
#     ("admin8","1234","true"),
#     ("admin9","1234","true"),
#     ("admin10","1234","true")
# )

@paramunittest.parametrized(
    {"user": "admin", "psw": "123", "result": "true"},
    {"user": "admin1", "psw": "1234", "result": "true"},
    {"user": "admin2", "psw": "1234", "result": "true"},
    {"user": "admin3", "psw": "1234", "result": "true"},
    {"user": "admin4", "psw": "1234", "result": "true"},
    {"user": "admin5", "psw": "1234", "result": "true"},
    {"user": "admin6", "psw": "1234", "result": "true"},
    {"user": "admin7", "psw": "1234", "result": "true"},
    {"user": "admin8", "psw": "1234", "result": "true"},
    {"user": "admin9", "psw": "1234", "result": "true"},
    {"user": "admin10", "psw": "1234", "result": "true"},
    {"user": "admin11", "psw": "1234", "result": "true"},
)
class TestDemo(unittest.TestCase):
    def setParameters(self,user,psw,result):
        self.user = user
        self.psw = psw
        self.result = result

    def testcase(self):
        print("开始执行用例--------")
        time.sleep(0.5)
        print("输入用户名：%s" % self.user)
        print("输入密码：%s" % self.psw)
        print("输入预期结果：%s" % self.result)
        time.sleep(0.5)
        self.assertTrue(self.result == "true")

# 用例路径
case_path = os.path.join(os.getcwd())
# 报告存放路径
report_path = os.path.join(os.getcwd())
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                     pattern="*.py",
                                                     top_level_dir=None)
    print(discover)
    return discover
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(all_case())

    # # html报告文件路径
    # report_abspath = os.path.join(report_path, "result.html")
    # fp = open(report_abspath, "wb")
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
    #                                        title=u'自动化测试报告,测试结果如下：',
    #                                        description=u'用例执行情况：')
    #
    # # 调用add_case函数返回值
    # runner.run(all_case())
    # fp.close()

