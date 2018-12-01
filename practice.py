# 未完成***
# 为什么爬取不了？？？
# 页面跳转问题解决

# 目标：利用Selenium爬取优品ppt的ppt
# 并用pyquery解析得到的ppt的名称，页数，查看人数，静态或动态
# 并保存至MongoDB


from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
import time

MAX_PAGE = 1
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)


def index_page(page):
    try:
        if page == 1:
            url = 'http://www.ypppt.com/moban/jingmei/'
        else:
            url = 'http://www.ypppt.com/moban/jingmei/list-' + str(page) + '.html'
        browser.get(url)
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    # 当前页面商品
    html = browser.page_source
    doc = pq(html)
    items = doc('#menu .clear')
    print(items)


def main():
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
        time.sleep(5)


if __name__ == '__main__':
    main()