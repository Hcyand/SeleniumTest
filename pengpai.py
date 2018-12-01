# 抓取澎湃新闻练习 -- 完成
# 澎湃新闻有下拉更新，交互练习 -- 完成

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
import time


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)


def index_page():
    try:
        url = 'https://www.thepaper.cn/channel_25950'
        browser.get(url)
        try:
            # 下拉进度条，新闻刷新。循环6次，等待时间6秒
            for i in range(1, 6):
                browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                time.sleep(6)
        except Exception as ex:
            print(ex)
        get_products()
    except TimeoutException:
        index_page()


def get_products():
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainContent .news_li').items()
    for item in items:
        product = {
            '标题': item.find('h2>a').text(),
            '内容': item.find('p').text(),
            '发布者': item.find('.pdtt_trbs>a').text(),
            '发布时间': item.find('span').text()
        }
        print(product)


def main():
    index_page()


if __name__ == '__main__':
    main()