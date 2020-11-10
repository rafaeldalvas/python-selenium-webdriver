from selenium import webdriver
from pages.page_inscricao_externo import inscricaoExterno

webdriver = webdriver.Chrome(r'd:\Downloads\chromedriver_win32\chromedriver.exe')

url = "https://integra-h.nrc.ice.ufjf.br/integra/geral/menuEvento.zul"

inscricao_externo = inscricaoExterno(webdriver)

# ---------- Casos de teste: Evento não selecionado --------------#
webdriver.get(url)
inscricao_externo.caminho()
inscricao_externo.ct50_inscricao_externo(
    cpf = '96055817012',
    nome = 'Participante Externo Teste',
    email = 'pexterno@teste.com',
    telefone = '43663746970',
    celular = '51405831810'
)

# - Casos de teste: Confirmar inscrição de usuário externo padrão-#
# ---------- Casos de teste: Prazo para inscrição vencido --------#
# --------------- Casos de teste: CPF inválido -------------------#
# -------------- Casos de teste: Email inválido ------------------#
# - Casos de teste: Campos obrigatórios no primeiro formulário ---#
# -- Casos de teste: Campos obrigatórios no segundo formulário ---#