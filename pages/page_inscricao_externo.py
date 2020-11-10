from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, \
    ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.config import PageElement
from time import sleep


class inscricaoExterno(PageElement):
    # CAMINHO
    inscricao_eventos = (By.CSS_SELECTOR, "a[href$='listaEventos.zul']")
    evento = (By.CSS_SELECTOR, 'table[id$="comp-99!box"] [class$="button-cm"]')

    proxima_pagina = (By.CLASS_NAME, 'z-paging-next')
    atividade = (By.XPATH, '/html/body/div/div/div/div/div/div/div/div['
                           '2]/div/section/div/div/section/div/div/section/div/div[1]/div[2]/div[1]/div/div/div/div['
                           '3]/div[2]/table/tbody[2]/tr[5]/td[3]/div/table/tbody/tr/td/span/table/tbody/tr[2]/td[2]')
    # FORMULARIO-1
    cpf = (By.ID, 'zk-comp-45')
    nome = (By.ID, 'zk-comp-48')
    email = (By.ID, 'zk-comp-51')
    confirmar = (By.ID, 'zk-comp-54')
    # FORMULARIO-2
    telefone = (By.ID, 'zk-comp-97')
    celular = (By.ID, 'zk-comp-100')
    concluir = (By.CSS_SELECTOR, 'table[id$="comp-102!box"] [class$="button-cm"]')

    alert_tipo = (By.CSS_SELECTOR, 'div[class="z-separator-hor-bar"]')
    alert_texto = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[1]/tbody/tr/td[3]/div/span')
    btn_ok_alert = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[2]/tbody/tr/td/span/table/tbody/tr['
                              '2]/td[2]')

    def caminho(self):
        sleep(1)
        self.find_element(self.inscricao_eventos).click()
        sleep(1)
        self.find_element(self.evento).click()
        sleep(1)

    def espera_mensagem(self):
        try:
            alert_tipo = WebDriverWait(self.webdriver, poll_frequency=0.2, timeout=5)
            alert_tipo.until(expected_conditions.visibility_of_element_located(self.alert_tipo))
            if alert_tipo is not None:
                return True
        except TimeoutException:
            return False

    # ---------- Casos de teste: Evento não selecionado --------------#
    def ct50_inscricao_externo(self, cpf, nome, email, telefone, celular):
        txt = "Inscrição solicitada!"
        try:
            self.find_element(self.proxima_pagina).click()
            sleep(1)
            self.find_element(self.atividade).click()
            sleep(1)
            self.find_element(self.cpf).send_keys(cpf)
            self.find_element(self.nome).send_keys(nome)
            self.find_element(self.email).send_keys(email)
            self.find_element(self.confirmar).click()
            sleep(1)
            self.find_element(self.telefone).send_keys(telefone)
            self.find_element(self.celular).send_keys(celular)
            self.find_element(self.concluir).click()
            msg = self.espera_mensagem()
            if msg is True:
                if txt in self.find_element(self.alert_texto).text:
                    print("\n CT_50 sem erros: " + self.find_element(self.alert_texto).text)
                else:
                    print("\n [!] CT_50 reportou erro: " + self.find_element(self.alert_texto).text)
                self.find_element(self.btn_ok_alert).click()
            else:
                print("\n CT_50 sem erros: Inscrição solicitada com sucesso!")

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_50 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n [!] CT_22 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # - Casos de teste: Confirmar inscrição de usuário externo padrão-#
    # def ct51_inscricao_externo(self):
    # ---------- Casos de teste: Prazo para inscrição vencido --------#
    # def ct52_inscricao_externo(self):
    # --------------- Casos de teste: CPF inválido -------------------#
    # def ct53_inscricao_externo(self):
    # -------------- Casos de teste: Email inválido ------------------#
    # def ct54_inscricao_externo(self):
    # - Casos de teste: Campos obrigatórios no primeiro formulário ---#
    # def ct55_inscricao_externo(self):
    # -- Casos de teste: Campos obrigatórios no segundo formulário ---#