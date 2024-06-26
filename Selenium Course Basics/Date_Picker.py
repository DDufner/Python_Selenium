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

driver.get("https://jqueryui.com/datepicker/")

driver.switch_to.frame(0)
#driver.find_element(By.ID, "datepicker").send_keys("01/07/1964") 
driver.find_element(By.ID, "datepicker").click()

targetDay = "25"
targetMonth = "January"
targetMonth3Char = "Jan"
targetYear = "2020"

#while targetMonth != currentCalendarMonth:

# while True:
#     currentCalendarMonth = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
#     currentCalendarYear = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
#     if currentCalendarMonth == targetMonth and currentCalendarYear == targetYear:
#         driver.find_element(By.XPATH, "//a[@data-date='"+targetDay+"']").click()
#         break;
#     else:
#         driver.find_element(By.CLASS_NAME, "ui-icon.ui-icon-circle-triangle-w").click()
        
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_element(By.ID, "dob").click()
datepickerMonth = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
datepickerMonth.select_by_visible_text(targetMonth3Char)
#NOTE: method below did not work for selecting 'Jan' from list.
#driver.find_element(By.CLASS_NAME, "ui-datepicker-month").click()
#driver.find_element(By.XPATH, "//option[contains(text(),'"+targetMonth3Char+"')]").click()
driver.find_element(By.CLASS_NAME, "ui-datepicker-year").click()
driver.find_element(By.XPATH, "//option[contains(text(),'"+targetYear+"')]").click()
#driver.find_element(By.XPATH, "//a[@data-date='"+targetDay+"']").click()
#alternate date pick method: 
allDates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//td/a")
for date in allDates:
    if date.text == targetDay:
        date.click()
        break


selectedDate = driver.find_element(By.ID, "dob").get_attribute("value")
print(selectedDate)
time.sleep(5)
print("Test done.")