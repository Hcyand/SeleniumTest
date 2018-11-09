from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
# 动作链联练习
browser.switch_to.frame('iframeResult')
# 拖拽位置
source = browser.find_element_by_css_selector('#draggable')
# 目标位置
target = browser.find_element_by_css_selector('#droppable')
# 声明ActionChains对象并赋值为actions变量
actions = ActionChains(browser)
# 调用执行拖拽动作
actions.drag_and_drop(source, target)
actions.perform()