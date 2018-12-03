# 爬取知乎热榜内容
# 标题，内容，热度
# 需要模拟登录

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)


def get_page():
    try:
        url = "https://www.zhihu.com/hot"
        browser.get(url)
        get_product()
    except TimeoutException:
        get_page()


def get_product():
    html = browser.page_source
    doc = pq(html)
    items = doc('#Topstory .HotList .HotItem').items()
    for item in items:
        product = {
            '标题': item.find('.HotItem-content .HotItem-title').text(),
            '内容': item.find('.HotItem-content .HotItem-excerpt').text(),
            '热度': item.find('.HotItem-metrics').text(),
        }
        print(product)


def main():
    get_page()


if __name__ == '__main__':
    main()