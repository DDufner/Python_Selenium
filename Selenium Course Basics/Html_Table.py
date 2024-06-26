from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/chromedriver')

chrome_options = Options()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

ops = webdriver.ChromeOptions()
ops.add_argument("-diable-notifications")

driver.get("https://testautomationpractice.blogspot.com/")

numberOfRows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))

numberOfColumns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/th"))

print("number of rows: ", numberOfRows, "number of columns: ", numberOfColumns, "number of cells: ", numberOfColumns * numberOfRows)

valueFor2x2 = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[2]/td[2]").text

print(valueFor2x2)

for row in range(2,numberOfRows+1):
    for column in range(1, numberOfColumns+1):
        cellData = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(row)+"]/td["+str(column)+"]").text
        print(cellData, end='   ')
    print()

targetAuthor = "Mukesh"
numberOfBooks = 0
print("search by author name:")
for item in range(2,numberOfRows+1):
    authors = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/td[2]")
    authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(item)+"]/td[2]").text
    bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(item)+"]/td[1]").text
    if authorName == targetAuthor:
        numberOfBooks +=1
        print(bookName)
    else:
        print("...x...")
print("number of books by "+targetAuthor+": ", numberOfBooks)

