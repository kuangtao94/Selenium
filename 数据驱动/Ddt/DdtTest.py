import ddt,logging
import unittest,traceback
import HTMLTestRunner
import os
import time
from  selenium.common.exceptions import NoSuchElementException

#初始化日志对象
logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s %(name)s %(levelname)s %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S",
    filename = "./test-ddt.log",
)

@ddt.ddt
class TestCases(unittest.TestCase):
    def setUp(self):
        print("每条case之前都会执行这个方法")

    def tearDown(self):
        print("每条case之后都会执行这个方法")

    @ddt.data(1,2,3)
    def test_testcase_01(self,value):
        print("这是第一条用例")
        try:
            self.assertTrue(value)
            print("test pass")
        except Exception as e:
            print("出错了，错误的结果为%s"%e)
            print("test failed")
            raise e

    @ddt.data((1,1),(1,2),(2,2))
    @ddt.unpack
    def test_testcase_02(self,value1,value2):
        print("这是第二条用例")
        try:
            self.assertEqual(value1,value2)
            # print("test pass")
        except NoSuchElementException as  e:
            # 使用traceback获取详细的异常信息
            logging.error("查找页面不存在，异常信息：" + str(traceback.print_exc()))
        except Exception as e:
            logging.error('未知错误，错误信息：'+str(traceback.print_exc()))
        except AssertionError as e:
            logging.debug('实际-"%s",期望-"%s",-失败'%(value1,value2))
        else:
            logging.debug('实际-"%s",期望-"%s",-通过'%(value1,value2))
        # except Exception as e:
        #     print("出错了，错误的结果为%s"%e)
        #     print("test failed")
        #     raise e

# if __name__ == '__main__':
#     unittest.main()


def getsuite():
    # suite = unittest.TestSuite() #测试套件
    # loader = unittest.TestLoader()
    # return suite.addTest(loader.loadTestsFromTestCase(TestCases))
    test_case = os.path.dirname(__file__)
    suite = unittest.defaultTestLoader.discover(
        start_dir=test_case,
        pattern="Ddt_*.py",
        top_level_dir=None
        )
    return suite

def getnowtime():
    # report_dir = "./Test_report"
    # now = time.strftime("%Y-%m-%d %H-%M-%S")
    # reportname = report_dir + "/" + now + "Test_report.html"
    # return reportname
    return time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(time.time()))

def Main():
    # with open(Report(),"wb") as file:
    #     runner = HTMLTestRunner.HTMLTestRunner(
    #         stream=file,
    #         title="Model test report",
    #         description="Hello testers This is the description of Model test")
    #     runner.run(getsuite())
    report_path = os.path.dirname(__file__)
    report = os.path.join(report_path,"Report")
    if not os.path.exists(report):
        os.mkdir(report)
    else:
        print("存在")
    file_name = report + "\\" + getnowtime() + "report_test.html"
    fp = open(file_name,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = fp,
        title = "自动化测试报告",
        description = "自动化详细测试报告"
        )
    runner.run(getsuite())
    fp.close()


if __name__ == '__main__':
    Main()