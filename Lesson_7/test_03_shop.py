from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainPageShop import MainPageShop
from ResultPageShop import ResultPageShop

driver = webdriver.Chrome()
service = ChromeService(ChromeDriverManager().install())

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
    resultpage.total()
    
    total_sum = resultpage.total()

    driver.quit()
    
    assert total_sum == "Total: $58.29", "Сумма товаров не совпадает"