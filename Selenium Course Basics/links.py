import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests as requests 

chrome_options = Options()
service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

driver.get("http://demo.nopcommerce.com/")

driver.find_element(By.LINK_TEXT, "Digital downloads").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()

links = driver.find_elements(By.TAG_NAME, "a")

print(len(links))

for link in links:
    print(link.text)

time.sleep(10)

# Broken Links
# installed 'requests' package at PyCharm->settings->project->project interpreter->'+' icon->search list and install.
driver.get("http://www.deadlinkcity.com/")

