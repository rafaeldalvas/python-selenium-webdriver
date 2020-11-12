from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, \
    ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.config import PageElement
from time import sleep

class confirmarPresenca(PageElement):
    # CAMINHO
    calendario = (By.CSS_SELECTOR, "i.fa-calendar")
    admin = (By.CSS_SELECTOR, "a[href$='admEvento/inicial.zul?']")

    # --------- Casos de teste: Confirmar presença padrão ------------#
    # ---------- Casos de teste: Atividade sem inscrições ------------#
    # ------------- Casos de teste: Atividade fechada ----------------#
    # ------------- Casos de teste: Fechar atividade -----------------#