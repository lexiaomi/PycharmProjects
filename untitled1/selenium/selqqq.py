#user/bin/lilijun


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
    input = browser.find_element_by_id('kw')
    input.send_keys('陈冠希')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()
#获取百度搜索

#淘宝搜索 （元素交互动作）
from selenium import  webdriver
import  time
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('蓬蓬裙')
time.sleep(1)
button = browser.find_element_by_class_name('btn-search')
input.clear()
input.send_keys('仙女裙')
button = browser.find_element_by_class_name('btn-search')
button.click()

# 隐式等待
"""from selenium import  webdriver
browser = webdriver.Chrome()
browser.implicitly_wait(10)#隐式等待调用方法
browser.get('https://www.zhihu.com/explore')
input = browser.find_elements_by_class_name('zu-top-add-question')
print('input')"""
