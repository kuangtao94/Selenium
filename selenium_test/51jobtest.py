from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as t
from pyquery import PyQuery as pq
import re
from TestCase.Selenium_test.selenium_test.config import  *
import pymongo

#对MonGoDB进行实例化操作
client = pymongo.MongoClient(MONGO_URL)
#连接MongoDB数据库
db = client[MONGO_DB]

#浏览器实例化
# driver = webdriver.PhantomJS(service_args=SERVICE_ARGS)
option = webdriver.ChromeOptions()
option.add_argument("headless")
driver = webdriver.Chrome(chrome_options=option)

driver.set_window_size(1400,900)
driver.maximize_window()
driver.implicitly_wait(10)
#显示等待
wait = WebDriverWait(driver,10)

def search():
    print("正在搜索")
    try:
        driver.get("https://www.51job.com/")
        element = wait.until(
            EC.presence_of_element_located((By.ID,"kwdselectid"))
        )
        element.send_keys(KEYWORD)
        # 取消选中城市
        driver.find_element_by_id("work_position_input").click()
        t.sleep(2)
        selectedCityEles = driver.find_elements_by_css_selector(
            "#work_position_click_center_right_list_000000 em[class=on]"
        )
        for one in selectedCityEles:
            # print(one.text)
            one.click()
        # 选中城市
        t.sleep(2)
        driver.find_element_by_id("work_position_click_center_right_list_category_000000_040000").click()
        t.sleep(2)
        driver.find_element_by_id("work_position_click_bottom_save").click()
        #点击搜索
        t.sleep(2)
        driver.find_element_by_css_selector("body > div.content > div > div.fltr.radius_5 > div > button").click()
        # submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > div.dw_wp > form > div > div.dw_search_in > button")))
        # submit.click()
        #总计页数
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#resultList > div.dw_page > div > div > div > span:nth-child(2)")))
        # get_products()
        return total.text
    except Exception:
        return search()

def next_page(page_number):
    print("正在翻页",page_number)
    try:
        element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#jump_page"))
        )
        element.clear()
        element.send_keys(page_number)
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#resultList > div.dw_page > div > div > div > span.og_but")))
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#resultList > div.dw_page > div > div > div > ul > li.on"),str(page_number)))
        get_products()
    except Exception:
        next_page(page_number)

def get_products():
    # jobs = driver.find_elements_by_css_selector("#resultList div[class=el]")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#resultList div[class=el]")))
    html = driver.page_source
    doc = pq(html)
    items = doc("#resultList div[class=el]").items()
    for item in items:
        product = {
            "职位":item.find(".t1").text(),
            "公司":item.find(".t2").text(),
            "工作点":item.find(".t3").text(),
            "薪资":item.find(".t4").text(),
            "发布时间":item.find(".t5").text()
        }
        print(product)
        save_to_mongo(product)

def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print("存储到MONGODB成功",result)
    except Exception:
        print("存储到MONGODB失败",result)

def main():
    try:
        total = search()
        total = int(re.compile("(\d+)").search(total).group(1))
        print(total)
        for i in range(2,total + 1):
            next_page(i)
    except Exception:
        print("出错")
    finally:
        driver.quit()
if __name__ == '__main__':
    main()

    # for job in jobs:
    #     findles = job.find_elements_by_tag_name("span")
    #     stringfinds = [findle.text for findle in findles]
    #     print("|".join(stringfinds))

# def test():
#     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#resultList div[class=el]")))
#     html = driver.page_source
#     doc = pq(html)
#     items = doc("#resultList div[class=el]").items()
#     for item in items:
#         product = {
#             "image":item.find("xxxxx").attr("xxx"),
#             "price":item.find("xxxx").text(),
#             "deal":item.find("xxx").text()[:-3],
#             "title":item.find("xxxx").text(),
#             "shop":item.find("xxxx").text(),
#             "location":item.find("xxxx").text()
#         }
#         print(product)
