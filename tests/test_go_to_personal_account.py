from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestPersonalAccount:
    def test_login_by_personal_account_button(self, login):
        # Кнопка Личный Кабинет
        login.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        # Используем явное ожидание по url
        WebDriverWait(login, 5).until(EC.url_contains("https://stellarburgers.nomoreparties.site"
                                                      "/account/profile"))
        # Сравниваем текущий урл с ожидаемым
        assert login.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
