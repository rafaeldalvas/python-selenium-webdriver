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
    inscricoes_pendentes = (By.CSS_SELECTOR, 'table[id$="comp-127!box"] [class$="button-cm"]')
    todas_inscricoes = (By.CSS_SELECTOR, 'table[id$="comp-129!box"] [class$="button-cm"]')
    checkbox_presente = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div['
                                   '1]/div/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div/div['
                                   '2]/table/tbody[2]/tr[2]/td[1]/div/span/input')
    confirmar_selecionados =(By.CSS_SELECTOR, 'table[id$="comp-142!box"] [class$="button-cm"]')
    concluir = (By.CSS_SELECTOR, 'table[id$="comp-197!box"] [class$="button-cm"]')

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
        self.find_element(self.admin_inscricao).click()
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
    def ct44_confirmar_inscricao(self):
        try:
            self.find_element(self.combo_evento).click()
            sleep(1)
            self.find_element(self.evento).click()
            self.find_element(self.combo_atividade).click()
            sleep(1)
            self.find_element(self.atividade).click()
            self.find_element(self.inscricoes_pendentes).click()
            checkbox_presente = WebDriverWait(self.webdriver, poll_frequency=0.2, timeout=2)
            checkbox_presente.until(expected_conditions.visibility_of_element_located(self.checkbox_presente))
            if checkbox_presente is not None:
                self.find_element(self.checkbox_presente).click()
                sleep(1)
                self.find_element(self.confirmar_selecionados).click()
                sleep(1)
                self.find_element(self.concluir).click()
                sleep(1)
                msg = self.espera_mensagem()
                if msg is True:
                    txt = self.find_element(self.alert_texto).text
                    if txt == "As inscrições selecionadas foram confirmadas.":
                        print("\n CT_44 sem erros: " + txt)
                        self.find_element(self.btn_ok_alert).click()
                    else:
                        print("\n [!] CT_44 reportou erro: " + txt)
                        self.find_element(self.btn_ok_alert).click()

        except TimeoutException:
            print("\n [!] CT_44 reportou erro: Não foram exibidas as presenças")

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_44 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n [!] CT_44 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

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