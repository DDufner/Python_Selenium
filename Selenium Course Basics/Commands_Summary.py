from datetime import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/")

# Application commands
# get : gets URL listed in function.
# title : prints title of webpage, per what is in header.
# current_url : prints current URL of webpage.
# page_source : prints source data for page.

# Conditional commands
# is_displayed() : checks if element is present on webpage. returns true if present, if not, returns false.
# is_enabled() : checks if element can be interacted with e.g. enter text into text field, click button.
#    returns true or false.
# is_selected() : checks if element is selected e.g. checkbox, radio button, link etc.  returns true or false.

# Browser commands
# close :  closes browser but does not shut down webdriver. will only close one browser tab (current/focused).
# quit : closes browser and shuts down webdriver.  will close all browser tabs/windows.

# Navigational commands
# back() : uses browser back button.
# forward() : uses browser forward button.
# refresh() : uses browser refresh button.

# find_element() VS find_elements()
# find_element() finds single element.  can also be used to select multiple web elements if the identifier is generic
#     to return multiple.  will throw 'NoSuchElementException' if element is not found.
# find_elements() creates list of elements, even if there is only a single element or no items at all.
#     will not return error if no elements found.  need to assign to variable to create list variable that can be
#     printed, iterated through.


