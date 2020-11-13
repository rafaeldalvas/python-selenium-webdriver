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

# -------- Casos de teste: Confirmar inscrição padrão ------------#
# confirmar_inscricao.caminho()
# confirmar_inscricao.ct44_confirmar_inscricao()
# ----------- Casos de teste: Ver todas inscrições ---------------#
# confirmar_inscricao.caminho()
# confirmar_inscricao.ct45_confirmar_inscricao()
# -------- Casos de teste: Ver relatório de inscritos ------------#
# confirmar_inscricao.caminho()
# confirmar_inscricao.ct46_confirmar_inscricao()
# ----- Casos de teste: Ver relatório de inscritos efetivados ----#
confirmar_inscricao.caminho()
confirmar_inscricao.ct47_confirmar_inscricao()
# ------------ Casos de teste: Campo evento vazio ----------------#
# ----------- Casos de teste: Campo atividade vazio --------------#
