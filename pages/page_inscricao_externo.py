from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, \
    ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.config import PageElement
from time import sleep

class inscricaoExterno(PageElement):
    #CAMINHO
    inscricao_eventos = (By.CSS_SELECTOR, "a[href$='listaEventos.zul']")
    evento = (By.CSS_SELECTOR, 'table[id$="zk-comp-99!box"] [class$="button-cm"]')

    # ---------- Casos de teste: Evento não selecionado --------------#
    #def ct50_inscricao_externo(self):
    # - Casos de teste: Confirmar inscrição de usuário externo padrão-#
    #def ct51_inscricao_externo(self):
    # ---------- Casos de teste: Prazo para inscrição vencido --------#
    #def ct52_inscricao_externo(self):
    # --------------- Casos de teste: CPF inválido -------------------#
    #def ct53_inscricao_externo(self):
    # -------------- Casos de teste: Email inválido ------------------#
    #def ct54_inscricao_externo(self):
    # - Casos de teste: Campos obrigatórios no primeiro formulário ---#
    #def ct55_inscricao_externo(self):
    # -- Casos de teste: Campos obrigatórios no segundo formulário ---#