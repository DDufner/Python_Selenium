from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/chromedriver')

chrome_options = Options()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("ninja")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "wikipedia-search-button").click()
time.sleep(1)

linkListLength = len(driver.find_elements(By.ID, "wikipedia-search-result-link"))

#for link in linkListLength:
#driver.find_element(By.ID, "wikipedia-search-result-link").click()

#driver.find_elements(By.XPATH, "//id=wikipedia-search-result-link/ancestor::tr/following-sibling::*")
#linkList = driver.find_elements(By.XPATH, "//div[id='wikipedia-search-result-link']/a")
linkList = driver.find_elements(By.XPATH, "//a[contains(text(),'Ninja')]")

#word = linkList.get_attribute('value')
#print("word", word)

for link in linkList:
    link.click()
    print("window ID:", driver.current_window_handle)
    print("window title:", driver.title)
    
time.sleep(5)
print("end")
#assignment
#search in wiki box.
#capture all links
#click each link 
#get window id of eac window tab
#go through all tabs and print titles
#close all windows when done