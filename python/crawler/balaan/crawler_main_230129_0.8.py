from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pymysql
from datetime import datetime

def getConne():
    return pymysql.connect(host='175.126.232.100', user='devteam', password='qwe123!@#', db='corsomilano', charset='utf8')

def getProducts(url):    
    print(url)
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    return driver.find_elements(By.CLASS_NAME, "info_area")




# productCnt = 0
# todayMonth = str(datetime.today().month)
# todayMonth = todayMonth if len(todayMonth) == 2 else '0' + todayMonth
# todayDay = str(datetime.today().day)
# todayDay = todayDay if len(todayDay) == 2 else '0' + todayDay
# currentDate = str(datetime.today().year) + "-" + str(todayMonth) + "-" + str(todayDay)
# conn = getConne()
# cur = conn.cursor()
# domain = "https://www.balaan.co.kr/"

# targetUrl = [
#     'shop/goods/goods_list.php?page=nmccm&sort=pageview&f_price%5BisSet%5D=n&f_price%5Bmin%5D=0&f_price%5Bmax%5D=9000000&category=009002&size=80&keyword=', # 의류
#     'shop/goods/goods_list.php?page=nmccm&sort=pageview&f_price%5BisSet%5D=n&f_price%5Bmin%5D=0&f_price%5Bmax%5D=9000000&category=009003&size=80&keyword=', # 슈즈
# ]

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





