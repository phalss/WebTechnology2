from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('./chromedriver_win32/chromedriver')
driver.get(" http://127.0.0.1:8000/")
driver.implicitly_wait(10)
print(driver.title)
time.sleep(5)
elem = driver.find_element_by_partial_link_text("NEWS") #1
elem.click()
time.sleep(5)
elem = driver.find_element_by_partial_link_text("Look") #2
elem.click()
time.sleep(5)
inputElement = driver.find_element_by_name("quote") #3
inputElement.send_keys("btc") #3
time.sleep(5)
inputElement.submit()
time.sleep(5)
inputElement = driver.find_element_by_name("quote") #4
inputElement.send_keys("eth") #4
time.sleep(5)
inputElement.submit()
time.sleep(5)
inputElement = driver.find_element_by_name("quote") #5
inputElement.send_keys("ANCDJ") #5
time.sleep(5)
inputElement.submit()
time.sleep(5)
elem = driver.find_element_by_partial_link_text("Crypto") #6
elem.click()
time.sleep(10)
elem = driver.find_element_by_partial_link_text("Data") #7
elem.click()
time.sleep(20)
driver.execute_script("window.history.go(-1)") #8 
time.sleep(5)
elem = driver.find_element_by_partial_link_text("Read More...") #9
elem.click()
time.sleep(5)

driver.execute_script("window.history.go(-1)") 
time.sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #10 scrolling down to bottom of page .
time.sleep(5)  #10
driver.close()