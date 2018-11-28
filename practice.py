# 未完成***
# 存在问题，可能是网页不规范导致
# 页面跳转问题没有解决

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
from selenium.webdriver import ActionChains
from urllib.parse import quote

MONGO_URL = 'localhost'
MONGO_DB = 'ppt'
MONGO_COLLECTION = 'products'

MAX_PAGE = 2

SERVICE_ARGS = ['--disk-cache=true']

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def index_page(page):
    print('正在爬取第', page, '页')
    try:
        url = 'http://www.ypppt.com/moban/jingmei/'
        browser.get(url)
        if page > 1:
            submit = browser.find_element_by_link_text('2')
            actions = ActionChains(browser)
            actions.click(submit)
        get_products()
    except TimeoutException:
        print('error')


def get_products():
    # 当前页面商品
    html = browser.page_source
    doc = pq(html)
    items = doc('.wrapper .posts.clear li').items()
    print(type(items))
    for item in items:
        print(type(item))


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