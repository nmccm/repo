from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url='https://www.balaan.co.kr/shop/main/index.php')


driver.find_element(By.CLASS_NAME, 'header-subCategory__item').click()
# driver.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys("tistory")
# driver.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys(Keys.ENTER)

# 