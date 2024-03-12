from bs4 import BeautifulSoup
import requests

URL = "http://backoffice.letsmilan.co.kr"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

#h1_tag = soup.find("div")  
div = soup.select('div')
print(div)  