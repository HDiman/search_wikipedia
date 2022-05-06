from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "/Users/dsannikov/Documents/GitHub/ParsingPages/driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url=url)

number_of_articles = driver.find_element(By.XPATH, "//*[@id='articlecount']/a[1]")
# number_of_articles.click()

nominate_article = driver.find_element(By.LINK_TEXT, "Nominate an article")
# nominate_article.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
 


time.sleep(10)

driver.close()
driver.quit()
