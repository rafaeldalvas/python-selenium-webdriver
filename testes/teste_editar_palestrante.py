from time import sleep
from selenium import webdriver
from pages.page_editar_palestrante import editarPalestrante
from utils.login import LoginProfessor

webdriver = webdriver.Chrome(r'd:\Downloads\chromedriver_win32\chromedriver.exe')

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login()

editar_palestrante = editarPalestrante(webdriver)

# ------------ Caso de teste: Edição de palestrante padrão ---------------#
webdriver.get(url)
editar_palestrante.ct27_editar_palestrante(
    nome                = 'Samuel',
    email               = 'samuel@email.com',
    cpf                 = '810.109.190-40',
    rg                  = '19.394.008-5',
    pis                 = '013.31263.70-8',
    resumo_curriculo    = 'Professor mestre',
    link_lates          = 'linkedin.com.br',
    telefone            = '3288888888',
    endereco            = 'Rua da Maçã, 150',
    agencia             = '7777',
    conta               = '12345',
    valor_participacao  = '4500',
    valor_transporte    = '300',
    valor_alimentacao   = '900',
    valor_hotel         = '1400',
)

# ------------ Caso de teste: Cancelar edição ---------------#
sleep(1)
webdriver.get(url)
sleep(1)
webdriver.get(url)
editar_palestrante.ct_28_editar_palestrante()

# ------------ Caso de teste: Palestrante não selecionado ---------------#
sleep(1)
webdriver.get(url)
sleep(1)
editar_palestrante.caminho(True)
editar_palestrante.ct_29_editar_palestrante()

# ------------ Caso de teste: Caracteres inválidos ---------------#
sleep(1)
webdriver.get(url)
sleep(1)
webdriver.get(url)
editar_palestrante.ct_30_editar_palestrante(
    cpf                 = 'CPF',
    rg                  = 'RG',
    pis                 = 'PIS',
    telefone            = 'TELEFONE',
    agencia             = 'AGENCIA',
    conta               = 'CONTA'
)

# ------------ Caso de teste: Campos obrigatórios em branco ---------------#
sleep(1)
webdriver.get(url)
sleep(1)
webdriver.get(url)
editar_palestrante.ct_31_editar_palestrante(
    nome                = 'Arthur',
    email               = 'Arthur@email.com',
)

# ------------ Caso de teste: CPF inválido ---------------#
sleep(1)
webdriver.get(url)
sleep(1)
webdriver.get(url)
editar_palestrante.ct_32_editar_palestrante(
    cpf = '999.999.999-99'
)






