from bs4 import BeautifulSoup
import requests
import time

#URL = "http://backoffice.letsmilan.co.kr"
#URL = "https://www.balaan.co.kr/shop/goods/goods_list.php?page=1&sort=pageview&f_price%5BisSet%5D=n&f_price%5Bmin%5D=0&f_price%5Bmax%5D=3000000&category=009002&size=40&keyword="
#page = requests.get(URL)
#soup = BeautifulSoup(page.content, "html.parser")

#h1_tag = soup.find("div")  
#div = soup.select('div')
# print(div)  

url = "http://dev-backoffice.letsmilan.co.kr/login?a=1"
page = requests.get(url)