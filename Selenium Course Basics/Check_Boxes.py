import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

driver.get("http://the-internet.herokuapp.com/checkboxes")

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.click()

# check selected checkboxes only.
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()


time.sleep(10)