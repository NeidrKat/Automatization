from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()

driver.get(' http://the-internet.herokuapp.com/entry_ad')
wait = WebDriverWait(driver, 10)
modal_window = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
sleep(2)
clouse_window = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer")))
clouse_window.click()
sleep(5)
driver.quit()
