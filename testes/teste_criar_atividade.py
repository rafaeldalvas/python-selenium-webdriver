from selenium import webdriver
from pages.page_criar_atividade import criarAtividade
from utils.login import LoginProfessor

webdriver = webdriver.Chrome()

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login(
    login = 'testes.professor',
    senha = '6kmfDK'
)

criar_atividade = criarAtividade(webdriver)

# --------- Caso de teste: Criação de atividade padrão -------------#
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
webdriver.get(url)
criar_atividade.caminho()
criar_atividade.ct12_criar_atividade()

# --------------- Caso de teste: Data incoerente -----------------#
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
webdriver.close()