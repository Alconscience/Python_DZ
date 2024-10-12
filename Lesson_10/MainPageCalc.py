from selenium.webdriver.common.by import By
import allure

@allure.step("Заходим на сайт: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

class MainPageCalc:

   def __init__(self, driver):
    """
    Функция захода на сайт
    """
    self._driver = driver
    self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    self._driver.maximize_window()

   @allure.step("Установить таймер - {d_y}")
   def delay(self, d_y: int):
      """
      Функция устанавливает значение таймера в секундах
      """
      delay = self._driver.find_element(By.CSS_SELECTOR, "#delay")
      delay.clear()
      delay.send_keys(d_y)

   @allure.step("Последовательное нажатие на кнопки: 7, +, 8, =")
   def send_key(self):
      """
      Функция последовательно нажимает на кнопки: 7, +, 8, =
      """
      with allure.step("Нажатие на кнопку 7"):
         self._driver.find_element(By.XPATH, "//span[text()='7']").click()
      
      with allure.step("Нажатие на кнопку +"):
         self._driver.find_element(By.XPATH, "//span[text()='+']").click()
      
      with allure.step("Нажатие на кнопку 8"):
         self._driver.find_element(By.XPATH, "//span[text()='8']").click()
      
      with allure.step("Нажатие на кнопку ="):
         self._driver.find_element(By.XPATH, "//span[text()='=']").click()
