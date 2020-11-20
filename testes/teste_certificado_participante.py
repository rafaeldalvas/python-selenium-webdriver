from time import sleep
from selenium import webdriver

from pages.page_certificado_participante import certificadoParticipante
from utils.login import LoginProfessor

webdriver = webdriver.Chrome()

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login()

editar_palestrante = certificadoParticipante(webdriver)

# ------------ Caso de teste: Geração de certificado padrão ---------------#
editar_palestrante.caminho()
certificadoParticipante.ct50_certificado_participante()

# ------------ Caso de teste: Geração de certificado padrão ---------------#
webdriver.get(url)
editar_palestrante.tiraInscricao()
editar_palestrante.caminho()
editar_palestrante.ct51_certificado_participante()



