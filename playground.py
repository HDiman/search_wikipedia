from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "/Users/dsannikov/Documents/GitHub/ParsingPages/driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "http://secure-retreat-92358.herokuapp.com/"
driver.get(url=url)

search = driver.find_element(By.NAME, "fName")
search.send_keys("Dmitry")
time.sleep(3)

search = driver.find_element(By.NAME, "lName")
search.send_keys("Sannikov")
time.sleep(3)

search = driver.find_element(By.NAME, "email")
search.send_keys("dsannikov@gmail.com")
time.sleep(3)

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
time.sleep(3)

driver.close()
driver.quit()

