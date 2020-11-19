from selenium import webdriver
from pages.page_certificado_palestrante import certificadoPalestrante
from utils.login import LoginProfessor

webdriver = webdriver.Chrome(r'd:\Downloads\chromedriver_win32\chromedriver.exe')

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login(
    login = 'testes.professor',
    senha = '6kmfDK'
)

certificado_palestrante = certificadoPalestrante(webdriver)

# --- Casos de teste: Gerar Certificado Para Palestrando padrão --#
webdriver.get(url)
certificado_palestrante.caminho()
certificado_palestrante.ct37_certificado_palestrante()
# ---------- Casos de teste: Evento não selecionado --------------#
webdriver.get(url)
certificado_palestrante.caminho()
certificado_palestrante.ct38_certificado_palestrante()
# --------- Casos de teste: Atividade não especificada -----------#
webdriver.get(url)
certificado_palestrante.caminho()
certificado_palestrante.ct39_certificado_palestrante()