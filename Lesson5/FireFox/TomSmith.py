from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Firefox()

driver.get('http://the-internet.herokuapp.com/login')

name = driver.find_element(
    By.XPATH, '//*[@id="username"]')
sleep(1)
name.send_keys("tomsmith")
sleep(2)
password = driver.find_element(
    By.XPATH, '//*[@id="password"]')
sleep(1)
password.send_keys('SuperSecretPassword!')
button = driver.find_element(
    By.XPATH, '//*[@id="login"]/button')
button.click()
sleep(2)
driver.quit()
