from selenium import webdriver
from pages.page_certificado_participante_externo import certificadoParticipanteExterno

webdriver = webdriver.Chrome()
webdriver.maximize_window()

url = "https://integra-h.nrc.ice.ufjf.br/integra/geral/menuEvento.zul"

certificado_participante_externo = certificadoParticipanteExterno(webdriver)

# --------- Casos de teste: Geração de certificado padrão --------#
def test_ct62():
    webdriver.get(url)
    certificado_participante_externo.caminho()
    certificado_participante_externo.ct62_certificado_participante_externo(
        cpf = '94030784054'
    )
# --------------- Casos de teste: CPF inválido -------------------#
def test_ct63():
    webdriver.get(url)
    certificado_participante_externo.caminho()
    certificado_participante_externo.ct63_certificado_participante_externo(
        cpf = '99999999999'
    )
# ------------ Casos de teste: CPF não cadastrado ----------------#
def test_ct64():
    webdriver.get(url)
    certificado_participante_externo.caminho()
    certificado_participante_externo.ct63_certificado_participante_externo(
        cpf = '54616745005'
    )

