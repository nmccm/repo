from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.balaan.co.kr/products?searchType=search&keyword=KCB384TFL+S900&page=1&lowest=Y"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

try:

    driver.execute_script("var elements = document.getElementsByClassName('popup_wrapper'); for(var i = 0; i < elements.length; i++) { var element = elements[i]; element.parentNode.removeChild(element); }")

    time.sleep(2)

    product_items = driver.find_elements(By.CLASS_NAME, "click-area")
    #product_items = driver.find_elements(By.CLASS_NAME, "product-item")
    #product_items = driver.find_elements(By.CLASS_NAME, "sort-wrap")

    for item in product_items:
        print(item.text)

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()



