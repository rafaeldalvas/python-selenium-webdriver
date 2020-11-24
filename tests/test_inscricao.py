from time import sleep
from selenium import webdriver
from utils.login import LoginProfessor
from pages.page_inscricao import inscricao


webdriver = webdriver.Chrome(r'd:\Downloads\chromedriver_win32\chromedriver.exe')

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)
webdriver.maximize_window()

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login()

inscricao = inscricao(webdriver)

# ------------- Caso de teste: Inscrição padrão  -----------------#
def test_ct40():
    inscricao.caminho()
    inscricao.ct40_inscricao()
# ---------------- Prazo para inscrição vencido  -----------------#
def test_ct41():
    webdriver.get(url)
    inscricao.caminho(True)
    inscricao.ct41_inscricao()
# ------------------------ Ver Inscritos  ------------------------#
def test_ct42():
    webdriver.get(url)
    inscricao.caminho()
    inscricao.ct42_inscricao()
# ------------------- Horário indisponível  ----------------------#
def test_ct43():
    webdriver.get(url)
    inscricao.caminho()
    inscricao.ct43_inscricao()
