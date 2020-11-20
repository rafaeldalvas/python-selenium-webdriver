from selenium import webdriver
from pages.page_certificado_participante_externo import certificadoParticipanteExterno

webdriver = webdriver.Chrome()

url = "https://integra-h.nrc.ice.ufjf.br/integra/geral/menuEvento.zul"

certificado_participante_externo = certificadoParticipanteExterno(webdriver)

# --------- Casos de teste: Geração de certificado padrão --------#
webdriver.get(url)
certificado_participante_externo.caminho()
certificado_participante_externo.ct62_certificado_participante_externo(
    cpf = '66488349007'
)
# --------------- Casos de teste: CPF inválido -------------------#
webdriver.get(url)
certificado_participante_externo.caminho()
certificado_participante_externo.ct63_certificado_participante_externo(
    cpf = '99999999999'
)
# ------------ Casos de teste: CPF não cadastrado ----------------#
webdriver.get(url)
certificado_participante_externo.caminho()
certificado_participante_externo.ct63_certificado_participante_externo(
    cpf = '54616745005'
)
webdriver.close()
