import allure
from selenium import webdriver
from pages.page_certificado_palestrante_externo import CertificadoPalestranteExterno

webdriver = webdriver.Chrome()
webdriver.maximize_window()

url = "https://integra-h.nrc.ice.ufjf.br/integra/geral/menuEvento.zul"

certificado_palestrante_externo = CertificadoPalestranteExterno(webdriver)

# --------- Casos de teste: Geração de certificado padrão --------#
def test_ct58():
    webdriver.get(url)
    certificado_palestrante_externo.caminho()
    certificado_palestrante_externo.ct58_certificado_palestrante_externo(
        cpf = '83239472600'
    )

# --------- Casos de teste: Palestrante sem eventos --------------#
def test_ct59():
    webdriver.get(url)
    certificado_palestrante_externo.caminho()
    certificado_palestrante_externo.ct59_certificado_palestrante_externo(
        cpf = '62126930050'
    )
# --------------- Casos de teste: CPF inválido -------------------#
def test_ct60():
    webdriver.get(url)
    certificado_palestrante_externo.caminho()
    certificado_palestrante_externo.ct60_certificado_palestrante_externo(
        cpf = '99999999999'
    )
# ------------ Casos de teste: CPF não cadastrado ----------------#
def test_ct61():
    webdriver.get(url)
    certificado_palestrante_externo.caminho()
    certificado_palestrante_externo.ct61_certificado_palestrante_externo(
        cpf = '33332506080'
    )
