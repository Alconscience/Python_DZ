from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
service = ChromeService(ChromeDriverManager().install())

# заходим на сайт

driver.get("https://www.saucedemo.com/")

# вводим Username и Password

Login = driver.find_element(By.CSS_SELECTOR, "input#user-name")
Login.send_keys("standard_user")

Password = driver.find_element(By.CSS_SELECTOR, "input#password")
Password.send_keys("secret_sauce")

# нажатие на кнопку "Login"

driver.find_element(By.ID, "login-button").click()

# добавление товаров в корзину

# добавление товара Sauce Labs Backpack
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# добавление товара Sauce Labs Bolt T-Shirt
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

# добавление товара Sauce Labs Onesie
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

# переход в корзину
driver.find_element(By.ID, "shopping_cart_container").click()

# нажатие на кнопку "Checkout"
driver.find_element(By.ID, "checkout").click()

# ввод данных пользователя

# First Name
FirstName = driver.find_element(By.ID, "first-name")
FirstName.send_keys("Alexandr")

# Last Name
LastName = driver.find_element(By.ID, "last-name")
LastName.send_keys("Sviridov")

# Postal code
PostalCode = driver.find_element(By.ID, "postal-code")
PostalCode.send_keys("123456")

# нажатие на кнопку "Continue"
driver.find_element(By.ID, "continue").click()

# читаем со страницы итоговую стоимость, закрываем браузер и проверяем итоговую сумму
Total = driver.find_element(By.XPATH, '//div[text()="58.29"]').text

driver.quit()

assert Total == "Total: $58.29", "OK"
