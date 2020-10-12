from abc import ABC
from selenium.webdriver import Chrome

from config import PageElement

browser = Chrome()
url = "https://integra-h.nrc.ice.ufjf.br/integra/restrito/pagInicial/professor/inicial.zul"


class loginProfessor(PageElement):
    browser.get(url)





class loginAluno(PageElement):
    browser.get(url)
