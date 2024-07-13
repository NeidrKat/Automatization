from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 40)
driver.get(
    'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p[id=text]"), "Done!")
    )
print(driver.find_element(
    By.CSS_SELECTOR, "img[id=award]").get_attribute("src"))
