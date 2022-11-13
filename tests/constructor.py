from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructorSection:
    def test_constructor_section_bun(self, login):
        #Кнопка Конструктор
        login.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        #Кнопка «Соусы»(для того чтобы кнопка «Булки» была доступна)
        login.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()
        #Кнопка Булки
        login.find_element(By.XPATH, "//span[contains(text(), 'Булки')]").click()
        #Ожидание раздела «Булки»
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Булки')]")))
        assert login.find_element(By.XPATH, "//h2[contains(text(),'Булки')]").text == 'Булки'

    def test_constructor_section_sauces(self, login):
        #Кнопка Конструктор
        login.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        #Кнопка Соусы
        login.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()
        #Ожидание раздела «Соусы»
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Соусы')]")))
        assert login.find_element(By.XPATH, "//h2[contains(text(),'Соусы')]").text == 'Соусы'

    def test_constructor_section_toppings(self, login):
        #Кнопка Конструктор
        login.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        #Кнопка Начинки
        login.find_element(By.XPATH, "//span[contains(text(), 'Начинки')]").click()
        #Ожидание раздела «Начинки»
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Начинки')]")))
        assert login.find_element(By.XPATH, "//h2[contains(text(),'Начинки')]").text == 'Начинки'