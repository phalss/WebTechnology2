from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('./chromedriver_win32/chromedriver')
driver.get(" http://127.0.0.1:8000/")
driver.implicitly_wait(10)
print(driver.title)
time.sleep(2)
elem = driver.find_element_by_partial_link_text("NEWS") #Clicks the News and Analytics hyperlink and verifies if it redirects to the correct page
elem.click()
expected_url = "http://127.0.0.1:8000/news/"
# time.sleep(2)
if(driver.current_url == expected_url):
		print("TESTCASE 1 PASSED\n")
else:
		print("TESTCASE 1 FAILED\n")

# time.sleep(2)
elem = driver.find_element_by_partial_link_text("Look") #Clicks the Look-up Prices hyperlink and verifies if it redirects to the correct page
elem.click()
# time.sleep(2)
expected_url = "http://127.0.0.1:8000/news/prices/"
if(driver.current_url == expected_url):
		print("TESTCASE 2 PASSED\n")
else:
		print("TESTCASE 2 FAILED\n")
# time.sleep(5)
inputElement = driver.find_element_by_name("quote") #3 Checks if correct data corresponding to  shown if btc is entered in search bar
inputElement.send_keys("btc") #3
# time.sleep(5)
inputElement.submit()
time.sleep(2)
expected_content="BTC"
obtained_content = driver.find_element_by_css_selector("h1.display-4").text
if(obtained_content == expected_content):
	print("TESTCASE 3 PASSED\n")
else:
    print(obtained_content)
    print("TESTCASE 3 FAILED\n")
# time.sleep(5)
# time.sleep(5)
inputElement = driver.find_element_by_name("quote") #4  Checks if correct data corresponding to  eth is entered in search bar
inputElement.send_keys("eth") #4
# time.sleep(5)
inputElement.submit()
expected_content="ETH"
obtained_content = driver.find_element_by_css_selector("h1.display-4").text
if(obtained_content == expected_content):
	print("TESTCASE 4 PASSED\n")
else:
    print(obtained_content)
    print("TESTCASE 4 FAILED\n")
# time.sleep(5)
inputElement = driver.find_element_by_name("quote") #5 Checks if correct response is sent corresponding to incorrect entry
inputElement.send_keys("ANCDJ") #5
# time.sleep(5)
inputElement.submit()
expected_content="Sorry, ANCDJ doesn't exist. Please Try Again..."
obtained_content = driver.find_element_by_css_selector("div.container").text
if(obtained_content == expected_content):
	print("TESTCASE 5 PASSED\n")
else:
    print(obtained_content)
    print("TESTCASE 5 FAILED\n")
# time.sleep(5)
elem = driver.find_element_by_partial_link_text("Crypto") #6 CHECKS if it goes to the main news site
elem.click()

expected_url = "http://127.0.0.1:8000/news/"
if(driver.current_url == expected_url):
		print("TESTCASE 6 PASSED\n")
else:
		print("TESTCASE 6 FAILED\n")
# time.sleep(10)
elem = driver.find_element_by_partial_link_text("Data") #7 CHECKS if it goes to the prediction chart page
elem.click()
expected_url = "http://127.0.0.1:8000/news/chart/" 
if(driver.current_url == expected_url):
		print("TESTCASE 7 PASSED\n")
else:
		print("TESTCASE 7 FAILED\n")
# time.sleep(20)
driver.execute_script("window.history.go(-1)") #8  Check if the back button works and hence gets redirected to the home news page
expected_url = "http://127.0.0.1:8000/news/"
if(driver.current_url == expected_url):
		print("TESTCASE 8 PASSED\n")
else:
		print("TESTCASE 8 FAILED\n")
# 
# time.sleep(5)
elem = driver.find_element_by_partial_link_text("Read More...") #9 Checks if the first link in the News cards is clicked and it tis redirected to the news website
elem.click()
not_expected_url = "http://127.0.0.1:8000/news/"
if(driver.current_url == not_expected_url):
		print("TESTCASE 9 FAILED\n")
else:
		print("TESTCASE 9 PASSED \n")
# time.sleep(5)

driver.execute_script("window.history.go(-1)") 
time.sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #10 scrolling down to bottom of page .
expected_url = "http://127.0.0.1:8000/news/"
if(driver.current_url == expected_url):
		print("TESTCASE 10 PASSED\n")
else:
		print("TESTCASE 10 FAILED\n")


time.sleep(5)  #10
driver.close()