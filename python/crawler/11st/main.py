from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from bs4 import BeautifulSoup as bs
from urllib import parse
from openpyxl import Workbook

driver = webdriver.Chrome()
checkIndex = 0
workbook = Workbook()
sheet = workbook.active
sheet['A1'] = "상품명"    
sheet['B1'] = "정상가"    
sheet['C1'] = "판매가"    
sheet['D1'] = "이미지" 
sheet['E1'] = "URL" 















# 3334
for num in range(1, 100):
    urlPrefix = "https://shop.11st.co.kr/stores/2476/search?searchKwd=&sortCd=N&filter=&pageNo=" + str(num)
    url = urlPrefix + ""
    # print('url : ' + url)
    driver.get(url)
    time.sleep(1)        
    plist = driver.find_elements(By.CLASS_NAME, "store_product_item")

    for i in plist :        
        checkIndex = checkIndex + 1
        htmlStr = str(i.get_attribute('innerHTML'))
        # print(str(checkIndex) + ' : ' + htmlStr)    
        soup = bs(htmlStr, "html.parser")
        imgUrl = ''
        productName = ''
        productPrice = ''
        productDiscountPer = "-"

        if 'class="store_product_thumb_wrap"' in htmlStr :        
            tmpImgUrl = soup.select_one('div.store_product_thumb_wrap')
            tmp1 = str(tmpImgUrl).split(sep='https')
            tmp1 = str(tmp1[2]).replace('"', '').replace('</div>', '').replace('/>', '')
            imgUrl = 'https' + str(tmp1).replace('\n', '')   

            tmp1 = str(tmpImgUrl).split(sep='alt')
            tmp1 = str(tmp1[1]).split(sep='"')
            productName = tmp1[1].replace('\n', '')
            
        if 'class="store_product_price_area"' in htmlStr :
            tmpPrice = soup.select_one('span.store_product_price_area').get_text()        
            price = str(tmpPrice).replace('\n', '').split(sep='원')

        print('-----')
        print(f'{checkIndex} url => {imgUrl}')
        print(f'{checkIndex} productName => {productName}')    
        print(f'{checkIndex} productPrice => {price[0].replace('정상가', '')}')
        print(f'{checkIndex} productPrice => {price[1].replace('판매가', '')}')

        sheet.append([
            str(productName), 
            str(price[0].replace('정상가', '')), 
            str(price[1].replace('판매가', '')), 
            str(imgUrl),
            str(url)
        ])

workbook.save("result.xlsx")            





