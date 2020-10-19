from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.config import PageElement
from time import sleep


class LoginProfessor(PageElement):

    login = (By.ID, 'username')
    senha = (By.ID, 'password')
    btn = (By.ID, 'login-submit')

    def realiza_login(self, login, senha):
        id_field = WebDriverWait(self.webdriver, poll_frequency=0.2, timeout=10)
        id_field.until(expected_conditions.visibility_of_element_located(self.login))
        if id_field is not None:
            self.find_element(self.login).send_keys(login)
            self.find_element(self.senha).send_keys(senha)
            sleep(2)
            self.find_element(self.btn).click()