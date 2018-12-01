# 抓取澎湃新闻练习 -- 完成
# 澎湃新闻有下拉更新，交互练习 -- 完成
# 存储到文本文件当中
# （MongoDB）可视化 MYSQL?

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
            for i in range(1, 3):
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
        title = item.find('h2>a').text()
        news = item.find('p').text()
        author = item.find('.pdtt_trbs>a').text()
        times = item.find('span').text()
        file = open('pengpai.txt', 'a', encoding='utf-8')
        file.write('\n'.join([title, news, author, times]))
        file.write('\n' + '=' * 50 + '\n')
        file.close()


def main():
    index_page()


if __name__ == '__main__':
    main()