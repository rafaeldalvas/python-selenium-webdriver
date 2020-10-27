from selenium import webdriver
from pages.page_editar_evento import editarEvento
from utils.login import LoginProfessor

webdriver = webdriver.Chrome(r'd:\Downloads\chromedriver_win32\chromedriver.exe')

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login(
    login = 'testes.professor',
    senha = '6kmfDK'
)
