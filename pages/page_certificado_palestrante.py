from selenium.common.exceptions import UnexpectedAlertPresentException,\
    ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
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
    evento = (By.ID, 'zk-comp-174') # TESTE DALVAS E JP
    combo_atividade = (By.ID, 'zk-comp-119!btn')
    atividade = (By.ID, 'zk-comp-191') #5757
    tabela_atividades = (By.XPATH, '/html/body/div[4]/table/tbody/tr[1]/td[2]') # Todas as atividades
    exibir = (By.CSS_SELECTOR, 'table[id$="comp-121!box"] [class$="button-cm"]')
    gerar = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div['
                              '1]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/table/tbody[2]/tr/td['
                              '5]/div/span/table/tbody/tr[2]/td[2]')

    alert_tipo = (By.CSS_SELECTOR, 'div[class="z-separator-hor-bar"]')
    alert_texto = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[1]/tbody/tr/td[3]/div/span')
    btn_ok_alert = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[2]/tbody/tr/td/span/table/tbody/tr['
                              '2]/td[2]')

    def caminho(self):
        sleep(1)
        self.find_element(self.calendario).click()
        sleep(1)
        self.find_element(self.admin).click()
        sleep(1)
        self.find_element(self.geracao_certificado).click()
        sleep(1)

    def espera_mensagem(self):
        try:
            alert_tipo = WebDriverWait(self.webdriver, poll_frequency=0.2, timeout=5)
            alert_tipo.until(expected_conditions.visibility_of_element_located(self.alert_tipo))
            if alert_tipo is not None:
                return True
        except TimeoutException:
            return False

    # --- Casos de teste: Gerar Certificado Para Palestrando padrão --#
    def ct37_certificado_palestrante(self):
        try:
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
            sleep(1)
            msg = self.espera_mensagem()
            original_window = self.webdriver.current_window_handle
            if msg is True:
                txt = self.find_element(self.alert_texto).text
                print("\n [!] CT_37 reportou erro: " + txt)
                self.find_element(self.btn_ok_alert).click()
                assert False
            else:
                if len(self.webdriver.window_handles) != 1:
                    print("\n CT_37 sem erros: certificado gerado com sucesso!")
                    self.webdriver.switch_to.window(original_window)
                    assert True
                else:
                    print("\n [!] CT_37 sem erros: o certificado não foi gerado")
                    assert False

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_37 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n [!] CT_37 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # ---------- Casos de teste: Evento não selecionado --------------#
    def ct38_certificado_palestrante(self):
        try:
            self.find_element(self.exibir).click()
            sleep(1)
            msg = self.espera_mensagem()
            if msg is True:
                print("\n CT_38 reportou erro: " + self.find_element(self.alert_texto).text)
                self.find_element(self.btn_ok_alert).click()
                assert True
            else:
                print("\n [!] CT_38 sem erros: sistema não reportou erros!")
                assert False

        except UnexpectedAlertPresentException as e:
            print("\n CT_38 reportou erro: " + str(e))
            assert True

        except ElementClickInterceptedException:
            print("\n CT_38 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()
            assert True

    # --------- Casos de teste: Atividade não especificada -----------#
    def ct39_certificado_palestrante(self):
        try:
            self.find_element(self.combo_evento).click()
            sleep(1)
            self.find_element(self.evento).click()
            self.find_element(self.exibir).click()
            sleep(1)
            msg = self.espera_mensagem()
            if msg is True:
                print("\n [!] CT_39 reportou erro: " + self.find_element(self.alert_texto).text)
                self.find_element(self.btn_ok_alert).click()
                assert False
            else:
                if expected_conditions.visibility_of_element_located(self.tabela_atividades):
                    print("\n CT_39 sem erros: sistema exibiu todas as atividades!")
                    assert True
                else:
                    print("\n CT_39 sem erros: sistema não exibiu todas as atividades!")
                    assert True

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_39 reportou erro: " + str(e))
            assert False

        except ElementClickInterceptedException:
            print("\n [!] CT_39 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()
            assert False