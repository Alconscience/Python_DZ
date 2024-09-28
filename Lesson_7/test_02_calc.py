from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainPageCalc import MainPageCalc
from ResultPageCalc import ResultPageCalc

driver = webdriver.Chrome()
service = ChromeService(ChromeDriverManager().install())

def test_calc():
    mainpage = MainPageCalc(driver)
    resultpage = ResultPageCalc(driver)

    mainpage.delay(45)
    mainpage.send_key()

    result_text = resultpage.result_out()
    assert result_text == "15", "Значение не равно 15"
    
    driver.quit()