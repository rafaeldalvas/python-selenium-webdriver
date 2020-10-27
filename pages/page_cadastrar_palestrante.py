from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException
from selenium.webdriver.common.by import By
from utils.config import PageElement
from time import sleep

class cadastrarPalestrante(PageElement):
    #CAMINHO
    sleep(2)
    calendario = (By.CSS_SELECTOR, "i.fa-calendar")
    admin = (By.CSS_SELECTOR, "a[href$='admEvento/inicial.zul?']")
    main = (By.CSS_SELECTOR, "a[href$='inicial.zul']")
    cadastro_evento = (By.ID, 'zk-comp-112')
    radio_evento = (By.ID, 'zk-comp-118!real')
    btn_novo = (By.CSS_SELECTOR, '.z-button-cm')

    #FORMULÁRIO PADRAO
    nome = (By.ID, 'zk-comp-145')
    email = (By.ID, 'zk-comp-148')
    cpf = (By.ID, 'zk-comp-151')
    rg = (By.ID, 'zk-comp-154')
    pis = (By.ID, 'zk-comp-157')
    resumo_curriculo = (By.ID, 'zk-comp-160')
    link_lates = (By.ID, 'zk-comp-163')
    telefone = (By.ID, 'zk-comp-166')
    endereco = (By.ID, 'zk-comp-169')
    agencia = (By.ID, 'zk-comp-172')
    conta = (By.ID, 'zk-comp-175')
    valor_participacao = (By.ID, 'zk-comp-178')
    valor_transporte = (By.ID, 'zk-comp-181')
    pagou_transporte = (By.ID, 'zk-comp-185!real') # SELECIONANDO SIM
    valor_alimentacao = (By.ID, 'zk-comp-189')
    pagou_alimentacao = (By.ID, 'zk-comp-193!real') # SELECIONANDO SIM
    valor_hotel = (By.ID, 'zk-comp-197')
    pagou_hotel = (By.ID, 'zk-comp-201!real') # SELECIONANDO SIM

    # CONCLUIR
    salvar = (By.CSS_SELECTOR, 'table[id$="zk-comp-205!box"] [class$="button-cm"]')



