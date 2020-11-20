from selenium import webdriver
from pages.page_cadastrar_palestrante import cadastrarPalestrante
from utils.login import LoginProfessor

webdriver = webdriver.Chrome()

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login()

cadastrar_palestrante = cadastrarPalestrante(webdriver)

# --------- Caso de teste: Cadastro de palestrante padrão -------------#
cadastrar_palestrante.caminho()
cadastrar_palestrante.ct22_cadastrar_palestrante(
    nome                = 'Gabriel',
    email               = 'gabriel@email.com',
    cpf                 = '329.918.840-29',
    rg                  = '46.678.999-3',
    pis                 = '132.46619.92-0',
    resumo_curriculo    = 'Estagiário e professor',
    link_lates          = 'lattes.com.br',
    telefone            = '32999999999',
    endereco            = 'Rua da Praça, 87',
    agencia             = '5522',
    conta               = '55897',
    valor_participacao  = '2000',
    valor_transporte    = '100',
    valor_alimentacao   = '500',
    valor_hotel         = '800',
)
# --------- Caso de teste: Caracteres inválidos -------------#
webdriver.get(url)
cadastrar_palestrante.caminho()
cadastrar_palestrante.ct23_cadastrar_palestrante(
    nome                = 'Julia',
    email               = 'julia@email.com',
    cpf                 = 'testecpf',
    rg                  = 'testerg',
    pis                 = 'testepis',
    telefone            = 'testetelefone',
    agencia             = 'testeagencia',
    conta               = 'testeconta',
    valor_participacao  = 'testepartici',
    valor_transporte    = 'testetransporte',
    valor_alimentacao   = 'testealimentacao',
    valor_hotel         = 'testehotel',
)
# --------- Caso de teste: Campo obrigatório vazio -------------#
webdriver.get(url)
cadastrar_palestrante.caminho()
cadastrar_palestrante.ct24_cadastrar_palestrante(
    nome                = 'Rafaela',
    email               = 'rafaela@email.com',
    cpf                 = '271.471.130-80'
)
# --------- Caso de teste: Caracteres inválidos -------------#
webdriver.get(url)
cadastrar_palestrante.caminho()
cadastrar_palestrante.ct25_cadastrar_palestrante(
    nome                = 'Gabriel',
    email               = 'gabriel@email.com',
    cpf                 = '999.999.999-99'
)
webdriver.close()