from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# заходим на сайт

driver.get("http://the-internet.herokuapp.com/login")

# ввести в поле "username" значение "tomsmith"

textinput = driver.find_element(By.CSS_SELECTOR, "input#username")
textinput.send_keys("tomsmith")

# ввести в поле "password" значение "SuperSecretPassword!"

textinput = driver.find_element(By.CSS_SELECTOR, "input#password")
textinput.send_keys("SuperSecretPassword!")

# нажатие на кнопку "Login"

driver.find_element(By.CSS_SELECTOR, "i.fa.fa-2x.fa-sign-in").click()