from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Crawler
loopCnt = 1

while loopCnt < 3:
    url1 = 'https://www.balaan.co.kr/shop/goods/goods_list.php?page='    
    url = url1 + str(loopCnt) + '&sort=pageview&f_price%5BisSet%5D=n&f_price%5Bmin%5D=0&f_price%5Bmax%5D=3000000&category=009002&size=40&keyword='    
    print(url)        
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

    tmp = driver.find_elements(By.CLASS_NAME, "info_area")
    len1 = len(tmp)
    print(f'---------------------------- count : {len1}')    

    for i in tmp:
        text = i.text
        print(f'({loopCnt})==================================')
        print(text)

    loopCnt = loopCnt + 1

