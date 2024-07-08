from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/chromedriver')

chrome_options = Options()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

action=ActionChains(driver)
#slider
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
min_slider = driver.find_element(By.XPATH,"//span[1]")
max_slider = driver.find_element(By.XPATH,"//span[2]")
print("min",min_slider.location)
print("max",max_slider.location)
action.drag_and_drop_by_offset(min_slider, 88, 251).perform()
action.drag_and_drop_by_offset(max_slider, -120, 251).perform()
time.sleep(5)

#scrolling
driver.get('https://en.wikipedia.org/wiki/The_Poppy_Family')
driver.execute_script("window.scrollBy(0,3000)","")
value=driver.execute_script("return window.pageYOffset;")
print("pixels moved: ", value)

#scroll to item
studio_albums = driver.find_element(By.ID, "Studio_albums")
driver.execute_script("arguments[0].scrollIntoView();",studio_albums)

#scroll to bottom
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
pixelValue = driver.execute_script("return window.pageYOffset;")
print("pixel vallue: ", pixelValue)

#mouse over action
driver.get("http://the-internet.herokuapp.com/hovers")
figure1=driver.find_element(By.XPATH, "(//div[@class='figure'])[1]")
figure2=driver.find_element(By.XPATH, "(//div[@class='figure'])[2]")
figure3=driver.find_element(By.XPATH, "(//div[@class='figure'])[3]")
action.move_to_element(figure1).perform()
time.sleep(1)
action.move_to_element(figure2).perform()
time.sleep(1)
action.move_to_element(figure3).perform()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "a[href='/users/3']").click()
time.sleep(2)

#right click action
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
time.sleep(2)
rightClickButton = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
action.context_click(rightClickButton).perform()
span = driver.find_element(By.CLASS_NAME, "hljs-tag")
action.double_click(span).perform()
time.sleep(2)

driver.get("https://www.w3schools.com/TAgs/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.switch_to.frame("iframeResult")
field1=driver.find_element(By.XPATH, "//input[@id='field1']")
field1.clear()
field1.send_keys("welcome")
button = driver.find_element(By.XPATH, "//button[@ondblclick='myFunction()']")
action.double_click(button).perform()
time.sleep(2)

#drag and drop -> will not automate if linked at end of other tests
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
time.sleep(2)
for item in range(1,8):
    source_item = driver.find_element(By.ID, "box"+str(item)+"")
    target_item = driver.find_element(By.ID, "box10"+str(item)+"")
    action.drag_and_drop(source_item,target_item).perform()
print("end of test")