from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pymysql
from datetime import datetime
from bs4 import BeautifulSoup as bs
from urllib import parse
import sys

def getConne():    
    # return pymysql.connect(host='175.126.232.100', user='devteam', password='qwe123!@#', db='corsomilano', charset='utf8') # 개발서버
    return pymysql.connect(host='110.10.129.37', user='devteam', password='qwe123!@#', db='legacy', charset='utf8') # 운영서버

driver = webdriver.Chrome()
urlPrefix = "https://www.ssg.com"
url = urlPrefix + "/service/bestMain.ssg?zoneId=6000242397"
print('url : ' + url)
driver.get(url)
time.sleep(2)        
# executeScriptStr = """ 
#     var elements = document.getElementsByClassName('popup_wrapper');
#     for(var i = 0; i < elements.length; i++) {
#         var element = elements[i]; element.parentNode.removeChild(element); 
#     }
# """
# driver.execute_script(executeScriptStr)
# time.sleep(1)    
plist = driver.find_elements(By.CLASS_NAME, "cunit_info")
checkIndex = 0
conn = getConne()
cur = conn.cursor()

for i in plist:        
    checkIndex = checkIndex + 1
    htmlStr = str(i.get_attribute('innerHTML'))
    soup = bs(htmlStr, "html.parser")
    productName = ''
    productPrice = ''
    productDiscountPer = "-"

    if 'em class="tx_ko"' in htmlStr:
        productName = soup.select_one('a > em.tx_ko').get_text()

    if 'em class="ssg_price"' in htmlStr:
        productPrice = soup.select_one('em.ssg_price').get_text()

    print(f'{checkIndex} Result => {productName}, {productPrice}, {productDiscountPer}')
    query = "insert into crawler_raw (url, content, org_content, product_name, product_price, product_discount_per, c_datetime) values("            
    query += "'" + url + "', " 
    query += "'" + htmlStr.replace("'", "").replace('"', '') + "', " 
    query += "'" + htmlStr.replace("'", "").replace('"', '') + "', " 
    query += "'" + productName.replace("'", "").replace('"', '') + "', " 
    query += "'" + productPrice.replace("'", "").replace('"', '').replace(',', '').replace('원', '') + "', " 
    query += "'" + productDiscountPer.replace("'", "").replace('"', '').replace('%', '') + "', " 
    query += "now())" 
    # print(query)

    cur.execute(query)        
    conn.commit()        

conn.close()            



