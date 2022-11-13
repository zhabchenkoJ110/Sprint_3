import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture
def email():
    return 'testovtest1888@yandex.ru'

@pytest.fixture
def password():
    return 'test12345'

@pytest.fixture
def login(driver, email, password):
    #Кнопка Войти в аккаунт
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    #Ввод email
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys(email)
    #Ввод password
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
    #Кнопка Войти
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
    return driver

@pytest.fixture
def fake_email(): #генерация email
    fake = Faker()
    return fake.email()

@pytest.fixture
def fake_name(): #генерация имени
    fake = Faker()
    return fake.first_name()

@pytest.fixture
def fake_password(): #генерация пароля
    fake = Faker()
    return fake.password(length=6)


