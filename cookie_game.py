from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import threading

def check_items():
    threading.Timer(5.0).start()


chrome_driver_path = "/Users/dsannikov/Documents/GitHub/ParsingPages/driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url=url)


game_on = True
while game_on:
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()

