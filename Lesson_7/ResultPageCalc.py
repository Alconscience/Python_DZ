from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultPageCalc:
    
    def __init__(self, driver):
        self._driver = driver

# ожидание результата 45 сек.
    def result_out(self):
        result = WebDriverWait(self._driver, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        resultText = self._driver.find_element(By.CLASS_NAME, "screen").text
        return resultText
