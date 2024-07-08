from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get('http://uitestingplayground.com/classattr')
for a in range(3):
    button_blue = driver.find_element(
        'xpath', "//button[contains(concat(' ', normalize-space(@class), ' '),\
            ' btn-primary ')]")
    button_blue.click()
    sleep(5)
    alert_obj = driver.switch_to.alert
    alert_obj.accept()
    sleep(5)
driver.quit()
