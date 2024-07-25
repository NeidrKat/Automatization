from selenium import webdriver
from Calculator.CalculatorPage import CalculatorPage


def test_form_calculator():
    driver = webdriver.Chrome()
    calculator_page = CalculatorPage(driver)

    calculator_page.delay()
    calculator_page.sum_of_the_numbers()
    calculator_page.get_result()
    calculator_page.close_driver()
