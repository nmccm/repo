from bs4 import BeautifulSoup
import requests
import time

URL = "http://backoffice.letsmilan.co.kr"
URL = "https://www.balaan.co.kr/products?searchType=search&keyword=KCB384TFL+S900&page=1&lowest=Y"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

#h1_tag = soup.find("div")  
div = soup.select('div')
print(div)  