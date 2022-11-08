from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestPersonalAccount:
    def test_login_by_personal_account_button(self, login):
        #Кнопка Личный Кабинет
        login.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        #Используем явное ожидание по url
        WebDriverWait(login, 3).until(expected_conditions.url_contains("https://stellarburgers.nomoreparties.site/account"))
        #Сравниваем текущий урл с ожидаемым
        assert login.current_url == 'https://stellarburgers.nomoreparties.site/account'
