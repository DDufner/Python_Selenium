import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/chromedriver')
chrome_options = Options()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

dobDay = "25"
dobMonth = "January"
dobMonth3Char = "Jan"
dobYear = "1990"

driver.find_element(By.ID, "product_3186").click()
driver.find_element(By.ID, "travname").send_keys("firstname")
driver.find_element(By.ID, "travlastname").send_keys("lastname")
driver.find_element(By.ID, "order_comments").send_keys("some random notes")
driver.find_element(By.ID, "dob").click()
datepickerMonth = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
datepickerMonth.select_by_visible_text(dobMonth3Char)
driver.find_element(By.CLASS_NAME, "ui-datepicker-year").click()
driver.find_element(By.XPATH, "//option[contains(text(),'"+dobYear+"')]").click()
allDates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//td/a")
for date in allDates:
    if date.text == dobDay:
        date.click()
        break
driver.find_element(By.ID, "sex_2").click()
time.sleep(1)
"""
#NOTE: cannot get additional passenger to work.  failed on drop down select.  
#driver.find_element(By.XPATH, "//input[@id='addmorepax']").click()
driver.find_element(By.CLASS_NAME, "woocommerce-input-wrapper").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "selection").click()
additionaPassengersDropdown = Select(driver.find_element(By.ID,"select2-addpaxno-result-y1tj-3"))
datepickerMonth.select_by_visible_text("add 1 more passenger (100%)")
driver.find_element(By.ID, "travname2").send_keys("secondfirstname")
driver.find_element(By.ID, "travlastname2").send_keys("secondlastname")
driver.find_element(By.ID, "travlastname2").send_keys("secondlastname")
driver.find_element(By.ID, "dob2").send_keys("secondlastname")
secondDobMonth = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
secondDobYear = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
secondDobMonth.select_by_visible_text("Mar")
secondDobYear.select_by_visible_text("2000")
secondDobDates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//td/a")
for date in secondDobDates:
    if date.text == "13":
        date.click()
        break
driver.find_element(By.ID, "sex2_1").click()
"""

time.sleep(5)
print("done")