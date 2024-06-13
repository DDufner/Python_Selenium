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

windowId = driver.current_window_handle
print(windowId)

driver.find_element(By.XPATH, "//button[@onclick='myFunction()']").click()
windowIDs = driver.window_handles
parentWindow = windowIDs[0]
childWindow = windowIDs[1]

driver.switch_to.window(childWindow)
time.sleep(5)
driver.switch_to.window(parentWindow)
#driver.close()
time.sleep(2)

for wID in windowIDs:
    driver.switch_to.window(wID)
    print("page: ", driver.title)

print("test done")