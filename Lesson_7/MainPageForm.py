from selenium.webdriver.common.by import By

class MainPageForm:

# заходим на сайт
   def __init__(self, driver):
    self._driver = driver
    self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    self._driver.maximize_window()

# Заполняем форму значениями

# First Name
   def first_name(self, f_n):
    firstname = self._driver.find_element(By.CSS_SELECTOR, "[name=first-name]").send_keys(f_n)

# Last Name
   def last_name(self, l_n):
    lastname = self._driver.find_element(By.CSS_SELECTOR, "[name=last-name]").send_keys(l_n)

# Address
   def address(self, adr):
    address = self._driver.find_element(By.CSS_SELECTOR, "[name=address]").send_keys(adr)

# E-mail
   def email(self, e_l):
    email = self._driver.find_element(By.CSS_SELECTOR, "[name=e-mail]").send_keys(e_l)

# Phone number
   def phone(self, ph_ne):
    phone = self._driver.find_element(By.CSS_SELECTOR, "[name=phone]").send_keys(ph_ne)

# Zip code
   def zip_code(self, z_c):
    zipcode = self._driver.find_element(By.CSS_SELECTOR, "[name=zip-code]").send_keys(z_c)

# City
   def city(self, c_y):
    city = self._driver.find_element(By.CSS_SELECTOR, "[name=city]").send_keys(c_y)

# Country
   def country(self, c_ry):
    country = self._driver.find_element(By.CSS_SELECTOR, "[name=country]").send_keys(c_ry)

# Job position
   def job_position(self, j_p):
    job = self._driver.find_element(By.CSS_SELECTOR, "[name=job-position]").send_keys(j_p)

# Company
   def company(self, c_ny):
    company = self._driver.find_element(By.CSS_SELECTOR, "[name=company]").send_keys(c_ny)