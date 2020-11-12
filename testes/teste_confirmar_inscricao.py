from selenium import webdriver
from pages.page_confirmar_inscricao import confirmarInscricao
from utils.login import LoginProfessor

webdriver = webdriver.Chrome(r'd:\Downloads\chromedriver_win32\chromedriver.exe')

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login(
    login = 'testes.professor',
    senha = '6kmfDK'
)

confirmar_inscricao = confirmarInscricao(webdriver)

# ---------- Casos de teste: Evento não selecionado --------------#
confirmar_inscricao.caminho()
# -------- Casos de teste: Confirmar inscrição padrão ------------#
# ----------- Casos de teste: Ver todas inscrições ---------------#
# -------- Casos de teste: Ver relatório de inscritos ------------#
# ----- Casos de teste: Ver relatório de inscritos efetivados ----#
# ------------ Casos de teste: Campo evento vazio ----------------#
# ----------- Casos de teste: Campo atividade vazio --------------#
