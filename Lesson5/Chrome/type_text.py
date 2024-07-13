from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()

driver.get('http://the-internet.herokuapp.com/inputs')

number = driver.find_element(
    By.XPATH, '//*[@id="content"]/div/div/div/input')
sleep(5)
number.send_keys("1000")
sleep(5)
number = driver.find_element(
    By.XPATH, '//*[@id="content"]/div/div/div/input')
sleep(2)
number.clear()
sleep(5)
driver.quit()
