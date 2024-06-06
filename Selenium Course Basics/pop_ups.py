import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/chromedriver')

chrome_options = Options()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")


#alternate method that ignores extra spaces:
#driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()

time.sleep(2)

driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alertWindow = driver.switch_to.alert
alertWindow.accept()
time.sleep(1)
print("alert completed")

driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
alertWindow = driver.switch_to.alert
alertWindow.dismiss()
time.sleep(1)
print("confirm closed")

driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
alertWindow = driver.switch_to.alert
alertWindow.send_keys("Ima gigantic brain!")
alertWindow.accept()
time.sleep(1)
#alertWindow.dismiss()
print("confirm prompt")

alertButtons = driver.find_elements(By.XPATH, "//button")


for button in alertButtons:
    button.click()
    alertWindow = driver.switch_to.alert
    alertWindow.dismiss()
    print("completed "+button.text+" prompt")

#automatica authentication pop-up modal: enter user and pw values in URL

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(5)
