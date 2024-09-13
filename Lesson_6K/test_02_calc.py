from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
service = ChromeService(ChromeDriverManager().install())

# заходим на сайт

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

# в поле ввода по локатору "#delay" вводим значение 45

Delay = driver.find_element(By.CSS_SELECTOR, "#delay")
Delay.clear()
Delay.send_keys("45")

# нажимаем кнопки

# нажимаем 7
driver.find_element(By.XPATH, "//span[text()='7']").click()

# нажимаем +
driver.find_element(By.XPATH, "//span[text()='+']").click()

# нажимаем 8
driver.find_element(By.XPATH, "//span[text()='8']").click()

# нажимаем =
driver.find_element(By.XPATH, "//span[text()='=']").click()

# ожидание результата 45 сек.
Result = WebDriverWait(driver, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
ResultText = driver.find_element(By.CLASS_NAME, "screen").text
assert ResultText == "15", "OK"

driver.quit()