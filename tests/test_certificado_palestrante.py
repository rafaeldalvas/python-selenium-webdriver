from selenium import webdriver
from pages.page_certificado_palestrante import certificadoPalestrante
from utils.login import LoginProfessor

webdriver = webdriver.Chrome()

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)
webdriver.maximize_window()

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login()

certificado_palestrante = certificadoPalestrante(webdriver)

# --- Casos de teste: Gerar Certificado Para Palestrando padrão --#
def test_ct37():
    webdriver.get(url)
    certificado_palestrante.caminho()
    certificado_palestrante.ct37_certificado_palestrante()
# ---------- Casos de teste: Evento não selecionado --------------#
def test_ct38():
    webdriver.get(url)
    certificado_palestrante.caminho()
    certificado_palestrante.ct38_certificado_palestrante()
# --------- Casos de teste: Atividade não especificada -----------#
def test_ct39():
    webdriver.get(url)
    certificado_palestrante.caminho()
    certificado_palestrante.ct39_certificado_palestrante()
