from selenium.webdriver.common.by import By

class ResultPageForm:
    
    def __init__(self, driver):
        self._driver = driver
    
# нажатие на кнопку "Submit"
    def click(self):
        self._driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3").click()
