from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, \
    ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.config import PageElement
from time import sleep


class certificadoPalestranteExterno(PageElement):
    # CAMINHO
    certificado_palestrante = (By.CSS_SELECTOR, "a[href$='janelaCPF.zul?op=1']")
    cpf = (By.ID, 'zk-comp-46') # valido: 83239472600 / invalido: 33332506080
    confirmar = (By.ID, 'zk-comp-49')

    alert_tipo = (By.CSS_SELECTOR, 'div[class="z-separator-hor-bar"]')
    alert_texto = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[1]/tbody/tr/td[3]/div/span')
    btn_ok_alert = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[2]/tbody/tr/td/span/table/tbody/tr['
                              '2]/td[2]')

    def caminho(self):
        sleep(1)
        self.find_element(self.certificado_palestrante).click()
        sleep(1)

    def espera_mensagem(self):
        try:
            alert_tipo = WebDriverWait(self.webdriver, poll_frequency=0.2, timeout=5)
            alert_tipo.until(expected_conditions.visibility_of_element_located(self.alert_tipo))
            if alert_tipo is not None:
                return True
        except TimeoutException:
            return False


    # --------- Casos de teste: Geração de certificado padrão --------#
    def ct58_certificado_palestrante_externo(self, cpf):
        self.find_element(self.cpf).send_keys(cpf)
        self.find_element(self.confirmar).click()

    # --------- Casos de teste: Palestrante sem eventos --------------#
    # def ct59_certificado_palestrante_externo(self):
    # --------------- Casos de teste: CPF inválido -------------------#
    # def ct60_certificado_palestrante_externo(self):
    # ------------ Casos de teste: CPF não cadastrado ----------------#
    # def ct61_certificado_palestrante_externo(self):