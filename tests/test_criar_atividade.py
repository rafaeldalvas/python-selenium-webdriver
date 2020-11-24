from selenium import webdriver
from pages.page_criar_atividade import criarAtividade
from utils.login import LoginProfessor

webdriver = webdriver.Chrome()
webdriver.maximize_window()

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login()

criar_atividade = criarAtividade(webdriver)

# --------- Caso de teste: Criação de atividade padrão -------------#
def test_ct11():
    criar_atividade.caminho()
    criar_atividade.ct11_criar_atividade(
        tema        = 'ativividade teste ct11',
        descricao   = 'teste nova atividade',
        vagas       = '30',
        duracao     = '8',
        sala        = '101',
        data        = '12/12/2020',
        hora_inicio = '1000',
        hora_fim    = '1800'
    )
# ------------- Caso de teste: Cancelar transação ----------------#
def test_ct12():
    webdriver.get(url)
    criar_atividade.caminho()
    criar_atividade.ct12_criar_atividade()

# --------------- Caso de teste: Data incoerente -----------------#
def test_ct13():
    webdriver.get(url)
    criar_atividade.caminho()
    criar_atividade.ct13_criar_atividade(
        tema        = 'teste datas invalidas ct13',
        descricao   = 'teste data incoerente',
        vagas       = '30',
        duracao     = '8',
        sala        = '102',
        data        = '12/12/2017',
        hora_inicio = '1000',
        hora_fim    = '1800'
    )
# --------------- Caso de teste: Hora incoerente -----------------#
def test_ct14():
    webdriver.get(url)
    criar_atividade.caminho()
    criar_atividade.ct14_criar_atividade(
        tema        = 'teste datas invalidas ct14',
        descricao   = 'teste hora incoerente',
        vagas       = '30',
        duracao     = '1',
        sala        = '103',
        data        = '12/12/2020',
        hora_inicio = '0800',
        hora_fim    = '2200'
    )
# ------------- Caso de teste: Campos obrigatórios ---------------#
def test_ct15():
    webdriver.get(url)
    criar_atividade.caminho()
    criar_atividade.ct15_criar_atividade(
        tema        = 'teste campos obrigatorios ct15',
        descricao   = 'teste campos obrigatorios',
        vagas       = '30',
        duracao     = '8',
        local       = 'ICE',
        sala        = '103',
        data        = '12/12/2020',
        hora_inicio = '0800',
        hora_fim    = '2200'
    )

