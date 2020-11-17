from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from utils.config import PageElement

class certificadoParticipante(PageElement):
    #CAMINHO
    calendario = (By.CSS_SELECTOR, "i.fa-calendar")
    emissao = (By.CSS_SELECTOR, "a[href$='inicial.zul?pag=relatorioEventosParticipados']")
    main = (By.CSS_SELECTOR, "a[href$='inicial.zul']")
    dropdownLogout = (By.ID, "kMenu")
    logout = (By.ID, "zk-comp-102")


    # CERTIFICADO
    dropdownCertificado = (By.ID, "zk-comp-148!cell")
    gerar = (By.CLASS_NAME, "z-button-cm")

    # ALERT
    alert_tipo = (By.CSS_SELECTOR, 'div[class="z-separator-hor-bar"]')
    alert_texto = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[1]/tbody/tr/td[3]/div/span')
    btn_ok_alert = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[2]/tbody/tr/td/span/table/tbody/tr[''2]/td[2]')



    def logout(self):
        self.find_element(self.dropdownLogout).click()
        sleep(1)
        self.find_element(self.logout).click()

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
        sleep(1)
        self.find_element(self.calendario).click()
        sleep(1)
        self.find_element(self.emissao).click()

# ------------ Geração de certificado padrão  ---------------#
    def ct50_certificado_participante(self):
        try:
            sleep(1)
            self.find_element(self.dropdownCertificado).click()
            self.find_element(self.gerar).click()
            msg = self.espera_mensagem()
            original_window = self.webdriver.current_window_handle
            if msg is True:
                txt = self.find_element(self.alert_texto).text
                print("\n [!] CT_50 reportou erro: " + txt)
                self.find_element(self.btn_ok_alert).click()
            else:
                if len(self.webdriver.current_window_handles) != 1:
                    print("\n CT_50 sem erros: certificado gerado com sucesso!")
                    self.webdriver.switch_to.window(original_window)
                else:
                    print("\n [!] CT_50 reportou erro: o certificado não foi gerado")
        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_50 reportou erro: " + str(e))










