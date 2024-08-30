from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# заходим на сайт

driver.get("http://the-internet.herokuapp.com/inputs")

# ввести в поле текст "1000"

textinput = driver.find_element(By.CSS_SELECTOR, "input")
textinput.send_keys("1000")
sleep(2)

# очистить поле

driver.find_element(By.CSS_SELECTOR, "input").clear()
sleep(2)

# ввести в поле текст "999"

textinput = driver.find_element(By.CSS_SELECTOR, "input")
textinput.send_keys("999")