from selenium import webdriver
import time as t
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://www.cnblogs.com/Teachertao/")

# 添加cookie
c1 = {u'domain': u'.cnblogs.com',
      u'name': u'.CNBlogsCookie',
      u'value': u'BD99A6FDF11A861671409FD83A423902320DDF95794C8ACE23683B73942B920F24BDE575C30014E1315A20BD329AB3C93F6F9795473C1CBFFB58E8CC2D069FD1067CBA2AE259E7DC2683417ECA7DE3DC228E26F9',
      u'expiry': 1491887887,
      u'path': u'/',
      u'httpOnly': True,
      u'secure': False}

c2 = {u'domain': u'.cnblogs.com',
      u'name': u'.Cnblogs.AspNetCore.Cookies',
      u'value': u'CfDJ8D8Q4oM3DPZMgpKI1MnYlrn_hII7sjqtA9dj5XoGYuXBobEk1GsmY9Ld3pCrMr2X0hpVC8ie-mgE5_A7eassWL2YYO8VRr8Nv-4gfTtwLFViyr0Tc7P6-Fe5Y5RBw5mHIUFIQTSRsdku6zHKEoj4dF5Vrnt3smWB88VureD3kYlwLBDBzEmPs3TEv-5FriKv2KeLBue3W9GiwBTGjex6lkAutkhtdzUZRuDMpEdjpFvkdpjfadB2xVrvwehDtX3yZklgIdFXZZVRW_6oGqq3DB4LfKxjrTJ4RAan4AqiBLWCexQ9AvIDu9s5YXp3iZYV9OBNUdWsNYUZcgoaF3FvTl2NM37g5xSFJ8iPPW99grXt77DuoXRBzE-SfEC10OD9rTsqDWp_jpvMAR6NO6uns7UoJV0AgDxI6euoX5XeWbCE-LNzRIFEiIXWaAg4D6TWzA',
      u'expiry': 1491887887,
      u'path': u'/',
      u'httpOnly': True,
      u'secure': False}

driver.add_cookie(c1)  # 添加2个值
driver.add_cookie(c2)
t.sleep(3)

# 清除所有的cookie
driver.delete_all_cookies()
# 刷新下页面就见证奇迹了
driver.refresh()