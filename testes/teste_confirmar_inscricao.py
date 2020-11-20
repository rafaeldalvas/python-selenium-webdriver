from selenium import webdriver
from pages.page_confirmar_inscricao import confirmarInscricao
from utils.login import LoginProfessor

webdriver = webdriver.Chrome()

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login()

confirmar_inscricao = confirmarInscricao(webdriver)

# -------- Casos de teste: Confirmar inscrição padrão ------------#
confirmar_inscricao.caminho()
confirmar_inscricao.ct44_confirmar_inscricao()
# ----------- Casos de teste: Ver todas inscrições ---------------#
webdriver.get(url)
confirmar_inscricao.caminho()
confirmar_inscricao.ct45_confirmar_inscricao()
# -------- Casos de teste: Ver relatório de inscritos ------------#
webdriver.get(url)
confirmar_inscricao.caminho()
confirmar_inscricao.ct46_confirmar_inscricao()
# ----- Casos de teste: Ver relatório de inscritos efetivados ----#
webdriver.get(url)
confirmar_inscricao.caminho()
confirmar_inscricao.ct47_confirmar_inscricao()
# ------------ Casos de teste: Campo evento vazio ----------------#
webdriver.get(url)
confirmar_inscricao.caminho()
confirmar_inscricao.ct48_confirmar_inscricao()
# ----------- Casos de teste: Campo atividade vazio --------------#
webdriver.get(url)
confirmar_inscricao.caminho()
confirmar_inscricao.ct49_confirmar_inscricao()

webdriver.close()
