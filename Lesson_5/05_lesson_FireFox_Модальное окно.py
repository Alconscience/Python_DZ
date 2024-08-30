from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# заходим на сайт

driver.get("http://the-internet.herokuapp.com/entry_ad")

# подождать пока модальное окно и кнопка станут активными

sleep(5)

# нажать на кнопку "Close"

driver.find_element(By.XPATH, ("//p[text()='Close']")).click()