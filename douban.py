# 爬取豆瓣最受欢迎书评

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser, 10)


def get_page():
    try:
        url = 'https://book.douban.com/review/best/'
        browser.get(url)
        get_product()
    except TimeoutException:
        get_page()


def get_product():
    html = browser.page_source
    doc = pq(html)
    items = doc('.book-content .article .review-list .review-item').items()
    for item in items:
        product = {
            'name': item.find('.main-hd .name').text(),
            'time': item.find('.main-hd .main-meta').text(),
            'text': item.find('.main-bd .short-content').text(),
        }
        print(product)


def main():
    get_page()


if __name__ == '__main__':
    main()