import pytest
from selenium.common.exceptions import UnexpectedAlertPresentException, \
    ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.config import PageElement
from time import sleep


class CertificadoPalestranteExterno(PageElement):
    # CAMINHO
    certificado_palestrante = (By.CSS_SELECTOR, "a[href$='janelaCPF.zul?op=1']")
    cpf = (By.ID, 'zk-comp-46') # valido: 83239472600 / sem eventos: 33332506080
    confirmar = (By.ID, 'zk-comp-49')
    palestra = (By.CSS_SELECTOR, '#zk-comp-105\!cell > img')
    gerar = (By.CSS_SELECTOR, 'table[id$="comp-104!box"] [class$="button-cm"]')

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
                print("\n [!] CT_58 reportou erro: " + txt)
                self.find_element(self.btn_ok_alert).click()
                assert False
            else:
                if len(self.webdriver.window_handles) != 1:
                    print("\n CT_58 sem erros: certificado gerado com sucesso!")
                    self.webdriver.switch_to.window(original_window)
                    assert True
                else:
                    print("\n [!] CT_58 sem erros: o certificado não foi gerado")
                    assert False

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_58 reportou erro: " + str(e))
            assert False

        except ElementClickInterceptedException:
            print("\n [!] CT_58 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()
            assert False

    # --------- Casos de teste: Palestrante sem eventos --------------#
    def test_ct59_certificado_palestrante_externo(self, cpf):
        try:
            self.find_element(self.cpf).send_keys(cpf)
            self.find_element(self.confirmar).click()
            sleep(1)
            msg = self.espera_mensagem()
            original_window = self.webdriver.current_window_handle
            if msg is True:
                txt = self.find_element(self.alert_texto).text
                print("\n CT_59 reportou erro: " + txt)
                self.find_element(self.btn_ok_alert).click()
                assert True
            else:
                if len(self.webdriver.window_handles) != 1:
                    print("\n [!] CT_59 sem erros: certificado gerado com sucesso!")
                    self.webdriver.switch_to.window(original_window)
                    assert False
                else:
                    print("\n CT_59 sem erros: o certificado não foi gerado")
                    assert True

        except UnexpectedAlertPresentException as e:
            print("\n CT_59 reportou erro: " + str(e))
            assert True

        except ElementClickInterceptedException:
            print("\n CT_59 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()
            assert True

    # --------------- Casos de teste: CPF inválido -------------------#
    def test_ct60_certificado_palestrante_externo(self, cpf):
        try:
            self.find_element(self.cpf).send_keys(cpf)
            self.find_element(self.confirmar).click()
            sleep(1)
            msg = self.espera_mensagem()
            original_window = self.webdriver.current_window_handle
            if msg is True:
                txt = self.find_element(self.alert_texto).text
                print("\n CT_60 reportou erro: " + txt)
                self.find_element(self.btn_ok_alert).click()
                assert True
            else:
                if len(self.webdriver.window_handles) != 1:
                    print("\n [!] CT_60 sem erros: certificado gerado com sucesso!")
                    self.webdriver.switch_to.window(original_window)
                    assert False
                else:
                    print("\n CT_60 sem erros: o certificado não foi gerado")
                    assert True

        except UnexpectedAlertPresentException as e:
            print("\n CT_60 reportou erro: " + str(e))
            assert True

        except ElementClickInterceptedException:
            print("\n CT_60 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()
            assert True

    # ------------ Casos de teste: CPF não cadastrado ----------------#
    def test_ct61_certificado_palestrante_externo(self, cpf):
        try:
            self.find_element(self.cpf).send_keys(cpf)
            self.find_element(self.confirmar).click()
            sleep(1)
            msg = self.espera_mensagem()
            original_window = self.webdriver.current_window_handle
            if msg is True:
                txt = self.find_element(self.alert_texto).text
                print("\n CT_61 reportou erro: " + txt)
                self.find_element(self.btn_ok_alert).click()
                assert True
            else:
                if len(self.webdriver.window_handles) != 1:
                    print("\n [!] CT_61 sem erros: certificado gerado com sucesso!")
                    self.webdriver.switch_to.window(original_window)
                    assert False
                else:
                    print("\n CT_61 sem erros: o certificado não foi gerado")
                    assert True

        except UnexpectedAlertPresentException as e:
            print("\n CT_61 reportou erro: " + str(e))
            assert True

        except ElementClickInterceptedException:
            print("\n CT_61 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()
            assert True