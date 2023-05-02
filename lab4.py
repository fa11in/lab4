from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.implicitly_wait(10)

login = driver.find_element(By.ID, 'email')
login.send_keys("zhairbaev@gmail.com")
driver.implicitly_wait(10)

password = driver.find_element(By.ID, 'pass')
password.send_keys("1y3b9af3")
password.submit()
# driver.implicitly_wait(10)
time.sleep(10)
