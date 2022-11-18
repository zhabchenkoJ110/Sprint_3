from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLogout:
    def test_logout(self, login):
        #Кнопка Личный Кабинет
        login.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        #Явное ожидание загрузки кнопки Выход
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Выход')]")))
        #Кнопка Выход
        login.find_element(By.XPATH, "//button[contains(text(),'Выход')]").click()
        #Явное ожидание загрузки кнопки Войти
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]")))
        #Проверяем корректность url
        assert login.current_url == 'https://stellarburgers.nomoreparties.site/login'
