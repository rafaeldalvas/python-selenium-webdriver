from selenium import webdriver
from pages.page_confirmar_presenca import confirmarPresenca
from utils.login import LoginProfessor

webdriver = webdriver.Chrome(r'd:\Downloads\chromedriver_win32\chromedriver.exe')

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login(
    login = 'testes.professor',
    senha = '6kmfDK'
)

confirmar_presenca = confirmarPresenca(webdriver)

# --------- Casos de teste: Confirmar presença padrão ------------#
# ---------- Casos de teste: Atividade sem inscrições ------------#
# ------------- Casos de teste: Atividade fechada ----------------#
# ------------- Casos de teste: Fechar atividade -----------------#