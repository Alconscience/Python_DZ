from selenium.webdriver.common.by import By

class MainPageCalc:

# заходим на сайт
   def __init__(self, driver):
    self._driver = driver
    self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    self._driver.maximize_window()

# в поле ввода по локатору "#delay" вводим значение 45
   def delay(self, d_y):
     delay = self._driver.find_element(By.CSS_SELECTOR, "#delay")
     delay.clear()
     delay.send_keys(d_y)

# нажимаем кнопки
   def send_key(self):
     self._driver.find_element(By.XPATH, "//span[text()='7']").click() # нажимаем 7
     self._driver.find_element(By.XPATH, "//span[text()='+']").click() # нажимаем +
     self._driver.find_element(By.XPATH, "//span[text()='8']").click() # нажимаем 8
     self._driver.find_element(By.XPATH, "//span[text()='=']").click() # нажимаем =
