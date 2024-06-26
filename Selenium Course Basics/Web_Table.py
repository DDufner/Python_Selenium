import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By

service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/chromedriver')
chrome_options = Options()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

driver.get("https://opensource-demo.orangehrmlive.com")
driver.implicitly_wait(5)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.find_element(By.XPATH, "//span[text()='Admin']").click()

rowsLength = len(driver.find_elements(By.XPATH,"//div[@class='oxd-table-card']")) 

#enabled count loop
enabledCount = 0
for row in range(1, rowsLength+1):
    status = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div["+str(row)+"]/div/div[5]").text
    if status == "Enabled":
        enabledCount = enabledCount +1
print("total number of enabled employees: ", enabledCount)
print("total number of disabled employees: ", rowsLength - enabledCount)
#non-ESS works
for row in range(1, rowsLength+1):
    role = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div["+str(row)+"]/div/div[3]").text
    if role != "ESS":
        userName = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div["+str(row)+"]/div/div[2]").text
        roleName = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div["+str(row)+"]/div/div[3]").text
        employeeName = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div["+str(row)+"]/div/div[4]").text
        print("Employee Name: ", employeeName, "\nUser Name: ", userName, "\nRole: ",roleName)

#assignment
#print user name and role if role is NOT ESS

print("done")