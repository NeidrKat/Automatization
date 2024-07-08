from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

quantity = 0
driver.get("http://uitestingplayground.com/dynamicid")
for b in range(3):
    button = driver.find_element(
        By.XPATH, '//button[text() = "Button with Dynamic ID"]').click()
    quantity = quantity + 1
    sleep(5)
    print(quantity)
driver.quit()
