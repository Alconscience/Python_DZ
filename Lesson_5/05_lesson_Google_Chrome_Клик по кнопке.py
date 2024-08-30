from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
service = ChromeService(ChromeDriverManager().install())

# заходим на сайт

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# нажатие на кнопку "Add Element" 5 раз

for i in range(5):
    addButton = driver.find_element(By.CSS_SELECTOR, "button").click()

# поиск всех кнопок DELETE

searchDeleteButton = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")

# подсчет и вывод количества кнопок DELETE

print(len(searchDeleteButton))

sleep(10) 