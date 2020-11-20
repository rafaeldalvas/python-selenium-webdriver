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
    mais_info = (By.ID, "zk-comp-151!box")
    mais_info_vencida = (By.ID, "zk-comp-137!box")
    skip = (By.ID, "zk-comp-137!tb_l")
    atividade = (By.CLASS_NAME, "z-button-cm")
    main = (By.CSS_SELECTOR, "a[href$='inicial.zul']")

    # CASOS DE TESTE
    inscrever_se = (By.ID, "zk-comp-158!box")
    inscritos = (By.ID, "zk-comp-162!box")
    inscrever_se_ativdade1 = (By.ID, "zk-comp-12933!box")
    inscrever_se_ativdade2 = (By.ID, "zk-comp-12978!box")
    voltar = (By.ID, "zk-comp-164!box")

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

    def caminho(self, noPrazo = False, vencida = False):
        sleep(2)
        self.find_element(self.calendario).click()
        sleep(1)
        self.find_element(self.menu_evento).click()
        sleep(1)
        if noPrazo is True:
            self.find_element(self.mais_info).click()
        elif vencida is True:
            self.find_element(self.mais_info_vencida).click()
        sleep(1)
        self.find_element(self.skip).click()
        sleep(1)
        self.find_element(self.atividade).click()

# ------------ Caso de teste: Inscrição padrão  ---------------#
    def ct40_inscricao(self):
        try:
            sleep(1)
            self.find_element(self.inscrever_se).click()
            sleep(5)
            msg = self.espera_mensagem()
            if msg is True:
                self.find_element(self.btn_ok_alert).click()
                sleep(5)
                msgConfirmacao = self.espera_mensagem()
                if msgConfirmacao is True and self.find_element(self.alert_texto).text.find('Inscrição solicitada!') != -1:
                    print('\n CT_40 sem erros: a inscrição foi solicitada com sucesso')
                    self.find_element(self.btn_ok_alert).click()
                else:
                    print("\n [!] CT_40 reportou erro: a inscrição não foi solicitada")
        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_40 reportou erro: " + str(e))

# ------------ Prazo para inscrição vencido  ---------------#
    def ct41_inscricao(self):
        try:
            sleep(1)
            self.find_element(self.inscrever_se).click()
            sleep(5)
            msg = self.espera_mensagem()
            if msg is True:
                self.find_element(self.btn_ok_alert).click()
                sleep(5)
                msgConfirmacao = self.espera_mensagem()
                if msgConfirmacao is True and self.find_element(self.alert_texto).text.find('Inscrição solicitada!') != -1:
                    print('\n [!] CT_41 reportou erro: a inscrição foi solicitada após o vencimento do prazo')
                else:
                    print("\n CT_41 reportou erro: a inscrição não foi solicitada")
        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_41 reportou erro: " + str(e))
        except NoSuchElementException as e:
            print("\n CT_41 reportou erro: a inscrição não foi solicitada")


# ------------ Ver Inscritos  ---------------#
    def ct42_inscricao(self):
        try:
            sleep(1)
            self.find_element(self.inscritos).click()
            sleep(1)
            url = self.webdriver.current_url
            if url.find('pag=listaInscritos') > 0:
                print('\n CT_42 sem erros: a lista de inscritos foi exibida')
            else:
                print('\n [!] CT_42 reportou erro: a lista de inscritos não foi exibida')
        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_42 reportou erro: " + str(e))

# ------------ Horário indisponível  ---------------#
    def ct43_inscricao(self):
        try:
            sleep(1)
            self.find_element(self.inscrever_se_ativdade1).click()
            msg = self.espera_mensagem()
            if msg is True:
                self.find_element(self.btn_ok_alert).click()
            self.find_element(self.voltar).click()

            self.find_element(self.inscrever_se_ativdade2).click()
            msg = self.espera_mensagem()
            if msg is True:
                self.find_element(self.btn_ok_alert).click()
                sleep(5)
                msgConfirmacao = self.espera_mensagem()
                if msgConfirmacao is True and self.find_element(self.alert_texto).text.find('Inscrição solicitada!') != -1:
                    print('\n CT_43 reportou erro: o sistema não permitiu a inscrição do usuário')
                else:
                    print("\n [!] CT_43 reportou erro: a inscrição foi solicitada sendo que o usuário não possui horário disponível")
        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_43 reportou erro: " + str(e))
        except NoSuchElementException as e:
            print("\n CT_43 reportou erro: usuário já inscrito na atividade")

















