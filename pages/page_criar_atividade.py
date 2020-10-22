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

    # FORMULARIO BASICO
    combo_tipo = (By.ID, 'zk-comp-155!btn')
    tipo = (By.CSS_SELECTOR, 'tr[id$="comp-209"] [class="z-combo-item-text"]')
    tema = (By.ID, 'zk-comp-163')
    descricao = (By.ID, 'zk-comp-166')
    vagas = (By.ID, 'zk-comp-169')
    duracao = (By.ID, 'zk-comp-173')
    combo_palestrante = (By.ID, 'zk-comp-192!btn')
    palestrante = (By.CSS_SELECTOR, 'tr[id$="comp-228"] [class="z-combo-item-text"]') #Alberto Duque Portugal

    #DATAS DA ATIVIDADE
    botao_definir = (By.CSS_SELECTOR, 'table[id$="comp-159!box"] [class$="button-cm"]')
    sala = (By.ID, 'zk-comp-1110')
    Data = (By.ID, 'zk-comp-1113!real')
    hora_inicio = (By.ID, 'zk-comp-1116')
    hora_fim = (By.ID, 'zk-comp-1119')
    botao_adicionar = (By.CSS_SELECTOR, 'table[id$="comp-159!box"] [class$="button-cm"]')
    botao_salvar = (By.CSS_SELECTOR, 'table[id$="comp-159!box"] [class$="button-cm"]')

    def caminho(self):
        sleep(1)
        self.find_element(self.calendario).click()
        sleep(1)
        self.find_element(self.admin).click()
        sleep(1)
        self.find_element(self.cadastro_atividade).click()
        sleep(1)
        self.find_element(self.radio_atividade).click()
        sleep(1)
        self.find_element(self.combo_atividade).click()
        sleep(1)
        self.find_element(self.evento).click()
        sleep(2)
        self.find_element(self.btn_novo).click()
