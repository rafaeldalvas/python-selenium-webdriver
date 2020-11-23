from selenium import webdriver
from pages.page_confirmar_presenca import confirmarPresenca
from utils.login import LoginProfessor

webdriver = webdriver.Chrome()

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login()

confirmar_presenca = confirmarPresenca(webdriver)

# --------- Casos de teste: Confirmar presença padrão ------------#
webdriver.get(url)
confirmar_presenca.caminho()
confirmar_presenca.ct33_confirmar_presenca()
# ---------- Casos de teste: Atividade sem inscrições ------------#
webdriver.get(url)
confirmar_presenca.caminho()
confirmar_presenca.ct34_confirmar_presenca()
# ------------- Casos de teste: Atividade fechada ----------------#
webdriver.get(url)
confirmar_presenca.caminho()
confirmar_presenca.ct35_confirmar_presenca()
# ------------- Casos de teste: Fechar atividade -----------------#
webdriver.get(url)
confirmar_presenca.caminho()
confirmar_presenca.ct36_confirmar_presenca()

webdriver.close()