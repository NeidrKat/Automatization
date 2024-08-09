from selenium.webdriver.common.by import By


class PurPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/')
        self.driver.implicitly_wait(5)

    # авторизация
    def autorization(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    # добавление в корзину товара
    def add(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    # переход в корзину и оформление покупки
    def shopping_cart_and_checkout(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        self.driver.find_element(By.ID, "checkout").click()

    # заполнение формы оплаты
    def form_of_payment(self):
        self.driver.find_element(By.ID, "first-name").send_keys('Dead')
        self.driver.find_element(By.ID, "last-name").send_keys('Pool')
        self.driver.find_element(By.ID, "postal-code").send_keys('456654')
        self.driver.find_element(By.ID, "continue").click()

    # окончательная цена покупик
    def total_price(self):
        self.driver.find_element(
            By.CLASS_NAME, "summary_total_label").get_attribute("textContent")
