from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import openpyxl

def f(x):
    browser = webdriver.PhantomJS()
    browser.get('http://202.118.8.7:8991/F/-?func=bor-info')
    input1 = browser.find_element_by_name('bor_id')
    input1.send_keys(x)
    input2 = browser.find_element_by_name('bor_verification')
    y = str(int(x)%1000000)
    input2.send_keys(y)
    input2.send_keys(Keys.ENTER)
    book = browser.find_elements_by_tag_name('td')
    return book[35].text, book[37].text


wb = openpyxl.load_workbook('NEUlib_phantomjs.xlsx')
sheet = wb['Sheet1']
#print(sheet['A1'].value)
#print(f('1801670'))    #借书超期警告
for i in list(sheet.columns)[0]:
    print(i.value, f(str(i.value)))
