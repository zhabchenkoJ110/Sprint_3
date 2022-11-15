from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


class TestLogin:
    def test_login_by_login_button_on_main_page(self, driver, email, password):
        #Кнопка Войти в аккаунт
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        # Вводим email
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys(email)
        # Вводим password
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        # Клик по кнопке Войти
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        # Кнопка Оформить заказ
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(),'Оформить заказ')]").text == "Оформить заказ"

    def test_login_by_personal_account_button(self, driver, email, password):
        #Кнопка Личный Кабинет
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        # Вводим email
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys(email)
        # Вводим password
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        # Клик по кнопке Войти
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        # Кнопка Оформить заказ
        # вот я использую ожидание
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(),'Оформить заказ')]").text == "Оформить заказ"

    def test_login_through_button_in_registration_page(self, driver, email, password):
        #Кнопка Личный Кабинет
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        #Кнопка Зарегистрироваться
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        #Кнопка Войти
        driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()
        # Вводим email
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys(email)
        # Вводим password
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        # Клик по кнопке Войти
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        # Кнопка Оформить заказ
        # вот я использую ожидание
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(),'Оформить заказ')]").text == "Оформить заказ"

    def test_login_through_button_in_forgot_password_page(self,  driver, email, password):
        #Кнопка Личный Кабинет
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        #Кнопка Восстановить пароль
        driver.find_element(By.XPATH, "//a[contains(text(),'Восстановить пароль')]").click()
        #Кнопка Войти
        driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()
        # Вводим email
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys(email)
        # Вводим password
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        # Клик по кнопке Войти
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        # Кнопка Оформить заказ
        # вот я использую ожидание
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(),'Оформить заказ')]").text == "Оформить заказ"