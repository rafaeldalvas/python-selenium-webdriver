from selenium.common.exceptions import UnexpectedAlertPresentException, TimeoutException, \
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
    dropdownLogout = (By.ID, "kMenu")
    logout = (By.ID, "zk-comp-102")
    admin = (By.CSS_SELECTOR, "a[href$='admEvento/inicial.zul?']")
    admin_inscricao = (By.CSS_SELECTOR, "a[href$='inicial.zul?pag=admInscricao']")

    # TIRAR INSCRICAO
    inscrever_se = (By.ID, "zk-comp-158!box")
    inscritos = (By.ID, "zk-comp-162!box")
    inscrever_se_ativdade1 = (By.ID, "zk-comp-12933!box")
    inscrever_se_ativdade2 = (By.ID, "zk-comp-12978!box")
    voltar = (By.ID, "zk-comp-164!box")

    # FECHAR ATIVIDADE
    controle_presenca = (By.ID, "zk-comp-116")
    mais_infos = (By.ID, "zk-comp-124!box")
    evento = (By.ID, "zk-comp-12952!box")
    reabrir = (By.ID, "zk-comp-135!box")

    # CERTIFICADO
    dropdownCertificado = (By.ID, "zk-comp-148!cell")
    gerar = (By.CLASS_NAME, "z-button-cm")

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

    def caminho(self):
        sleep(1)
        self.find_element(self.calendario).click()
        sleep(1)
        self.find_element(self.emissao).click()

    def tiraInscricao(self):
        self.find_element(self.inscrever_se).click()
        sleep(1)
        self.find_element(self.inscritos).click()
        sleep(1)
        self.find_element(self.inscrever_se_ativdade1).click()
        sleep(1)
        self.find_element(self.inscrever_se_ativdade2).click()
        sleep(1)
        self.find_element(self.voltar).click()
        sleep(1)

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
        except ElementClickInterceptedException:
            print("\n [!] CT_50 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

# ------------ Usuário sem certificado disponível  ---------------#
    def ct51_certificado_participante(self):
        try:
            sleep(1)
            self.find_element(self.dropdownCertificado).click()
            self.find_element(self.gerar).click()
            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text.find('Sem certificado para o participante') != -1:
                    print("\n CT_51 reportou erro: o sistema informou que não existe certificado para o participante")
                else:
                    print("\n [!] CT_51 sistema reportou erro: " + self.find_element(self.alert_texto).text)
            else:
                print("\n [!] CT_51 sistema reportou erro: não foi informado que o usuário não possui certificado para gerar")
        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_51 reportou erro: " + str(e))
        except ElementClickInterceptedException:
            print("\n [!] CT_51 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()
















