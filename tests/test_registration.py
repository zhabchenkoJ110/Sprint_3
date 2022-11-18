from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:

    def test_successful_registration(self, driver, fake_name, fake_email, fake_password):
        #Кнопка Личный кабинет
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        #Кнопка Зарегистрироваться
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        #Ввод имени
        driver.find_element(By.XPATH, "//label[text()='Имя']/following::input[@type='text']").send_keys(fake_name)
        #Ввод email
        driver.find_element(By.XPATH, "//label[text()='Email']/following::input[@type='text']").send_keys(fake_email)
        #Ввод пароля
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(fake_password)
        #Клик по кнопке Зарегистрироваться
        driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Вход')]")))
        assert driver.find_element(By.XPATH, "//h2[contains(text(),'Вход')]").text == "Вход"

    def test_incorrect_password_error(self, driver, fake_name, fake_email):
        #Кнопка Личный кабинет
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        #Кнопка Зарегистрироваться
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        #Ввод имени
        driver.find_element(By.XPATH, "//label[text()='Имя']/following::input[@type='text']").send_keys(fake_name)
        #Ввод email
        driver.find_element(By.XPATH, "//label[text()='Email']/following::input[@type='text']").send_keys(fake_email)
        #Ввод некорректного пароля
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("12345")
        #Клик по кнопке Зарегистрироваться
        driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
        #Проверка, что появилось сообщение об ошибке
        assert driver.find_element(By.XPATH, "//p[contains(text(),'Некорректный пароль')]").text == 'Некорректный пароль'