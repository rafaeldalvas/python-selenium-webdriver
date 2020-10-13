from selenium.webdriver.common.by import By
from utils.config import PageElement
from time import sleep


class LoginProfessor(PageElement):

    login = (By.ID, 'username')
    senha = (By.ID, 'password')
    btn = (By.ID, 'login-submit')

    def realiza_login(self, login, senha):
        self.find_element(self.login).send_keys(login)
        self.find_element(self.senha).send_keys(senha)
        sleep(2)
        self.find_element(self.btn).click()
