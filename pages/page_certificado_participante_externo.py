from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, \
    ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.config import PageElement
from time import sleep


class certificadoParticipanteExterno(PageElement):
    # CAMINHO
    certificado_participante = (By.CSS_SELECTOR, "a[href$='janelaCPF.zul?op=2']")
    cpf = (By.ID, 'zk-comp-46')
    confirmar = (By.ID, 'zk-comp-49')
    palestra = (By.CSS_SELECTOR, '#zk-comp-104\!cell > img')
    gerar = (By.CSS_SELECTOR, 'table[id$="comp-108!box"] [class$="button-cm"]')

    alert_tipo = (By.CSS_SELECTOR, 'div[class="z-separator-hor-bar"]')
    alert_texto = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[1]/tbody/tr/td[3]/div/span')
    btn_ok_alert = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[2]/tbody/tr/td/span/table/tbody/tr['
                              '2]/td[2]')

    def caminho(self):
        sleep(1)
        self.find_element(self.certificado_participante).click()
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
    def ct62_certificado_participante_externo(self, cpf):
        try:
            self.find_element(self.cpf).send_keys(cpf)
            self.find_element(self.confirmar).click()
            sleep(1)
            self.find_element(self.palestra).click()
            sleep(1)
            self.find_element(self.gerar).click()
            sleep(1)
            msg = self.espera_mensagem()
            original_window = self.webdriver.current_window_handle
            if msg is True:
                txt = self.find_element(self.alert_texto).text
                print("\n [!] CT_62 reportou erro: " + txt)
                self.find_element(self.btn_ok_alert).click()
            else:
                if len(self.webdriver.window_handles) != 1:
                    print("\n CT_62 sem erros: certificado gerado com sucesso!")
                    self.webdriver.switch_to.window(original_window)
                else:
                    print("\n [!] CT_62 sem erros: o certificado não foi gerado")

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_62 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n [!] CT_62 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # --------------- Casos de teste: CPF inválido -------------------#
    def ct63_certificado_participante_externo(self, cpf):
        try:
            self.find_element(self.cpf).send_keys(cpf)
            self.find_element(self.confirmar).click()
            sleep(1)
            msg = self.espera_mensagem()
            original_window = self.webdriver.current_window_handle
            if msg is True:
                txt = self.find_element(self.alert_texto).text
                print("\n CT_63 reportou erro: " + txt)
                self.find_element(self.btn_ok_alert).click()
            else:
                if len(self.webdriver.window_handles) != 1:
                    print("\n [!] CT_63 sem erros: certificado gerado com sucesso!")
                    self.webdriver.switch_to.window(original_window)
                else:
                    print("\n CT_63 sem erros: o certificado não foi gerado")

        except UnexpectedAlertPresentException as e:
            print("\n CT_63 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n CT_63 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # ------------ Casos de teste: CPF não cadastrado ----------------#
    def ct64_certificado_participante_externo(self, cpf):
        try:
            self.find_element(self.cpf).send_keys(cpf)
            self.find_element(self.confirmar).click()
            sleep(1)
            msg = self.espera_mensagem()
            original_window = self.webdriver.current_window_handle
            if msg is True:
                txt = self.find_element(self.alert_texto).text
                print("\n CT_64 reportou erro: " + txt)
                self.find_element(self.btn_ok_alert).click()
            else:
                if len(self.webdriver.window_handles) != 1:
                    print("\n [!] CT_64 sem erros: certificado gerado com sucesso!")
                    self.webdriver.switch_to.window(original_window)
                else:
                    print("\n CT_64 sem erros: o certificado não foi gerado")

        except UnexpectedAlertPresentException as e:
            print("\n CT_64 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n CT_64 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()