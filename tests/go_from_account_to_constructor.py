from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestFromAccountToConstructor:
    def test_click_to_constructor(self, login):
        #Кнопка Личный Кабинет
        login.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        #Кнопка Конструктор
        login.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        #Явное ожидание поке элемент не станет видимым «Соберите бургер»
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))

    def test_click_to_logo(self, login):
        #Кнопка Личный Кабинет
        login.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        #Кнопка логотип
        login.find_element(By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]").click()
        #Явное ожидание поке элемент не станет видимым «Соберите бургер»
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))
