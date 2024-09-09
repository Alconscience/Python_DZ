from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
service = ChromeService(ChromeDriverManager().install())

# поиск элемента в течении 20 секунд

driver.implicitly_wait(20)

# заходим на сайт

driver.get("http://uitestingplayground.com/ajax")

# нажать на кнопку "Button Triggering AJAX Request"

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# ищем элемент с id="content"

id_content = driver.find_element(By.CSS_SELECTOR, "#content")

# собираем текст из элемента с тегом p class="bg-success" через элеменет в id_content

text_content = id_content.find_element(By.CSS_SELECTOR, "p.bg-success").text

# выводим полученный текст и закрываем драйвер

print(text_content)
driver.quit()