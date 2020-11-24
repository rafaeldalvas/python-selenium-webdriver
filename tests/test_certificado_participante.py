from time import sleep
from selenium import webdriver

from pages.page_certificado_participante import certificadoParticipante
from utils.login import LoginProfessor

webdriver = webdriver.Chrome()
webdriver.maximize_window()

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login()

cetificado_participante = certificadoParticipante(webdriver)

# ------------ Caso de teste: Geração de certificado padrão ---------------#
def test_ct50():
    cetificado_participante.caminho()
    cetificado_participante.ct50_certificado_participante()

# ------------ Caso de teste: Geração de certificado padrão ---------------#
def test_ct51():
    webdriver.get(url)
    cetificado_participante.tiraInscricao()
    cetificado_participante.caminho()
    cetificado_participante.ct51_certificado_participante()
