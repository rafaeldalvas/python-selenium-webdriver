from time import sleep
from selenium import webdriver
from utils.login import LoginProfessor
from pages.page_inscricao import inscricao


webdriver = webdriver.Chrome(r'd:\Downloads\chromedriver_win32\chromedriver.exe')

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login()

inscricao = inscricao(webdriver)

# ------------- Caso de teste: Inscrição padrão  -----------------#
inscricao.caminho(True)
inscricao.ct40_inscricao()
# ---------------- Prazo para inscrição vencido  -----------------#
webdriver.get(url)
inscricao.caminho(False, True)
inscricao.ct41_inscricao()
# ------------------------ Ver Inscritos  ------------------------#
webdriver.get(url)
inscricao.caminho(True)
inscricao.ct42_inscricao()
# ------------------- Horário indisponível  ----------------------#
webdriver.get(url)
inscricao.caminho(True)
inscricao.ct43_inscricao()

webdriver.close()

