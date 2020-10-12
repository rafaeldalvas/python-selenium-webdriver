from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from config import PageElement

browser = Chrome()
url = "https://integra-h.nrc.ice.ufjf.br/integra/restrito/pagInicial/professor/inicial.zul"
browser.get(url)


class loginProfessor(PageElement):
    login = (By.ID, 'username')
    senha = (By.ID, 'password')
    btn = (By.ID, 'login-submit')

    def realizaLogin(self, login, senha):
        self.webdriver.find_element(*self.login).send_keys(login)
        self.webdriver.find_element(*self.senha).send_keys(senha)
        self.webdriver.find_element(*self.btn).click()

# class loginAluno(PageElement):
