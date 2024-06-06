from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 
service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/chromedriver')

chrome_options = Options()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

driver.get("http://the-internet.herokuapp.com/dropdown")

#country_dropdown = driver.find_element(By.XPATH, "//select[@id='input-country']")
dropdown_select = Select(driver.find_element(By.XPATH, "//select[@id='dropdown']"))

all_options = dropdown_select.options

#selection methods:
dropdown_select.select_by_visible_text("Option 1")
dropdown_select.select_by_value("2")
dropdown_select.select_by_index(1)
for option in all_options:
    if option.text=="Option 1":
        option.click()
        break

print("total number of options: ", len(all_options))

for option in all_options:
    print(option.text)