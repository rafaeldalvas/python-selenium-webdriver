from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, \
    ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.config import PageElement
from time import sleep

class certificadoPalestrante(PageElement):
    # CAMINHO
    calendario = (By.CSS_SELECTOR, "i.fa-calendar")
    admin = (By.CSS_SELECTOR, "a[href$='admEvento/inicial.zul?']")
    geracao_certificado = (By.ID, 'zk-comp-124')
    #CERTIFICADO
    combo_evento = (By.ID, 'zk-comp-114!btn')
    evento = (By.ID, 'zk-comp-163') # TESTE DALVAS E JP
    combo_atividade = (By.ID, 'zk-comp-119!btn')
    atividade = (By.ID, 'zk-comp-176') #5757
    todas_atividades = (By.ID, 'zk-comp-175') # Todas as atividades
    exibir = (By.CSS_SELECTOR, 'table[id$="comp-121!box"] [class$="button-cm"]')
    gerar = (By.CSS_SELECTOR, 'table[id$="comp-196!box"] [class$="button-cm"]')

    def caminho(self):
        sleep(2)
        self.find_element(self.calendario).click()
        sleep(1)
        self.find_element(self.admin).click()
        sleep(1)
        self.find_element(self.geracao_certificado).click()
        sleep(1)

    # --- Casos de teste: Gerar Certificado Para Palestrando padrão --#
    def ct37_certificado_palestrante(self):
        self.find_element(self.combo_evento).click()
        sleep(1)
        self.find_element(self.evento).click()
        self.find_element(self.combo_atividade).click()
        sleep(1)
        self.find_element(self.atividade).click()
        sleep(1)
        self.find_element(self.exibir).click()
        sleep(1)
        self.find_element(self.gerar).click()

    # ---------- Casos de teste: Evento não selecionado --------------#
    # def ct38_certificado_palestrante(self):
    # --------- Casos de teste: Atividade não especificada -----------#
    # def ct39_certificado_palestrante(self):