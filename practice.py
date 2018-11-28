# 未完成***

# 目标：利用Selenium爬取优品ppt的ppt
# 并用pyquery解析得到的ppt的名称，页数，查看人数，静态或动态
# 并保存至MongoDB

import pymongo
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from urllib.parse import quote

MONGO_URL = 'localhost'
MONGO_DB = 'ppt'
MONGO_COLLECTION = 'products'

KEYWORD = 'jingmei'

MAX_PAGE = 4

SERVICE_ARGS = ['--disk-cache=true']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

wait = WebDriverWait(browser, 10)
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def index_page(page):
    print('正在爬取第', page, '页')
    try:
        url = 'http://www.ypppt.com/moban/jingmei/'
        browser.get(url)
        if page > 1:
            submit = browser.find_element(By.LINK_TEXT, '下一页')
            submit.click()
        wait.until(
          wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.posts.clear li')))
        )
        get_products()
    except TimeoutException:
        print('error')


def get_products():
    lis = browser.find_elements(By.CSS_SELECTOR, '.posts.clear li')
    for li in lis:
        product = {
            'title': li.find('p-title').text(),
            'left': li.find('left').text(),
            'right': li.find('right').text(),
        }
        print(product)
        save_to_monge(product)


def save_to_monge(result):
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到mongoDB成功')
    except Exception:
        print('存储到mongoDB失败')


def main():
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
    browser.close()


if __name__ == '__main__':
    main()