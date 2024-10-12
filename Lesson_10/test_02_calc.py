from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainPageCalc import MainPageCalc
from ResultPageCalc import ResultPageCalc
import allure

driver = webdriver.Chrome()
service = ChromeService(ChromeDriverManager().install())

@allure.epic("Домашняя работа №10")
@allure.feature("Задание 02. Калькулятор")

@allure.story("Сумма целых чисел")
@allure.title("Проверка вычисления суммы целых чисел")
@allure.description("Только целые числа")
@allure.severity("blocker")

def test_calc():
    
    mainpage = MainPageCalc(driver)
    resultpage = ResultPageCalc(driver)

    mainpage.delay(45)
    mainpage.send_key()

    result_text = resultpage.result_out()
    
    with allure.step("Проверка, что результат вычислений = {}".format(result_text)):
        assert result_text == "15", "Значение не равно 15"
    
    driver.quit()