from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://uitestingplayground.com/textinput')

rename = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
rename.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()

print(driver.find_element(By.CSS_SELECTOR, '#updatingButton').text)
