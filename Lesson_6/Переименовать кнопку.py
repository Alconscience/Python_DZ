from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
service = ChromeService(ChromeDriverManager().install())

# поиск элемента в течении 4 секунд

driver.implicitly_wait(4)

# заходим на сайт

driver.get("http://uitestingplayground.com/textinput")

# найти поле ввода "newButtonName" и ввести "SkyPro"

textinput = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
textinput.send_keys("SkyPro")

# нажать на кнопку "Button That Should Change it's Name Based on Input Value"

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

# собираем текст из новой кнопки

text_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

# выводим полученный текст и закрываем драйвер

print(text_button)
driver.quit()