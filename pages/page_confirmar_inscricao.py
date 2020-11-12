from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, \
    ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.config import PageElement
from time import sleep

class confirmarInscricao(PageElement):
    # CAMINHO
    calendario = (By.CSS_SELECTOR, "i.fa-calendar")
    admin = (By.CSS_SELECTOR, "a[href$='admEvento/inicial.zul?']")
    admin_inscricao = (By.CSS_SELECTOR, "a[href$='inicial.zul?pag=admInscricao']")

    combo_evento = (By.ID, 'zk-comp-116!btn')
    evento = (By.ID, 'zk-comp-162')
    combo_atividade = (By.ID, 'zk-comp-122!btn')
    atividade = (By.ID, 'zk-comp-169')
    todas_atividades = (By.ID, 'zk-comp-167')
    inscricoes_pendentes = (By.CSS_SELECTOR, 'span[id$="comp-127!box"] [class$="button-cm"]')
    todas_inscricoes = (By.CSS_SELECTOR, 'span[id$="comp-129!box"] [class$="button-cm"]')
    checkbox_presente = (By.ID, 'zk-comp-279')

    alert_tipo = (By.CSS_SELECTOR, 'div[class="z-separator-hor-bar"]')
    alert_texto = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[1]/tbody/tr/td[3]/div/span')
    btn_ok_alert = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[2]/tbody/tr/td/span/table/tbody/tr['
                              '2]/td[2]')

    def caminho(self):
        sleep(2)
        self.find_element(self.calendario).click()
        sleep(1)
        self.find_element(self.admin).click()
        sleep(1)

    def espera_mensagem(self):
        try:
            alert_tipo = WebDriverWait(self.webdriver, poll_frequency=0.2, timeout=5)
            alert_tipo.until(expected_conditions.visibility_of_element_located(self.alert_tipo))
            if alert_tipo is not None:
                return True
        except TimeoutException:
            return False

    # -------- Casos de teste: Confirmar inscrição padrão ------------#
    # def ct44_confirmar_inscricao(self):
    # ----------- Casos de teste: Ver todas inscrições ---------------#
    # def ct45_confirmar_inscricao(self):
    # -------- Casos de teste: Ver relatório de inscritos ------------#
    # def ct46_confirmar_inscricao(self):
    # ----- Casos de teste: Ver relatório de inscritos efetivados ----#
    # def ct47_confirmar_inscricao(self):
    # ------------ Casos de teste: Campo evento vazio ----------------#
    # def ct48_confirmar_inscricao(self):
    # ----------- Casos de teste: Campo atividade vazio --------------#
    # def ct49_confirmar_inscricao(self):