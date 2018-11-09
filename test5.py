from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)

# 执行JavaScript
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')

# get_attribute()获取节点属性
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))

# text获得文本值
input = browser.find_elements_by_class_name('zu-top-add-question')
print(input.text)

# id属性获得节点id
# location属性获得节点页面相对位置
# tag_name属性获得标签名称
# size属性获得节点大小（宽高）
# back() 后退
# forward() 前进
# Selenium可以对Cookies进行操作
# try except 语句来捕获各种异常
