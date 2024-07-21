from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()


def test_form():
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(
        'Иван')
    driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(
        'Петров')
    driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys(
        'Ленина, 55-3')
    driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(
        'test@skypro.com')
    driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys(
        '+7985899998787')
    driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys(
        'Москва')
    driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys(
        'Россия')
    driver.find_element(
        By.CSS_SELECTOR, 'input[name="job-position"]').send_keys('QA')
    driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys(
        'SkyPro')
    sleep(5)
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    sleep(10)
    zip_cod_failed = driver.find_element(
        By.ID, 'zip-code')
    assert "alert-danger" in zip_cod_failed.get_attribute("class")
    driver.quit()
