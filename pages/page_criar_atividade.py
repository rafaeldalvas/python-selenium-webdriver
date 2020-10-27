from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, \
    ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.config import PageElement
from time import sleep

class criarAtividade(PageElement):
    # CAMINHO
    calendario = (By.CSS_SELECTOR, "i.fa-calendar")
    admin = (By.CSS_SELECTOR, "a[href$='admEvento/inicial.zul?']")
    cadastro_atividade = (By.ID, 'zk-comp-112')
    radio_atividade = (By.ID, 'zk-comp-116!real')
    combo_atividade = (By.ID, "zk-comp-125!btn")  # COMBO BOX
    evento = (By.CSS_SELECTOR, 'tr[id$="comp-930"] [class="z-combo-item-text"]')  # EVENTO TESTES DALVAS E JP
    btn_novo = (By.CSS_SELECTOR, '.z-button-cm')

    # FORMULARIO BASICO
    combo_tipo = (By.ID, 'zk-comp-155!btn')
    tipo = (By.CSS_SELECTOR, 'tr[id$="comp-209"] [class="z-combo-item-text"]')
    tema = (By.ID, 'zk-comp-163')
    descricao = (By.ID, 'zk-comp-166')
    vagas = (By.ID, 'zk-comp-169')
    duracao = (By.ID, 'zk-comp-173')
    combo_palestrante = (By.ID, 'zk-comp-192!btn')
    palestrante = (By.CSS_SELECTOR, 'tr[id$="comp-228"] [class="z-combo-item-text"]') #Alberto Duque Portugal

    #DATAS DA ATIVIDADE
    botao_definir = (By.CSS_SELECTOR, 'span[id$="comp-187"] [class$="button-cm"]')
    sala = (By.ID, 'zk-comp-957')
    data = (By.ID, 'zk-comp-960!real')
    hora_inicio = (By.ID, 'zk-comp-963')
    hora_fim = (By.ID, 'zk-comp-966')
    botao_adicionar = (By.CSS_SELECTOR, 'table[id$="comp-967!box"] [class$="button-cm"]')
    botao_salvar = (By.CSS_SELECTOR, 'table[id$="comp-981!box"] [class$="button-cm"]')

    salvar = (By.CSS_SELECTOR, 'table[id$="comp-202!box"] [class$="button-cm"]')

    alert_tipo = (By.CSS_SELECTOR, 'div[class$="modal-cm-noborder"] div[class="myMultiMessageBox"]')
    alert_texto = (By.CSS_SELECTOR, '#zk-comp-990')
    ok_alert = (By.CSS_SELECTOR, 'table[id$="!box"] > tbody > tr:nth-child(2) > td.z-button-cm')


    def caminho(self):
        sleep(1)
        self.find_element(self.calendario).click()
        sleep(1)
        self.find_element(self.admin).click()
        sleep(1)
        self.find_element(self.cadastro_atividade).click()
        sleep(1)
        self.find_element(self.radio_atividade).click()
        sleep(1)
        self.find_element(self.combo_atividade).click()
        sleep(1)
        self.find_element(self.evento).click()
        sleep(1)
        self.find_element(self.btn_novo).click()

    def espera_mensagem(self):
        try:
            element = self.find_element(self.alert_tipo)
            return True
        except NoSuchElementException:
            return False

    # --------- Casos de teste: Criação de evento padrão -------------#

    def ct11_criar_atividade(self, tema, descricao, vagas, duracao, sala, data, hora_inicio, hora_fim):
        try:
            sleep(1)
            self.find_element(self.combo_tipo).click()
            self.find_element(self.tipo).click()
            self.find_element(self.tema).send_keys(tema)
            self.find_element(self.descricao).send_keys(descricao)
            self.find_element(self.vagas).send_keys(vagas)
            self.find_element(self.duracao).send_keys(duracao)

            # DATAS DA ATIVIDADE
            self.find_element(self.botao_definir).click()
            sleep(1)
            self.find_element(self.sala).send_keys(sala)
            self.find_element(self.data).send_keys(data)
            self.find_element(self.hora_inicio).send_keys(hora_inicio)
            self.find_element(self.hora_fim).send_keys(hora_fim)
            self.find_element(self.botao_adicionar).click()
            self.find_element(self.botao_salvar).click()
            sleep(1)
            # RESPONSAVEL
            self.find_element(self.combo_palestrante).click()
            self.find_element(self.palestrante).click()
            # self.find_element(self.salvar).click()
            sleep(1)
            msg = self.espera_mensagem()

            print("\n CT_11 sem erros: atividade criada com sucesso!")

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_11 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n [!] CT_11 reportou erro: " + self.find_element(self.alert_texto).text)
            sleep(1)
            self.find_element(self.ok_alert).click()

    # ------------- Caso de teste: Cancelar transação ----------------#

    def ct12_criar_atividade(self):
        try:
            sleep(1)
            self.find_element(self.combo_tipo).click()
            self.find_element(self.tipo).click()

            print("\n CT_12 sem erros: atividade cancelada com sucesso!")

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_12 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n [!] CT_12 reportou erro: " + self.find_element(self.alert_texto).text)
            sleep(1)
            self.find_element(self.ok_alert).click()

    # --------------- Caso de teste: Data incoerente -----------------#
    def ct13_criar_atividade(self, tema, vagas, duracao, sala, data, hora_inicio, hora_fim):
        try:
            sleep(1)
            self.find_element(self.combo_tipo).click()
            self.find_element(self.tipo).click()
            self.find_element(self.tema).send_keys(tema)
            self.find_element(self.vagas).send_keys(vagas)
            self.find_element(self.duracao).send_keys(duracao)

            # DATAS DA ATIVIDADE
            self.find_element(self.botao_definir).click()
            sleep(1)
            self.find_element(self.sala).send_keys(sala)
            self.find_element(self.data).send_keys(data)
            self.find_element(self.hora_inicio).send_keys(hora_inicio)
            self.find_element(self.hora_fim).send_keys(hora_fim)
            self.find_element(self.botao_adicionar).click()
            self.find_element(self.botao_salvar).click()
            # self.find_element(self.salvar).click()
            msg = self.espera_mensagem()

            print("\n [!] CT_13 sem erros: atividade criada com sucesso!")

        except UnexpectedAlertPresentException as e:
            print("\n CT_13 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n CT_13 reportou erro: " + self.find_element(self.alert_texto).text)
            sleep(1)
            self.find_element(self.ok_alert).click()

# --------------- Caso de teste: Hora incoerente -----------------#

    def ct14_criar_atividade(self, tema, vagas, duracao, sala, data, hora_inicio, hora_fim):
        try:
            sleep(1)
            self.find_element(self.combo_tipo).click()
            self.find_element(self.tipo).click()
            self.find_element(self.tema).send_keys(tema)
            self.find_element(self.vagas).send_keys(vagas)
            self.find_element(self.duracao).send_keys(duracao)

            # DATAS DA ATIVIDADE
            self.find_element(self.botao_definir).click()
            sleep(1)
            self.find_element(self.sala).send_keys(sala)
            self.find_element(self.data).send_keys(data)
            self.find_element(self.hora_inicio).send_keys(hora_inicio)
            self.find_element(self.hora_fim).send_keys(hora_fim)
            self.find_element(self.botao_adicionar).click()
            self.find_element(self.botao_salvar).click()
            # self.find_element(self.salvar).click()
            msg = self.espera_mensagem()

            print("\n [!] CT_14 sem erros: atividade criada com sucesso!")

        except UnexpectedAlertPresentException as e:
            print("\n CT_14 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n CT_14 reportou erro: " + self.find_element(self.alert_texto).text)
            sleep(1)
            self.find_element(self.ok_alert).click()