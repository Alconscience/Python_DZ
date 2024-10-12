from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class ResultPageCalc:
    
    def __init__(self, driver):
        self._driver = driver

    @allure.step("Ожидание результата вычислений и возврат суммы вычислений")
    def result_out(self):
        """
        Функция ожидает результата.
        """
        result = WebDriverWait(self._driver, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        resultText = self._driver.find_element(By.CLASS_NAME, "screen").text
        with allure.step("Сумма вычислений = {}".format(resultText)):
            return resultText
