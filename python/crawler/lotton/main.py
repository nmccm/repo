from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pymysql
from datetime import datetime
from bs4 import BeautifulSoup as bs
from urllib import parse
import sys

def getConne() :    
    # return pymysql.connect(host='175.126.232.100', user='devteam', password='qwe123!@#', db='corsomilano', charset='utf8') # 개발서버
    return pymysql.connect(host='110.10.129.37', user='devteam', password='qwe123!@#', db='legacy', charset='utf8') # 운영서버

driver = webdriver.Chrome()
urlPrefix = "https://www.lotteon.com/p/display/shop/seltDpShop/29675?callType=menu"
url = urlPrefix + ""
print('url : ' + url)
driver.get(url)
time.sleep(2)        
driver.find_element(By.XPATH, "//*[@id='main-tab-button-FC05000000']").click()
time.sleep(2)    
plist = driver.find_elements(By.CLASS_NAME, "s-goods-grid__item")
checkIndex = 0
conn = getConne()
cur = conn.cursor()

for i in plist :        
    checkIndex = checkIndex + 1
    htmlStr = str(i.get_attribute('innerHTML'))
    soup = bs(htmlStr, "html.parser")
    productName = ''
    productPrice = ''
    productDiscountPer = "-"

    if 'class="s-goods-title"' in htmlStr :
        productName = soup.select_one('div.s-goods-title').get_text()

    if 'class="s-goods-price__discount"' in htmlStr and 'class="s-goods-price__number"' in htmlStr :
        productDiscountPer = soup.select_one('span.s-goods-price__discount > span.s-goods-price__number').get_text()        

    if 'class="s-goods-price__final"' in htmlStr and 'class="s-goods-price__number"' in htmlStr :        
        productPrice = soup.select_one('strong.s-goods-price__final > span.s-goods-price__number').get_text()

    print(f'{checkIndex} Result => {productName}, {productPrice}, {productDiscountPer}')
    query = "insert into crawler_raw (url, content, org_content, product_name, product_price, product_discount_per, c_datetime) values("            
    query += "'" + url + "', " 
    query += "'" + htmlStr.replace("'", "").replace('"', '') + "', " 
    query += "'" + htmlStr.replace("'", "").replace('"', '') + "', " 
    query += "'" + productName.replace("'", "").replace('"', '') + "', " 
    query += "'" + productPrice.replace("'", "").replace('"', '').replace(',', '').replace('원', '') + "', " 
    query += "'" + productDiscountPer.replace("'", "").replace('"', '').replace('%', '') + "', " 
    query += "now())" 
#     # print(query)

    cur.execute(query)        
    conn.commit()        

conn.close()            
