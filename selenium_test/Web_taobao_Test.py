from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
def search():
    try:
        driver.get("https://www.taobao.com")
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#q")))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_TSearchForm > div.search-button > button")))
        input.send_keys("美食")
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > div.total")))
        return total.text
    except TimeoutError:
        return search()

def next_page(page_number):
    try:
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > div.form > input")))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit")))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > ul > li.item.active > span"))).str(page_number)
    except TimeoutError:
        next_page(page_number)




def main():
    total = search()
    total = int(re.compile("(\d+)").search(total).group(1))
    for item in range(2,total+1):
        next_page(item)

if __name__ == "__main__":
    main()


