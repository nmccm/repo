from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pymysql
from datetime import datetime
from bs4 import BeautifulSoup as bs
from urllib import parse

def getConne():
    return pymysql.connect(host='175.126.232.100', user='devteam', password='qwe123!@#', db='corsomilano', charset='utf8')

kwdList = [
    "XXW00G0DE50NHV B999","XXM0GW05470RE0 B608 7","XXM0GW05470RE0 C405","XXM64C00640RE0 C405","XXW79A0DE70MID B001","XXW79A0DE70MID B999",
    "XXW79A0HM60MBW B999","XXM0GW05470EK0 B999",
    "XXW0FW050305J1 9996","6231775","6300068","6231539","6226438","6301346","6235350","6218025","6224892","6235347","6218031","6238773","6235331",
    "6238781","6234604","6232155","6235329",
    "6302087","6220467","6240275","6221811","6238961","6232048","6301349","6227997","6236963","6224218","6231961","6300743","6218067","6238780",
    "6301933","6238969","6231539(127866) 6.5","6228860",
    "6300409","6302087(121347)","6237301","6300097","6301887","6224892(144747)","M1A 4950 BMULKE 79","M1A 4768 BMULTI 79","M1AOCK APACKM 92","M1A 4832 BMULTI 79","M1A 4950 BMULKE 66",
    "M1A 6711 FMULTR 79","M1A 6751 BMULTI 79","M1A 5022 BMULTI 79","M1A 4774 BMULTI 79","M2R 011R KZEBRA 79","M1A 4768 GCOVGA 79","M1A 4768 FMINSP 79","M1A 4832 HMINST 79","M2R 011R KZEBRA 01",
    "M1A 4768 KMINTI 79","M1A 4768 HMINST 79","M1A768 FMULTR 79","M1A768 AMINRC PR","M2R 011R AZEBRA 79","M1A950 BMULKE 662","M2S DAL06 AEVA 79","M1A 239D A40674 92","M1A780 AMULTI 78",
    "M1A 2871N AMULTB 92","M1A 167N AMULTB 92","M1A 4832 KMINTI 79","M1A833 GCOVGA 79","M1A774 FMINSP 79","M1A950 BMULKE 66(097799)4","M1A832 BMULTI 79(110051)","M1A54D AS22 79",
    "M1A950 BMULKE 664","M1A833 FMINSP 79","M1A 868F GS10 79","M1A 6751 BMULTI 79(115129)","M1A832 BMULTI 79(140764)","M1A832 BMULTI 79(114609)","M1A774 BMULTI 79(105004)",
    "M1A950 BMULKE 66(099773)4","M1A950 BMULKE 66(099774)4","M1A950 BMULKE 66(112989)4","M1A950 BMULKE 66(113577)4","M1A950 BMULKE 66(106300)4","M1A950 BMULKE 79(105215)","M1A950 BMULKE 66(136623)4",
    "M1A950 BMULKE 66(097800)4","M1A95AMULKB 66(072873)2","M1A95AMULKE 79(054888)0","M1A95AMULKB 66(067006)4","M1AOCK APACKM 92(133361)","M1AOCK APACKM(112281) 6","M1AOCK APACKM 92(105226)",
    "M2S DAL06 AEVA 79(111150)","M2R 011R AZEBRA 79 (110042)","M1A 4950 BMULKE 79(144238)","JX02 WHITE BLACK EU1","CX01ULTI KAKI EU","POUCHULTI BLUE","112 WHITE1","BX00ULTI CUBE EU","DW03 BWB",
    "POUCH B/W/BURGUNDY","CX01(105412)","BX0MULTI CUBE(073779)1","101 TRIM BE / NE(104286) EU","JX02 WHITE-BLACK(076584)","CX01 MULTI KAKI(114618)","LANCER 85 PAT.5","LANCER 85 PAT (110176)",
    "151AYLA","LANCER 85 GLE.5","LANCER 85 PAT NUDE(105417).5","ROMY 60 XRT BLACK.5","MIMI PAT GRAY(097756).5","MIMI PAT BLACK(022746)","C D024 6000 0010","C W004 6000 0010(036649)",
    "1G158Q1739Z99 BLACK","1G158S1739Z99 BLACK","1G158S1739Z00 WHITE","FP65234T5228 003","HP56202J I6257 725(061374)3","65154004 JKA004 A04 995 50","FP66239T A6296 090(095325)","FP66239T A6296 090(096770)",
    "FP64212T D4229 005","J071304401555","H009L01 SP21 001","40F2FHFB5L 001(099765)","40S3SDFA1Q8 011493","40F2FHFB5L 001(104284)","887879 EK08 AM1 A25(088046)","26168852","26156605","I031410 K02XX"    
]

