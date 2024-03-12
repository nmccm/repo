from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pymysql
from datetime import datetime


print('start....')
url = "https://www.balaan.co.kr/products?searchType=search&keyword=KCB384TFL+S900&page=1&lowest=Y"

print(url)
driver = webdriver.Chrome()
driver.get(url)

time.sleep(5)

try:
    driver.execute_script("var elements = document.getElementsByClassName('popup_wrapper'); for(var i = 0; i < elements.length; i++) { var element = elements[i]; element.parentNode.removeChild(element); }")
    time.sleep(2)
    main = driver.find_elements(By.CLASS_NAME, "product-list-wrap")
    print('-------------- find start -----------')
    print(main)
    loopCnt = 1
    for i in main:
        print(i.text.getText())
        loopCnt = loopCnt + 1
    print('-------------- find end -----------')    
except Exception as e:
    print("error", e)



    

def getConne():
    return pymysql.connect(host='175.126.232.100', user='devteam', password='qwe123!@#', db='corsomilano', charset='utf8')

def getProducts(url):    
    print(url)
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(5)
    #return driver.find_elements(By.CLASS_NAME, "info_area")
    #return driver.find_elements(By.CLASS_NAME, "product-item")

    try:
        div_element = driver.find_elements(By.ID, "main")
        print('-------------- find start -----------')
        print(div_element)
        print('-------------- find end -----------')
        # driver.execute_script("var elements = document.getElementsByClassName('popup_wrapper'); for(var i = 0; i < elements.length; i++) { var element = elements[i]; element.parentNode.removeChild(element); }")
    except Exception as e:
        print("error", e)

    #return driver.find_elements(By.CLASS_NAME, "product-item")
    return div_element




productCnt = 0
todayMonth = str(datetime.today().month)
todayMonth = todayMonth if len(todayMonth) == 2 else '0' + todayMonth
todayDay = str(datetime.today().day)
todayDay = todayDay if len(todayDay) == 2 else '0' + todayDay
currentDate = str(datetime.today().year) + "-" + str(todayMonth) + "-" + str(todayDay)
# conn = getConne()
# cur = conn.cursor()
domain = "https://www.balaan.co.kr/"

targetUrl = [
    'shop/pc2m.php?landing_url=/products?searchType=search&keyword=KCB384TFL+S900', # B 최저가
]

# for tmpUrl in targetUrl:
#     loopCnt = 1        
#     while loopCnt < 50000: 
#         url = domain + tmpUrl.replace("nmccm", str(loopCnt))    
#         products = getProducts(url)
#         productCnt = len(products)
#         forLoopCnt = 1
#         if productCnt > 0:
#             for i in products:
#                 print(f'== count : {str(forLoopCnt)} / {productCnt}')            
#                 text = i.text                
#                 query = "insert into crawler_raw (url, content, page, c_datetime) values('" + url + "', '" + text.replace("'", "") + "', '" + str(loopCnt) + "', now())"                
#                 print(query) 
#                 cur.execute(query)        
#                 conn.commit()
#                 forLoopCnt = forLoopCnt + 1
#         else:
#             print(f'== count : {productCnt}')            
#             forLoopCnt = 1
#             loopcnt = 50000        
#         loopCnt = loopCnt + 1        
#     print('end...')
# conn.close()



