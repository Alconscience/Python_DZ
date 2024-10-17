from selenium.webdriver.common.by import By
import allure

class ResultPageForm:
    
    def __init__(self, driver):
        self._driver = driver
    

    @allure.step("Нажатие на кнопку Submit")
    def click(self):
        """
        Функция нажатия на кнопку Submit
        """
        self._driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3").click()
