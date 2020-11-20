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
sleep(1)
certificadoParticipante.ct50_certificado_participante()

# ------------ Caso de teste: Geração de certificado padrão ---------------#
webdriver.get(url)
sleep(1)
editar_palestrante.tiraInscricao()
sleep(1)
editar_palestrante.caminho()
sleep(1)
editar_palestrante.ct51_certificado_participante()



