from selenium.webdriver.common.by import By

class TestRegistration:

    def test_successful_registration(self, driver, fake_name, fake_email, fake_password):
        #Кнопка Личный кабинет
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        #Кнопка Зарегистрироваться
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        #Ввод имени
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys(fake_name)
        #Ввод email
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys(fake_email)
        #Ввод пароля
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]").send_keys(fake_password)
        #Клик по кнопке Зарегистрироваться
        driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()

    def test_incorrect_password_error(self, driver, fake_name, fake_email):
        #Кнопка Личный кабинет
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        #Кнопка Зарегистрироваться
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        #Ввод имени
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys(fake_name)
        #Ввод email
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys(fake_email)
        #Ввод некорректного пароля
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]").send_keys("12345")
        #Клик по кнопке Зарегистрироваться
        driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
        #Проверка, что появилось сообщение об ошибке
        assert driver.find_element(By.XPATH, "//p[contains(text(),'Некорректный пароль')]").text == 'Некорректный пароль'