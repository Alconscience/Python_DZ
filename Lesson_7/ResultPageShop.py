from selenium.webdriver.common.by import By

class ResultPageShop:

    def __init__(self, driver):
        self._driver = driver
    
# нажатие на кнопку "Checkout"
    def send_check(self):
        self._driver.find_element(By.ID, "checkout").click()

# ввод данных пользователя

# First Name
    def first_name(self, f_n):
        firstname = self._driver.find_element(By.ID, "first-name").send_keys(f_n)
# Last Name        
    def last_name(self, l_n):
        lastname = self._driver.find_element(By.ID, "last-name").send_keys(l_n)
# Postal code
    def postcode(self, p_c):
        postalcode = self._driver.find_element(By.ID, "postal-code").send_keys(p_c)

# нажатие на кнопку "Continue"
    def send_cont(self):
        self._driver.find_element(By.ID, "continue").click()

# читаем со страницы итоговую стоимость
    def total(self):
        total_out = self._driver.find_element(By.XPATH, '//div[text()="58.29"]').text
        return total_out
