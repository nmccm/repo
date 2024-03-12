import requests

URL = "http://backoffice.letsmilan.co.kr"
page = requests.get(URL)
print(page.content)  