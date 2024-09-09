from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
service = ChromeService(ChromeDriverManager().install())

# поиск элемента в течении 10 секунд

driver.implicitly_wait(10)

# заходим на сайт

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# ищем элемент с id="award"

id_award = driver.find_element(By.CSS_SELECTOR, "#award")

# собираем текст из элемента src через элемент id_award

text_src = id_award.get_attribute("src")

# выводим полученный текст и закрываем драйвер

print(text_src)
driver.quit()