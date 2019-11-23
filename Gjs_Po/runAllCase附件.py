from TestCase.Gjs_Po.common.HTMLTestRunner import *
from TestCase.Gjs_Po.mail.sendmail163 import *
import HTMLTestRunnerCN
#实现的逻辑
#先生成测试报告
#查找最新的测试报告文件，通过new_file函数找到最新的测试报告，把返回的结果return file_new_name
#把new_file函数，file_new_name文件传入到send_mail 读取出来，然后以邮件的附件形式加载到邮件模板中，设置参数，链接服务器发送最新的测试报告#


if __name__ == '__main__':
    report = os.path.dirname(__file__) #D:/Project/TestCase/Gjs_Po
    test_path = os.path.join(report,"testcase") #测试用例文件夹
    suite = unittest.defaultTestLoader.discover(
        start_dir=test_path,pattern="Gjs_login*.py",top_level_dir=None)
    report_path = os.path.join(report,"report") #测试报告文件夹
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    else:
        print('存在report报告文件夹')
    now = time.strftime("%Y-%m-%d %H_%M_%S") #时间戳
    file_name = report_path + '\\' + now + "report_test.html" #测试报告文件名
    fp = open(file_name,"wb")
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream = fp,
        title = 'GJs自动化测试报告',
        description = 'u"系统环境:Windows7 浏览器:Chrome 用例执行情况:"'
    )
    runner.run(suite) #执行测试用例
    fp.close()

    new_report = new_file(report_path) #获取最新的报告文件
    semd_mail(new_report)   #发送最新的测试报告



