from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
service = ChromeService(ChromeDriverManager().install())

# заходим на сайт

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# Заполняем форму значениями

# First Name
FirstName = driver.find_element(By.CSS_SELECTOR, "[name=first-name]")
FirstName.send_keys("Иван")

# Last Name
LastName = driver.find_element(By.CSS_SELECTOR, "[name=last-name]")
LastName.send_keys("Петров")

# Address
Address = driver.find_element(By.CSS_SELECTOR, "[name=address]")
Address.send_keys("Ленина, 55-3")

# E-mail
Email = driver.find_element(By.CSS_SELECTOR, "[name=e-mail]")
Email.send_keys("test@skypro.com")

# Phone number
Phone = driver.find_element(By.CSS_SELECTOR, "[name=phone]")
Phone.send_keys("+7985899998787")

# Zip code
ZipCode = driver.find_element(By.CSS_SELECTOR, "[name=zip-code]")
ZipCode.send_keys("")

# City
City = driver.find_element(By.CSS_SELECTOR, "[name=city]")
City.send_keys("Москва")

# Country
Country = driver.find_element(By.CSS_SELECTOR, "[name=country]")
Country.send_keys("Россия")

# Job position
Job = driver.find_element(By.CSS_SELECTOR, "[name=job-position]")
Job.send_keys("QA")

# Company
Company = driver.find_element(By.CSS_SELECTOR, "[name=company]")
Company.send_keys("SkyPro")

# нажатие на кнопку "Submit"

driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3").click()

# проверяем что поле "Zip code" подсвечено красным

Zip_Code_Alert = driver.find_element(By.CSS_SELECTOR, "#zip-code.alert.py-2.alert-danger")
assert Zip_Code_Alert.is_displayed(), "Поле 'Zip code' не подсвечено красным"

# проверяем что поля подсвечены зеленым

Pole = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
for i in Pole:
    y = "#" + i + ".alert.py-2.alert-success"
    Alert = driver.find_element(By.CSS_SELECTOR, y)
    assert Alert.is_displayed(), "Поле не подсвечено зеленым"

driver.quit()