from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions
# same as above but using EC for alies: from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

time.sleep(2)
# will always wait for full time set even if element is available.
# reduces performance.  if element is not available after time, change of getting exception.

driver.implicitly_wait(2)
# unless browser is closed, implicit_wait will be applied to all statements throughout rest of script.
# only waits for as long as it takes for element to appear instead of waiting full time.
# if element is not present after wait time, exception thrown.

myWait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,
                                                                         ElementNotInteractableException])
elementToFind = myWait.until(expected_conditions.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
# used WebDriverWait class object.   waits until condition is met for element listed.
# statement will return web element, which can ba assigned to a variable.
# time limit set is for how long it takes for statement to exit and continue if element is not found.
# can also add list of exceptions to ignore in WebDriverWait object.
# needs to be used for each element we want to apply it to, not once for the whole scrip til implicit wait.
# poll_frequency can add regular check intervals.

print("test me")