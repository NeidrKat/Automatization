from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()


def test_purchase():
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    sleep(2)
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    sleep(5)
    driver.find_element(By.ID, "shopping_cart_container").click()
    sleep(5)
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys('Dead')
    driver.find_element(By.ID, "last-name").send_keys('Pool')
    driver.find_element(By.ID, "postal-code").send_keys('456654')
    sleep(5)
    driver.find_element(By.ID, "continue").click()
    sleep(5)
    price = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_price = price.text.strip().replace("Total: $", "")

    expected_total_price = '58.29'
    assert total_price == expected_total_price
