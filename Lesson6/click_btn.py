from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = driver.implicitly_wait(17)
driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()
result = driver.find_element(By.CSS_SELECTOR, '#content')
text = result.find_element(By.CSS_SELECTOR, "p.bg-success").text
print("Результат:", text)
driver.quit()
