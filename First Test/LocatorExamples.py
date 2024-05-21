from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

driver.find_element(By.ID, "passwordID")

driver.find_element(By.CLASS_NAME, "userClass")

driver.find_element(By.NAME, "passwordName")

driver.find_element(By.LINK_TEXT, "Enter Password")

driver.find_element(By.PARTIAL_LINK_TEXT, "Enter Pa")

#CSS
#tag & id
driver.find_element(By.CSS_SELECTOR, "input#email")
driver.find_element(By.CSS_SELECTOR, "#email")

#tag and class
driver.find_element(By.CSS_SELECTOR, "input.class_name")

#tag and attribute

#tag, class, and attribute
driver.find_element(By.CSS_SELECTOR, "input.class_name[data-test=email_thing")

#xpath options
# and : can find element with both attributes.  e.g. //input[@name='user' and @placeholder='organize']
# or : can be used to choose between attributes.  e.g. //input[@name='user' or @placeholder='organize']
# contains() : attribute contains a specified value, can be anywhere in attribute, even middle.  e.g. //*[contains(@id,ort)]
# starts-with() : attribute starts with a specified value.  e.g. //*[starts-with(@id,st)]
# text() : attribute has specified text.  e.g. //a[text()='hello, is it me you're looking for?']

#xpath axes - examples based on:  https://money.rediff.com/gainers/bse/dail/groupa
# self : the central node.  different axes types are based on their association to the self node.  e.g. //*[attribute='value']/self::tagname
# EXAMPLE: driver.find_element(By.XPATH, "//a[contains(text(),'some text')]/self::a")

# parent : the node prior to the self node.  e.g. //*[attribute='value']/parent::tagname
# EXAMPLE: driver.find_element(By.XPATH, "//a[contains(text(),'some text')]/parent::td")

# child : the  node after the self node.  e.g. //*[attribute='value']/child::tagname
# EXAMPLE: driver.find_element(By.XPATH, "//a[contains(text(),'some text')]/ancestor::tr/child::td") -> in this example
# we needed to navigate to the ancestor element as the self element did not have a child element.

# ancestor : the node before the parent element of the self node.  e.g. //*[attribute='value']/ancestor::tagname
# EXAMPLE: driver.find_element(By.XPATH, "//a[contains(text(),'some text')]/ancestor::tr")

# descendant : the node after the child element of the self node.  e.g. //*[attribute='value']/descendant::tagname
# EXAMPLE: driver.find_element(By.XPATH, "//a[contains(text(), 'some text')]/ancestor::tr/descendant::*"

# following : parallel siblings of a parent node that are after the parent node.  on the same 'level' on the DOM. e.g. //*[attribute='value']/following::tagname
# EXAMPLE: driver.find_element(By.XPATH, "//a[contains(text(), 'some text')]/ancestor::tr/following::*"

# following-sibling : parallel siblings that are after the self node.  e.g. //current html tag[@attribute='value']/following-sibling::sibling tag[@attribute='value']
# EXAMPLE: driver.find_element(By.XPATH, "//a[contains(text(), 'some text')]/ancestor::tr/following-sibling::*"

# preceding : parallel siblings of a parent node that are before the parent node.  e.g. //*[attribute='value']/preceding::tagname
# EXAMPLE: driver.find_element(By.XPATH, "//a[contains(text(), 'some text')]/ancestor::tr/preceding::*"

# preceding-sibling : parallel siblings that are before  the self node.  e.g. //current html tag[@attribute='value']/preceding-sibling::sibling tag[@attribute='value']
# EXAMPLE: driver.find_element(By.XPATH, "//a[contains(text(), 'some text')]/ancestor::tr/preceding-sibling::*"

#end of notes