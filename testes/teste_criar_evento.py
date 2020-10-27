from selenium import webdriver
from pages.page_criar_evento import criarEvento
from utils.login import LoginProfessor

webdriver = webdriver.Chrome(r'd:\Downloads\chromedriver_win32\chromedriver.exe')

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login(
    login = 'testes.professor',
    senha = '6kmfDK'
)

criar_evento = criarEvento(webdriver)

# --------- Caso de teste: Criação de evento padrão -------------#
criar_evento.caminho()
criar_evento.ct01_criar_evento(
    nome                = 'Evento teste ct1',
    descricao           = 'testando evento',
    site                = 'teste.com.br',
    email_responsavel   = 'teste@teste.com',
    inicio_evento       = '22/12/2020',
    fim_evento          = '01/01/2021',
    inicio_inscricao    = '20/11/2020',
    fim_inscricao       = '20/12/2020',
    funcao1             = 'Professor',
    funcao2             = 'Gerente',
    funcao3             = 'Diretor'
)
# ------------ Caso de teste: Trocar responsável ----------------#
webdriver.get(url)
criar_evento.caminho()
criar_evento.ct02_criar_evento(
    nome               = 'Evento teste ct2',
    descricao          = 'testando responsavel',
    site               = 'teste2.com',
    email_responsavel  = 'teste2@teste.com',
    inicio_evento      = '03/01/2021',
    fim_evento         = '10/01/2021',
    inicio_inscricao   = '21/12/2020',
    fim_inscricao      = '02/01/2021',
    funcao1            = 'Professor',
    funcao2            = 'Gerente',
    funcao3            = 'Diretor',
    nome_responsavel   = 'Raquel Alves da Silva'
)
# ------------- Caso de teste: Cancelar transação ---------------#
webdriver.get(url)
criar_evento.caminho()
criar_evento.ct03_criar_evento(
    nome        ='Evento teste ct3',
    descricao   ='testando cancelar criacao'
)
# ----- Caso de teste: Campos obrigatórios não preenchidos -------#
webdriver.get(url)
criar_evento.caminho()
criar_evento.ct04_criar_evento(
    nome                = 'Evento teste ct1',
    descricao           = 'testando evento',
    inicio_evento       = '22/12/2020',
    fim_evento          = '01/01/2021',
    inicio_inscricao    = '20/11/2020',
    fim_inscricao       = '20/12/2020',
)
# ---------------- Caso de teste: Data inválida -----------------#
webdriver.get(url)
criar_evento.caminho()
criar_evento.ct05_criar_evento(
    nome               = 'Evento teste ct5',
    descricao          = 'testando datas invalidas',
    #Datas inferiores a data atual do sistema:
    inicio_evento      = '03/12/2015',
    fim_evento         = '10/01/2016',
    inicio_inscricao   = '02/11/2015',
    fim_inscricao      = '02/12/2015',
)


