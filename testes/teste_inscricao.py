from time import sleep
from selenium import webdriver
from utils.login import LoginProfessor
from pages.page_inscricao import inscricao


webdriver = webdriver.Chrome(r'd:\Downloads\chromedriver_win32\chromedriver.exe')

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login(
    login = 'testes.professor',
    senha = '6kmfDK'
)

inscricao = inscricao(webdriver)

# ------------ Caso de teste: Inscrição padrão  ---------------#
inscricao.caminho(True)
inscricao.ct40_inscricao()

# ------------ Prazo para inscrição vencido  ---------------#
sleep(1)
webdriver.get(url)
sleep(1)
inscricao.caminho(False, True)
inscricao.ct41_inscricao()

# ------------ Ver Inscritos  ---------------#
sleep(1)
webdriver.get(url)
sleep(1)
inscricao.caminho(True)
inscricao.ct42_inscricao()

# ------------ Horário indisponível  ---------------#
sleep(1)
webdriver.get(url)
sleep(1)
inscricao.caminho(True)
inscricao.ct43_inscricao()

