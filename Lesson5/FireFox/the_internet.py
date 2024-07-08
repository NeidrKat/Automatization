from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
F_driver = webdriver.Firefox()

F_driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
sleep(5)
for a in range(5):
    add_button = F_driver.find_element(
        By.XPATH, '//*[@id="content"]/div/button').click()
    delete_button_Firefox = F_driver.find_elements(
        By.XPATH, '//*[@id="elements"]/button')
sleep(2)
print(f'размер списка "Delete-кнопок":{len(delete_button_Firefox)}')
F_driver.quit
