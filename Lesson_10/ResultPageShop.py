from selenium.webdriver.common.by import By
import allure

class ResultPageShop:

    def __init__(self, driver):
        self._driver = driver
    
    @allure.step("нажатие на кнопку Checkout")
    def send_check(self):
        """
        Функция нажатия на кнопку Checkout
        """
        self._driver.find_element(By.ID, "checkout").click()

    @allure.step("Ввод данных пользователя: First Name - {f_n}")
    def first_name(self, f_n):
        """
        Функция ввода First Name
        """
        firstname = self._driver.find_element(By.ID, "first-name").send_keys(f_n)

    @allure.step("Ввод данных пользователя: Last Name - {l_n}")
    def last_name(self, l_n):
        """
        Функция ввода Last Name
        """
        lastname = self._driver.find_element(By.ID, "last-name").send_keys(l_n)

    @allure.step("Ввод данных пользователя: Postal code - {p_c}")
    def postcode(self, p_c):
        """
        Функция ввода Postal code
        """
        postalcode = self._driver.find_element(By.ID, "postal-code").send_keys(p_c)

    @allure.step("нажатие на кнопку Continue")
    def send_cont(self):
        """
        Функция нажатия на кнопку Continue
        """
        self._driver.find_element(By.ID, "continue").click()

    @allure.step("Читаем со страницы итоговую стоимость:")
    def total(self):
        """
        Функция читает со страницы итоговую сумму
        """
        total_out = self._driver.find_element(By.XPATH, '//div[text()="58.29"]').text
        with allure.step("Итоговая сумма заказа = {}".format(total_out)):
            return total_out
