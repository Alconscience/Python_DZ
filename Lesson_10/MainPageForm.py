from selenium.webdriver.common.by import By
import allure

@allure.step("Заходим на сайт: https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

class MainPageForm:

   def __init__(self, driver):
    """
    Функция захода на сайт
    """
    self._driver = driver
    self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    self._driver.maximize_window()

   #@allure.step("Заполняем форму значениями:")

   @allure.step("Заполняем форму: First Name - {f_n}") 
   def first_name(self, f_n):
    """
    Функция ввода - First Name
    """
    firstname = self._driver.find_element(By.CSS_SELECTOR, "[name=first-name]").send_keys(f_n)

   @allure.step("Заполняем форму: Last Name - {l_n}") 
   def last_name(self, l_n):
    """
    Функция ввода - Last Name
    """
    lastname = self._driver.find_element(By.CSS_SELECTOR, "[name=last-name]").send_keys(l_n)

   @allure.step("Заполняем форму: Address - {adr}") 
   def address(self, adr):
    """
    Функция ввода - Address
    """
    address = self._driver.find_element(By.CSS_SELECTOR, "[name=address]").send_keys(adr)

   @allure.step("Заполняем форму: Email - {e_l}") 
   def email(self, e_l):
    """
    Функция ввода - Email
    """
    email = self._driver.find_element(By.CSS_SELECTOR, "[name=e-mail]").send_keys(e_l)

   @allure.step("Заполняем форму: Phone number - {ph_ne}") 
   def phone(self, ph_ne):
    """
    Функция ввода - Phone number
    """
    phone = self._driver.find_element(By.CSS_SELECTOR, "[name=phone]").send_keys(ph_ne)

   @allure.step("Заполняем форму: Zip code - {z_c}") 
   def zip_code(self, z_c):
    """
    Функция ввода - Zip code
    """
    zipcode = self._driver.find_element(By.CSS_SELECTOR, "[name=zip-code]").send_keys(z_c)

   @allure.step("Заполняем форму: City - {c_y}") 
   def city(self, c_y):
    """
    Функция ввода - City
    """
    city = self._driver.find_element(By.CSS_SELECTOR, "[name=city]").send_keys(c_y)

   @allure.step("Заполняем форму: Country - {c_ry}") 
   def country(self, c_ry):
    """
    Функция ввода - Country
    """
    country = self._driver.find_element(By.CSS_SELECTOR, "[name=country]").send_keys(c_ry)

   @allure.step("Заполняем форму: Job position - {j_p}") 
   def job_position(self, j_p):
    """
    Функция ввода - Jop position
    """
    job = self._driver.find_element(By.CSS_SELECTOR, "[name=job-position]").send_keys(j_p)

   @allure.step("Заполняем форму: Company - {c_ny}") 
   def company(self, c_ny):
    """
    Функция ввода - Company
    """
    company = self._driver.find_element(By.CSS_SELECTOR, "[name=company]").send_keys(c_ny)