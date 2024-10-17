from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from MainPageForm import MainPageForm
from ResultPageForm import ResultPageForm
import allure

driver = webdriver.Chrome()
service = ChromeService(ChromeDriverManager().install())

@allure.step("Проверяем что поле Zip code подсвечено красным")
def zip_code_alert():
    """
    Функция проверки что поле "Zip code" подсвечено красным
    """
    zip_code_alert = driver.find_element(By.CSS_SELECTOR, "#zip-code.alert.py-2.alert-danger")
    with allure.step("Поле Zip code подсвечено красным"):
        assert zip_code_alert.is_displayed(), "Поле 'Zip code' не подсвечено красным"

@allure.step("Проверяем что поля подсвечены зеленым")
def green():
    """
    Функция проверки что поля подсвечены зеленым
    """
    pole = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
    for i in pole:
        y = "#" + i + ".alert.py-2.alert-success"
        alert = driver.find_element(By.CSS_SELECTOR, y)
        with allure.step("Поле " + i + " подсвечено зеленым"):
            assert alert.is_displayed(), "Поле не подсвечено зеленым"

@allure.epic("Домашняя работа №10")
@allure.feature("Задание 01. Заполнение формы")

@allure.story("Цвет фона полей")
@allure.title("Проверка свойств заполненных и незаполненных полей")
@allure.description("Свойство и значение передается в функции")
@allure.severity("minor")

def test_form():
    mainpage = MainPageForm(driver)
    resultpage = ResultPageForm(driver)
    
    mainpage.first_name("Иван")
    mainpage.last_name("Петров")
    mainpage.address("Ленина, 55-3")
    mainpage.email("test@skypro.com")
    mainpage.phone("+7985899998787")
    mainpage.zip_code("")
    mainpage.city("Москва")
    mainpage.country("Россия")
    mainpage.job_position("QA")
    mainpage.company("SkyPro")
    
    resultpage.click()
    zip_code_alert()
    green()
    
    driver.quit()