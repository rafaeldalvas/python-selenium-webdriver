from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.login import LoginProfessor

class criarEvento():

    webdriver = webdriver.Chrome(r'd:\Downloads\chromedriver_win32\chromedriver.exe')

    url = "https://integra-h.nrc.ice.ufjf.br/"
    webdriver.get(url)

    login_professor = LoginProfessor(webdriver)

    login_professor.realiza_login(
        login='testes.professor',
        senha='6kmfDK'
    )

    # CAMINHO
    admin = (By.XPATH, "a[contains(@href,'/integra/restrito/admEvento/inicial.zul?')]")
    cadastro_evento = (By.ID, 'zk-comp-112')
    radio_evento = (By.ID, 'zk-comp-114!real')
    btn_novo = (By.XPATH, "//td[text()='Novo']")


    # FORMULARIO PADRAO
    nome = (By.ID, 'zk-comp-958')
    descricao = (By.ID, 'zk-comp-961')
    site = (By.ID, 'zk-comp-964')
    email_responsavel = (By.ID, 'zk-comp-972')
    inicio_evento = (By.ID, 'zk-comp-983!real')
    fim_evento = (By.ID, 'zk-comp-986!real')
    inicio_inscricao = (By.ID, 'zk-comp-989!real')
    fim_inscricao = (By.ID, 'zk-comp-992!real')
    tipo_evento = (By.ID, 'zk-comp-995!real')
    inscricao_externa = (By.ID, 'zk-comp-999!real')
    evento_pago = (By.ID, 'zk-comp-1005!real')
    btn_enviar = (By.ID, 'id')

    # FORMUMARIO REPONSAVEL

    btn_buscar = (By.XPATH, "//td[text()='Buscar']")
    nome_responsavel = (By.ID, '')
    btn_pesquisar_responsavel = (By.XPATH, "//td[text()='Editar']")
    checkbox_responsavel = (By.ID, '')
    seleciona_nome = (By.ID, '')
    btn_confirma_responsavel = (By.XPATH, "//td[text()='Novo']")



    # FORMULARIO CERTIFICADO




