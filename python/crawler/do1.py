#-*-codeing:utf-8-*-
import os
from selenium import webdriver
from webdirver_manager.chrome import ChromeDriverManager

URL = 'https://www.gopax.co.kr/exchange/btc-krw'

def crawl(self):
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get(URL)

    m = driver.find_element_by_class_name("info_area")
    print(m.text)


