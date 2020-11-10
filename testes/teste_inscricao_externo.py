from selenium import webdriver
from pages.page_inscricao_externo import inscricaoExterno

webdriver = webdriver.Chrome(r'd:\Downloads\chromedriver_win32\chromedriver.exe')

url = "https://integra-h.nrc.ice.ufjf.br/integra/geral/menuEvento.zul"

inscricao_externo = inscricaoExterno(webdriver)

# - Casos de teste: Confirmar inscrição de usuário externo padrão-#
webdriver.get(url)
inscricao_externo.caminho()
inscricao_externo.ct50_inscricao_externo(
    cpf = '80737996005',
    nome = 'Participante Externo Teste',
    email = 'pexterno@teste.com',
    telefone = '43663746970',
    celular = '51405831810'
)
# ---------- Casos de teste: Prazo para inscrição vencido --------#
webdriver.get(url)
inscricao_externo.caminho(True)
inscricao_externo.ct51_inscricao_externo(
    cpf = '76455793072',
    nome = 'Participante Externo Teste 2',
    email = 'pexterno2@teste.com',
    telefone = '43663346970',
    celular = '51405531810'
)
# --------------- Casos de teste: CPF inválido -------------------#
webdriver.get(url)
inscricao_externo.caminho()
inscricao_externo.ct52_inscricao_externo(
    cpf = '12345678900',
    nome = 'Participante Externo Teste 3',
    email = 'pexterno2@teste.com',
)
# -------------- Casos de teste: Email inválido ------------------#
webdriver.get(url)
inscricao_externo.caminho()
inscricao_externo.ct53_inscricao_externo(
    cpf = '58796673087',
    nome = 'Participante Externo Teste 4',
    email = 'emailinvalidoteste',
)
# - Casos de teste: Campos obrigatórios no primeiro formulário ---#
# -- Casos de teste: Campos obrigatórios no segundo formulário ---#