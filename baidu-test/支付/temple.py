import zhifu
from unittest import mock
import unittest

class Test_zhifu_statues(unittest.TestCase):
    '''单元测试用例'''
    def test_01(self):
        '''测试支付成功场景'''
        # mock 一个支付成功的数据
        zhifu.zhifu = mock.Mock(return_value={"result": "success",
        "reason":"null"})
        # 根据支付结果测试页面跳转
        statues = zhifu.zhifu_status()
        print(statues)
        self.assertEqual(statues, "支付成功")
    def test_02(self):
        '''测试支付失败场景'''
        # mock 一个支付失败的数据
        zhifu.zhifu = mock.Mock(return_value={"result": "fail",
        "reason": "余额不足"})
        # 根据支付结果测试页面跳转
        statues = zhifu.zhifu_status()
        self.assertEqual(statues, "支付失败")

    def test_03(self):
        "测试支付未知错误"
        # mock 一个支付未知错误数据
        zhifu.zhifu = mock.Mock(return_value={None})
        # 根据支付结果测试页面跳转
        statues = zhifu.zhifu_status()
        self.assertEqual(statues, "未知错误异常")

    def test_04(self):
        "测试支付 Error 服务器返回异常"
        # mock 一个支付 Error 服务器返回异常
        zhifu.zhifu = mock.Mock(return_value={})
        # 根据支付结果测试页面跳转
        statues = zhifu.zhifu_status()
        self.assertEqual(statues, "Error 服务器返回异常")



if __name__ == '__main__':
    unittest.main(verbosity=2)

