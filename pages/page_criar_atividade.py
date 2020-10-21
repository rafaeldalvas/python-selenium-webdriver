from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.config import PageElement
from time import sleep

class criarAtividade(PageElement):
    # CAMINHO
    calendario = (By.CSS_SELECTOR, "i.fa-calendar")
    admin = (By.CSS_SELECTOR, "a[href$='admEvento/inicial.zul?']")
    cadastro_atividade = (By.ID, 'zk-comp-112')
    radio_atividade = (By.ID, 'zk-comp-116!real')
    combo_atividade = (By.ID, "zk-comp-125!btn")  # COMBO BOX
    evento = (By.CSS_SELECTOR, 'tr[id$="comp-930"] [class="z-combo-item-text"]')  # EVENTO TESTES DALVAS E JP
    btn_novo = (By.CSS_SELECTOR, '.z-button-cm')

    # FORMULARIO PADRAO