kwdList = [
    "XXW00G0DE50NHV B999","6224892"
]

driver = webdriver.Chrome()
conn = getConne()
cur = conn.cursor()

for item in kwdList:
    tmp = item.split(' ')

    if len(tmp) > 0 and len(tmp[0]) > 0:
        findKwd = tmp[0]
        urlPrefix = "https://www.balaan.co.kr/products"
        url = parse.urlparse(urlPrefix + "?keyword=" + item + "&page=1&lowest=Y")
        encodeQuery = parse.parse_qs(url.query)
        result = parse.urlencode(encodeQuery, doseq=True)
        url = urlPrefix + "?" + result        
        print('url : ' + url)
        driver.get(url)
        time.sleep(2)        
        executeScriptStr = """ 
            var elements = document.getElementsByClassName('popup_wrapper');
            for(var i = 0; i < elements.length; i++) {
                var element = elements[i]; element.parentNode.removeChild(element); 
            }
        """
        driver.execute_script(executeScriptStr)
        time.sleep(1)    
        plist = driver.find_elements(By.CLASS_NAME, "product-item")
        checkIndex = 0

        for i in plist:        
            checkIndex = checkIndex + 1
            isMatchB = 'nothing'
            isMatchKwd = isMatchB
            htmlStr = str(i.get_attribute('innerHTML'))

            if 'B 최저가' in htmlStr:
                isMatchB = 'match'

            if findKwd in htmlStr:
                isMatchKwd = 'match'                

            # print(f'{checkIndex} : b => {isMatchB}, kwd({findKwd}) => {isMatchKwd} ==============================================')                

            # if isMatchB == 'match':
            #     print(htmlStr)

            if 'B 최저가' in htmlStr and (findKwd in htmlStr or 'click-area' in htmlStr):
                # print(type(i.get_attribute('innerHTML')))
                # print(i.get_attribute('innerHTML'))            
                soup = bs(htmlStr, "html.parser")
                productName = productPrice = productDiscountPer = "???"

                if 'product-name' in htmlStr:
                    productName = soup.select_one('p.product-name').get_text()

                if 'price' in htmlStr:
                    productPrice = soup.select_one('span.price').get_text()

                if 'sale_percent' in htmlStr:
                    productDiscountPer = soup.select_one('span.sale_percent').get_text()                                    

                print(f'{checkIndex} execute => {productName}, {productPrice}, {productDiscountPer}')
                query = "insert into crawler_raw (kwd, url, content, org_content, product_name, product_price, product_discount_per, c_datetime) values("        
                query += "'" + item + "', " 
                query += "'" + url + "', " 
                query += "'" + htmlStr.replace("'", "").replace('"', '') + "', " 
                query += "'" + htmlStr.replace("'", "").replace('"', '') + "', " 
                query += "'" + productName.replace("'", "").replace('"', '') + " (" + item + ")', " 
                query += "'" + productPrice.replace("'", "").replace('"', '').replace(',', '').replace('원', '') + "', " 
                query += "'" + productDiscountPer.replace("'", "").replace('"', '').replace('%', '') + "', " 
                query += "now())" 
                # print('--------------')
                # print(query)
                cur.execute(query)        
                conn.commit()        
            # endif
        # endfor
    else:
        print(item + ' => split string length : ' + tmp.length + ', tmp[0] length error : ' + len(tmp[0]))
    # endif
#endfor

conn.close()            



