from selenium.common.exceptions import UnexpectedAlertPresentException, \
    ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.config import PageElement
from time import sleep

class confirmarPresenca(PageElement):
    # CAMINHO
    calendario = (By.CSS_SELECTOR, "i.fa-calendar")
    admin = (By.CSS_SELECTOR, "a[href$='admEvento/inicial.zul?']")
    controle_presenca = (By.CSS_SELECTOR, "a[href$='inicial.zul?pag=admPresencaEventos']")

    evento = (By.CSS_SELECTOR, 'table[id$="comp-124!box"] [class$="button-cm"]')
    proxima_pagina = (By.CLASS_NAME, 'z-paging-next')
    atividade = (By.ID, 'zk-comp-12957!box')
    atividade_ct34 = (By.ID, 'zk-comp-12952!box')
    fechar_atividade = (By.CSS_SELECTOR, 'table[id$="comp-135!box"] [class$="button-cm"]')
    checkbox_falta = (By.ID, 'zk-comp-148!real')
    checkbox_falta_2 = (By.ID, 'zk-comp-142!real')
    salvar = (By.CSS_SELECTOR, 'table[id$="comp-136!box"] [class$="button-cm"]')

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
        self.find_element(self.controle_presenca).click()
        sleep(1)

    def espera_mensagem(self):
        try:
            alert_tipo = WebDriverWait(self.webdriver, poll_frequency=0.2, timeout=5)
            alert_tipo.until(expected_conditions.visibility_of_element_located(self.alert_tipo))
            if alert_tipo is not None:
                return True
        except TimeoutException:
            return False

    # --------- Casos de teste: Confirmar presença padrão ------------#
    def ct33_confirmar_presenca(self):
        txt = "As mudanças foram salvas com sucesso!"
        try:
            self.find_element(self.evento).click()
            sleep(1)
            self.find_element(self.proxima_pagina).click()
            sleep(1)
            self.find_element(self.atividade).click()
            sleep(1)
            self.find_element(self.checkbox_falta).click()
            self.find_element(self.salvar).click()
            sleep(1)
            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text != txt:
                    print("\n [!] CT_33 reportou erro: " + self.find_element(self.alert_texto).text)
                else:
                    print("\n CT_33 sem erros: " + self.find_element(self.alert_texto).text)
                self.find_element(self.btn_ok_alert).click()
            else:
                print("\n CT_33 sem erros: sistema não reportou erros!")

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_33 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n [!] CT_33 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # ---------- Casos de teste: Atividade sem inscrições ------------#
    def ct34_confirmar_presenca(self):
        txt = "Não existem inscrições para esta atividade."
        try:
            self.find_element(self.evento).click()
            sleep(1)
            self.find_element(self.atividade_ct34).click()
            sleep(1)
            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text != txt:
                    print("\n [!] CT_34 reportou erro: " + self.find_element(self.alert_texto).text)
                else:
                    print("\n CT_34 sem erros: " + self.find_element(self.alert_texto).text)
                self.find_element(self.btn_ok_alert).click()
            else:
                print("\n CT_34 sem erros: sistema não reportou erros!")

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_34 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n [!] CT_34 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # ------------- Casos de teste: Atividade fechada ----------------#
    def ct35_confirmar_presenca(self):
        txt = "Atividade fechada com sucesso!"
        try:
            self.find_element(self.evento).click()
            sleep(1)
            self.find_element(self.proxima_pagina).click()
            sleep(1)
            self.find_element(self.atividade).click()
            sleep(1)
            self.find_element(self.fechar_atividade).click()
            sleep(1)
            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text != txt:
                    print("\n [!] CT_35 reportou erro: " + self.find_element(self.alert_texto).text)
                else:
                    print("\n CT_35 sem erros: " + self.find_element(self.alert_texto).text)
                self.find_element(self.btn_ok_alert).click()
            else:
                print("\n CT_35 sem erros: sistema não reportou erros!")

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_35 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n [!] CT_35 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # ------------- Casos de teste: Fechar atividade -----------------#
    def ct36_confirmar_presenca(self):
        txt = "As mudanças foram salvas com sucesso!"
        try:
            self.find_element(self.evento).click()
            sleep(1)
            self.find_element(self.proxima_pagina).click()
            sleep(1)
            self.find_element(self.atividade).click()
            sleep(1)
            self.find_element(self.checkbox_falta_2).click()
            self.find_element(self.salvar).click()
            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text != txt:
                    print("\n CT_36 reportou erro: " + self.find_element(self.alert_texto).text)
                else:
                    print("\n [!] CT_36 sem erros: " + self.find_element(self.alert_texto).text)
                self.find_element(self.btn_ok_alert).click()
            else:
                print("\n [!] CT_36 sem erros: sistema não reportou erros!")

        except UnexpectedAlertPresentException as e:
            print("\n CT_36 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n CT_36 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()