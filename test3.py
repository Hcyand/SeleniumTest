from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')

# 查找单个节点 输入框
input_first = browser.find_element_by_id('q')
print(input_first)

# 查找多个节点 导航栏
input_second = browser.find_elements_by_class_name('J_Cat')
print(input_second)

# 节点交互
input = browser.find_element_by_id('q')
# 输入iphone
input.send_keys('iphone')
# 等待一秒
time.sleep(1)
# 清空输入框
input.clear()
# 输入ipad
input.send_keys('ipad')
button = browser.find_element_by_class_name('btn-search')
# 完成搜索动作
button.click()
