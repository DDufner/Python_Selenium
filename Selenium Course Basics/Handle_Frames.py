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

#fatalFrame = driver.find_element(By.XPATH, "iframe/id='frame-one796456169'")

driver.switch_to.frame("frame-one796456169")
driver.find_element(By.XPATH, "//*[@id='RESULT_TextField-0']").send_keys("Frame Name")
driver.find_element(By.XPATH, "//*[@id='RESULT_TextField-2']").send_keys("01012002")
driver.switch_to.default_content()
driver.find_element(By.XPATH, "//*[@id='name']").send_keys("Tobert")

#to switch between multiple frames, user needs to go to frame, switch back to main page
#using 'driver.switch_to.default_content()' then switch to next frame 

time.sleep(3)

#nested frames

driver.get("https://demo.automationtesting.in/Frames.html")

driver.find_element(By.XPATH, "//a[contains(text(),'Iframe with in an Iframe')]").click()

outerFrame = driver.find_element(By.XPATH,("//iframe[@src='MultipleFrames.html']"))
driver.switch_to.frame(outerFrame)
innerFrame = driver.find_element(By.CSS_SELECTOR,".iframe-container > iframe:nth-child(2)")
driver.switch_to.frame(innerFrame)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("yo dawg, we heard you liked frames, so we put a frame in your frame so you can frame frames when you frame")

time.sleep(3)

print("test complete")