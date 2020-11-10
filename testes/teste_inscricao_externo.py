from selenium import webdriver
from pages.page_inscricao_externo import inscricaoExterno

webdriver = webdriver.Chrome(r'd:\Downloads\chromedriver_win32\chromedriver.exe')

url = "https://integra-h.nrc.ice.ufjf.br/integra/geral/menuEvento.zul"
webdriver.get(url)

# ---------- Casos de teste: Evento não selecionado --------------#
# - Casos de teste: Confirmar inscrição de usuário externo padrão-#
# ---------- Casos de teste: Prazo para inscrição vencido --------#
# --------------- Casos de teste: CPF inválido -------------------#
# -------------- Casos de teste: Email inválido ------------------#
# - Casos de teste: Campos obrigatórios no primeiro formulário ---#
# -- Casos de teste: Campos obrigatórios no segundo formulário ---#