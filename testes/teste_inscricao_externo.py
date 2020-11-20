from selenium import webdriver
from pages.page_inscricao_externo import inscricaoExterno

webdriver = webdriver.Chrome()

url = "https://integra-h.nrc.ice.ufjf.br/integra/geral/menuEvento.zul"

inscricao_externo = inscricaoExterno(webdriver)

#-- Casos de teste: Confirmar inscrição de usuário externo padrão-#
webdriver.get(url)
inscricao_externo.caminho()
inscricao_externo.ct52_inscricao_externo(
    cpf         = '66488349007',
    nome        = 'Participante Externo Teste',
    email       = 'pexterno@teste.com',
    telefone    = '43663746970',
    celular     = '51405831810'
)
# ---------- Casos de teste: Prazo para inscrição vencido --------#
webdriver.get(url)
inscricao_externo.caminho(True)
inscricao_externo.ct53_inscricao_externo(
    cpf         = '64380400026',
    nome        = 'Participante Externo Teste 2',
    email       = 'pexterno2@teste.com',
    telefone    = '43663346970',
    celular     = '51405531810'
)
# --------------- Casos de teste: CPF inválido -------------------#
webdriver.get(url)
inscricao_externo.caminho()
inscricao_externo.ct54_inscricao_externo(
    cpf     = '12345678900',
    nome    = 'Participante Externo Teste 3',
    email   = 'pexterno3@teste.com',
)
# -------------- Casos de teste: Email inválido ------------------#
webdriver.get(url)
inscricao_externo.caminho()
inscricao_externo.ct55_inscricao_externo(
    cpf     = '58796673087',
    nome    = 'Participante Externo Teste 4',
    email   = 'emailinvalidoteste'
)
# - Casos de teste: Campos obrigatórios no primeiro formulário ---#
webdriver.get(url)
inscricao_externo.caminho()
inscricao_externo.ct56_inscricao_externo(
    cpf     = '33740792027',
    nome    = 'Participante Externo Teste 5',
    email   = 'pexterno5@teste.com'
)
# -- Casos de teste: Campos obrigatórios no segundo formulário ---#
webdriver.get(url)
inscricao_externo.caminho()
inscricao_externo.ct57_inscricao_externo(
    cpf         = '48243520023',
    nome        = 'Participante Externo Teste 6',
    email       = 'pexterno6@teste.com',
    telefone    = '43663346975',
    celular     = '51405531814'
)
webdriver.close()
