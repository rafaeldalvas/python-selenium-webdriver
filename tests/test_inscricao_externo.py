from selenium import webdriver
from pages.page_inscricao_externo import inscricaoExterno

webdriver = webdriver.Chrome()
webdriver.maximize_window()

url = "https://integra-h.nrc.ice.ufjf.br/integra/geral/menuEvento.zul"

inscricao_externo = inscricaoExterno(webdriver)

#-- Casos de teste: Confirmar inscrição de usuário externo padrão-#
def test_ct52():
    webdriver.get(url)
    inscricao_externo.caminho()
    inscricao_externo.ct52_inscricao_externo(
        cpf         = '99363302008',
        nome        = 'Participante Externo Teste',
        email       = 'pexterno@teste.com',
        telefone    = '43663746970',
        celular     = '51405831810'
    )
# ---------- Casos de teste: Prazo para inscrição vencido --------#
def test_ct53():
    webdriver.get(url)
    inscricao_externo.caminho(True)
    inscricao_externo.ct53_inscricao_externo(
        cpf         = '24643211091',
        nome        = 'Participante Externo Teste 2',
        email       = 'pexterno2@teste.com',
        telefone    = '43663346970',
        celular     = '51405531810'
    )
# --------------- Casos de teste: CPF inválido -------------------#
def test_ct54():
    webdriver.get(url)
    inscricao_externo.caminho()
    inscricao_externo.ct54_inscricao_externo(
        cpf     = '12345678900',
        nome    = 'Participante Externo Teste 3',
        email   = 'pexterno3@teste.com',
    )
# -------------- Casos de teste: Email inválido ------------------#
def test_ct55():
    webdriver.get(url)
    inscricao_externo.caminho()
    inscricao_externo.ct55_inscricao_externo(
        cpf     = '78160965001',
        nome    = 'Participante Externo Teste 4',
        email   = 'emailinvalidoteste'
    )
# - Casos de teste: Campos obrigatórios no primeiro formulário ---#
def test_ct56():
    webdriver.get(url)
    inscricao_externo.caminho()
    inscricao_externo.ct56_inscricao_externo(
        cpf     = '43828955029',
        nome    = 'Participante Externo Teste 5',
        email   = 'pexterno5@teste.com'
    )
# -- Casos de teste: Campos obrigatórios no segundo formulário ---#
def test_ct57():
    webdriver.get(url)
    inscricao_externo.caminho()
    inscricao_externo.ct57_inscricao_externo(
        cpf         = '94196348092',
        nome        = 'Participante Externo Teste 6',
        email       = 'pexterno6@teste.com',
        telefone    = '43663346975',
        celular     = '51405531814'
    )
