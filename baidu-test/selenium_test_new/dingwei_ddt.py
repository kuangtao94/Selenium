import ddt
import unittest_1

#测试数据
testData = [{"username":"selenium","passwd":"16371821"},
            {"username":"appium","passwd":"38219131"},
            {"username":"python","passwd":"12382313"}]

@ddt.ddt
class Test(unittest_1.TestCase):
    def setUp(self):
        print("start")

    def tearDown(self):
        print("end")

    @ddt.data(*testData)
    def test_data(self,data):
        print(data)


if __name__ == '__main__':
    unittest_1.main(verbosity=2)