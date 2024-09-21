from selenium.webdriver.common.by import By

class MainPageShop:

# заходим на сайт
   def __init__(self, driver):
    self._driver = driver
    self._driver.get("https://www.saucedemo.com/")
    self._driver.maximize_window()

# вводим Username и Password
   def authorization(self, log, pas):
    login = self._driver.find_element(By.CSS_SELECTOR, "input#user-name").send_keys(log)
    password = self._driver.find_element(By.CSS_SELECTOR, "input#password").send_keys(pas)

# нажатие на кнопку "Login"
   def send_batton(self):
    self._driver.find_element(By.ID, "login-button").click()

# добавление товаров в корзину

   def send_tovar(self):
    # добавление товара Sauce Labs Backpack
    self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    # добавление товара Sauce Labs Bolt T-Shirt
    self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    # добавление товара Sauce Labs Onesie
    self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()


# переход в корзину
   def check_cart(self):
    self._driver.find_element(By.ID, "shopping_cart_container").click()
