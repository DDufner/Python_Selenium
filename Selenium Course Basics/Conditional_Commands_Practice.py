import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

driver.get("https://demo.nopcommerce.com/register")

driver.maximize_window()

# is_displayed() : checks if element is present on webpage. returns true if present, if not, returns false.
#-needs to be used in reference to a web element and not in reference to the webdriver. e.g. element.is_enabled, NOT driver.is_enabled
# is_enabled() : checks if element can be interacted with e.g. enter text into text field, click button.  returns true or false.

search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Display status: ",search_box.is_displayed())
print("Enabled  status: ",search_box.is_enabled())

# is_selected() : checks if element is selected e.g. checkbox, radio button, link etc.  returns true or false.
male_radio_button = driver.find_element(By.XPATH, "//input[@id='gender-male']")
female_radio_button = driver.find_element(By.XPATH, "//input[@id='gender-female']")

male_radio_button.click()

newsletter_checkbox = driver.find_element(By.XPATH, "//input[@id='Newsletter']")
newsletter_checkbox.click()
time.sleep(3)
top_search_field = driver.find_element(By.XPATH, "//form[@id='small-search-box-form']")

print("Male radio selected status: ",male_radio_button.is_selected())
print("Female radio selected status: ",female_radio_button.is_selected())
print("Newsletter selected status: ",newsletter_checkbox.is_selected())
print("top search field status: ",top_search_field.is_enabled())
