from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainPageShop import MainPageShop
from ResultPageShop import ResultPageShop
import allure

driver = webdriver.Chrome()
service = ChromeService(ChromeDriverManager().install())

@allure.epic("Домашняя работа №10")
@allure.feature("Задание 03. Интернет-магазин")

@allure.story("Итоговая сумма заказа")
@allure.title("Проверка итоговой суммы заказа")
@allure.description("")
@allure.severity("blocker")

def test_shop():
    mainpage = MainPageShop(driver)
    resultpage = ResultPageShop(driver)
    
    mainpage.authorization("standard_user", "secret_sauce")
    mainpage.send_batton()
    mainpage.send_tovar()
    mainpage.check_cart()

    resultpage.send_check()
    resultpage.first_name("Alexandr")
    resultpage.last_name("Sviridov")
    resultpage.postcode("123456")
    resultpage.send_cont()
        
    total_sum = resultpage.total()

    driver.quit()
    with allure.step("Проверка, что итоговая сумма заказа = {}".format(total_sum)):
        assert total_sum == "Total: $58.29", "Сумма товаров не совпадает"