from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from utils.config import PageElement

class inscricao(PageElement):
    #CAMINHO
    calendario = (By.CSS_SELECTOR, "i.fa-calendar")
    menu_evento = (By.CSS_SELECTOR, "a[href$='inicial.zul?pag=listaEventos']")
    mais_info = (By.CLASS_NAME, "z-button")
    atividade = (By.CLASS_NAME, "z-button-cm")
    main = (By.CSS_SELECTOR, "a[href$='inicial.zul']")

    # CASOS DE TESTE
    inscrever = (By.ID, "zk-comp-158!box")


    # ALERT
    alert_tipo = (By.CSS_SELECTOR, 'div[class="z-separator-hor-bar"]')
    alert_texto = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[1]/tbody/tr/td[3]/div/span')
    btn_ok_alert = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[2]/tbody/tr/td/span/table/tbody/tr[''2]/td[2]')

    def espera_mensagem(self):
        try:
            alert_tipo = WebDriverWait(self.webdriver, poll_frequency=0.2, timeout=10)
            alert_tipo.until(expected_conditions.visibility_of_element_located(self.alert_tipo))
            if alert_tipo is not None:
                return True
        except TimeoutException:
            return False

    def clicarMain(self):
        sleep(1)
        self.find_element(self.main).click()

    def caminho(self):
        sleep(2)
        self.find_element(self.calendario).click()
        sleep(1)
        self.find_element(self.menu_evento).click()
        sleep(1)
        self.find_element(self.mais_info).click()
        sleep(1)
        self.find_element(self.atividade).click()





