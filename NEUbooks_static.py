from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    browser.get('http://202.118.8.7:8991/F/-?func=bor-info')
    input1 = browser.find_element_by_name('bor_id')
    input1.send_keys('1801769')
    input2 = browser.find_element_by_name('bor_verification')
    input2.send_keys('801769')
    input2.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    x = browser.find_elements_by_tag_name('td')
    i = 34
    while i < 38:
        print(x[i].text, '：', x[i + 1].text, '本')
        i = i + 2
finally:
    browser.close()
