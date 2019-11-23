import ddt
import requests
import unittest

"""通过接口测试的技术获取拉钩网平台的资料"""
url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
def getHeaders():
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Cookie": "JSESSIONID=ABAAABAAAIAACBI2438D04CF91400F1FF0A2B38358AFFA5; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1550930753; _ga=GA1.2.193872554.1550930753; _gat=1; user_trace_token=20190223220617-301cdfdc-3774-11e9-af96-525400f775ce; LGSID=20190223220617-301ce139-3774-11e9-af96-525400f775ce; PRE_UTM=; PRE_HOST=cn.bing.com; PRE_SITE=https%3A%2F%2Fcn.bing.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20190223220617-301ce2a8-3774-11e9-af96-525400f775ce; _gid=GA1.2.1796885419.1550930753; index_location_city=%E5%85%A8%E5%9B%BD; SEARCH_ID=a0ad1593bd14438d8a205a17a17f95c1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1550930826; LGRID=20190223220730-5b9c7593-3774-11e9-af96-525400f775ce; TG-TRACK-CODE=search_code",
        "Referer": "https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput="
    }
    return headers
"""
测试类前加修饰@ddt.ddt
case前加修饰@ddt.data() 相同的测试用例
@ddt.unpack 分解data的参数
"""
@ddt.ddt
class Ddt(unittest.TestCase):
    @ddt.data((1,),(2,),(3,))  #指页数
    @ddt.unpack
    def test_lagou(self,page):
        r = requests.post(
            url=url,
            headers=getHeaders(),
            data={"first": False,"pn": page,"kd": "自动化测试工程师"})
        print(r.text)
        self.assertEqual(r.json()["success"],True)
        print(r.json()["content"]["positionResult"]["result"][0]["city"])
if __name__ == '__main__':
    unittest.main(verbosity=2)




