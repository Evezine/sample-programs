from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify the path to the chromedriver executable (no quotes needed)
service = Service('D:/python programs/automation_driver/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# try:
    # Open Google India
driver.get('https://www.google.co.in/')
    
    # Wait until the search box is present and type the query
    # wait = WebDriverWait(driver, 20)
    # search = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="q"]')))
    # search.send_keys('python online compiler')
    # search.send_keys(Keys.ENTER)
    
    # # Wait until the first result is clickable and click it
    # first_result = wait.until(EC.element_to_be_clickable((By.XPATH, '(//h3)[1]/../../a')))
    # first_result.click()
    
    # # Wait for the button to be clickable and then click it
    # button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="some-button-id"]')))  # Replace with the actual XPath
    # button.click()
    
    # Sleep to allow time to observe the result (adjust as necessary)
time.sleep(10000)
    
# finally:
#     # Quit the driver
#     driver.quit()
