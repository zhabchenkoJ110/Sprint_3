from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructorSection:
    def test_constructor_section_bun(self, login):
        #Кнопка Конструктор
        login.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        #Кнопка «Соусы»(для того чтобы кнопка «Булки» была доступна)
        login.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[2]").click()
        #Кнопка Булки
        login.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[1]").click()
        #Ожидание раздела «Булки»
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Булки')]")))

    def test_constructor_section_sauces(self, login):
        #Кнопка Конструктор
        login.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        #Кнопка Соусы
        login.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[2]").click()
        #Ожидание раздела «Соусы»
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Соусы')]")))

    def test_constructor_section_toppings(self, login):
        #Кнопка Конструктор
        login.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        #Кнопка Начинки
        login.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[3]").click()
        #Ожидание раздела «Начинки»
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Начинки')]")))