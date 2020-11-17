from selenium import webdriver
from pages.page_certificado_palestrante_externo import certificadoPalestranteExterno

webdriver = webdriver.Chrome(r'd:\Downloads\chromedriver_win32\chromedriver.exe')

url = "https://integra-h.nrc.ice.ufjf.br/integra/geral/menuEvento.zul"

certificado_palestrante_externo = certificadoPalestranteExterno(webdriver)

# --------- Casos de teste: Geração de certificado padrão --------#
webdriver.get(url)
certificado_palestrante_externo.caminho()
# --------- Casos de teste: Palestrante sem eventos --------------#
# --------------- Casos de teste: CPF inválido -------------------#
# ------------ Casos de teste: CPF não cadastrado ----------------#
