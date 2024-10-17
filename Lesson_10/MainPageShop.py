from selenium.webdriver.common.by import By
import allure

@allure.step("Заходим на сайт: https://www.saucedemo.com/")

class MainPageShop:

# заходим на сайт
   def __init__(self, driver):
    """
    Функция захода на сайт
    """
    self._driver = driver
    self._driver.get("https://www.saucedemo.com/")
    self._driver.maximize_window()

   @allure.step("Вводим данные для авторизации :")
   def authorization(self, log, pas):
     """
     Функция ввода Login и Password
     """
     with allure.step("Вводим Login - {}".format(log)):
      login = self._driver.find_element(By.CSS_SELECTOR, "input#user-name").send_keys(log)
     with allure.step("Вводим Password - {}".format(pas)):
      password = self._driver.find_element(By.CSS_SELECTOR, "input#password").send_keys(pas)

   @allure.step("Нажатие на кнопку Login")
   def send_batton(self):
     """
     Функция нажатия на кнопку Login
     """
     self._driver.find_element(By.ID, "login-button").click()

   @allure.step("Добавление товаров в корзину")
   def send_tovar(self):
     """
     Функция добавления товаров в корзину
     """
     with allure.step("Добавление товара Sauce Labs Backpack"):
      self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
   
     with allure.step("Добавление товара Sauce Labs Bolt T-Shirt"):
      self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    
     with allure.step("Добавление товара Sauce Labs Onesie"):
      self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()


   @allure.step("Нажатие на кнопку Корзина")
   def check_cart(self):
     """
     Функция перехода в корзину
     """
     self._driver.find_element(By.ID, "shopping_cart_container").click()
