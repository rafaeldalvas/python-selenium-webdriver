from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, \
    ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.config import PageElement
from time import sleep


class criarAtividade(PageElement):
    # CAMINHO
    calendario = (By.CSS_SELECTOR, "i.fa-calendar")
    admin = (By.CSS_SELECTOR, "a[href$='admEvento/inicial.zul?']")
    cadastro_atividade = (By.ID, 'zk-comp-112')
    radio_atividade = (By.ID, 'zk-comp-116!real')
    combo_atividade = (By.ID, "zk-comp-125!btn")  # COMBO BOX
    evento = (By.XPATH, '/html/body/div[3]/table/tbody/tr[2]/td[2]')  # EVENTO TESTES DALVAS E JP
    btn_novo = (By.CSS_SELECTOR, '.z-button-cm')

    # FORMULARIO BASICO
    combo_tipo = (By.ID, 'zk-comp-155!btn')
    tipo = (By.CSS_SELECTOR, 'tr[id$="comp-209"] [class="z-combo-item-text"]')
    tema = (By.ID, 'zk-comp-163')
    descricao = (By.ID, 'zk-comp-166')
    vagas = (By.ID, 'zk-comp-169')
    duracao = (By.ID, 'zk-comp-173')
    combo_palestrante = (By.ID, 'zk-comp-192!btn')
    palestrante = (By.CSS_SELECTOR, 'tr[id$="comp-228"] [class="z-combo-item-text"]')  # Alcione de Paiva Oliveira
    btn_add_palestrante = (By.ID, 'zk-comp-194!hvig')
    btn_excluir_palestrante = (By.CSS_SELECTOR, 'table[id$="comp-970!box"] [class$="button-cm"]')

    # DATAS DA ATIVIDADE
    btn_definir = (By.CSS_SELECTOR, 'span[id$="comp-187"] [class$="button-cm"]')
    local = (By.XPATH, '/html/body/div[5]/div[2]/div[1]/div/div/div/div[1]/div[2]/table/tbody[2]/tr[1]/td[2]/div/input')
    sala = (By.XPATH, '/html/body/div[6]/div[2]/div[1]/div/div/div/div[1]/div[2]/table/tbody[2]/tr[2]/td[2]/div/input')
    data = (By.XPATH, '/html/body/div[6]/div[2]/div[1]/div/div/div/div[1]/div[2]/table/tbody[2]/tr[3]/td['
                      '2]/div/span/input')
    hora_inicio = (By.XPATH, '/html/body/div[6]/div[2]/div[1]/div/div/div/div[1]/div[2]/table/tbody[2]/tr[4]/td['
                             '2]/div/input')
    hora_fim = (By.XPATH, '/html/body/div[6]/div[2]/div[1]/div/div/div/div[1]/div[2]/table/tbody[2]/tr[5]/td['
                          '2]/div/input')
    btn_adicionar = (By.XPATH, '/html/body/div[6]/div[2]/div[1]/div/div/div/span/table/tbody/tr[2]/td[2]')
    btn_salvar_datas = (By.XPATH, '/html/body/div[6]/div[2]/div[1]/div/div/div/hbox/span[1]/table/tbody/tr[2]/td[2]')
    btn_excluir_datas = (By.XPATH, '/html/body/div[5]/div[2]/div[1]/div/div/div/div[2]/div[2]/table/tbody[2]/tr/td['
                                   '6]/div/span/table/tbody/tr[2]/td[2]')

    btn_salvar = (By.CSS_SELECTOR, 'table[id$="comp-202!box"] [class$="button-cm"]')
    btn_cancelar = (By.CSS_SELECTOR, 'table[id$="comp-204!box"] [class$="button-cm"]')

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
            alert_tipo = WebDriverWait(self.webdriver, poll_frequency=0.2, timeout=10)
            alert_tipo.until(expected_conditions.visibility_of_element_located(self.alert_tipo))
            if alert_tipo is not None:
                return True
        except TimeoutException:
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
            self.find_element(self.btn_definir).click()
            sleep(3)
            self.find_element(self.sala).send_keys(sala)
            self.find_element(self.data).clear()
            self.find_element(self.data).send_keys(data)
            self.find_element(self.hora_inicio).send_keys(hora_inicio)
            self.find_element(self.hora_fim).send_keys(hora_fim)
            self.find_element(self.btn_adicionar).click()
            self.find_element(self.btn_salvar_datas).click()
            sleep(1)
            # RESPONSAVEL
            self.find_element(self.combo_palestrante).click()
            self.find_element(self.palestrante).click()
            self.find_element(self.btn_add_palestrante).click()
            self.find_element(self.btn_salvar).click()
            sleep(1)
            msg = self.espera_mensagem()
            if msg is True and self.find_element(self.alert_texto).text.find('Atividade salva com sucesso') != -1:
                print("\n [!] CT_11 reportou erro: " + self.find_element(self.alert_texto).text)
                self.find_element(self.btn_ok_alert).click()
            else:
                print("\n CT_11 sem erros: atividade criada com sucesso!")

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_11 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n [!] CT_11 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # ------------- Caso de teste: Cancelar transação ----------------#

    def ct12_criar_atividade(self):
        try:
            sleep(1)
            self.find_element(self.combo_tipo).click()
            self.find_element(self.tipo).click()
            self.find_element(self.btn_cancelar).click()
            msg = self.espera_mensagem()
            if msg is True:
                print("\n [!] CT_12 reportou erro: " + self.find_element(self.alert_texto).text)
                self.find_element(self.btn_ok_alert).click()
            else:
                print("\n CT_12 sem erros: atividade cancelada com sucesso!")

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_12 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n [!] CT_12 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # --------------- Caso de teste: Data incoerente -----------------#
    def ct13_criar_atividade(self, tema, descricao, vagas, duracao, sala, data, hora_inicio, hora_fim):
        try:
            sleep(1)
            self.find_element(self.combo_tipo).click()
            self.find_element(self.tipo).click()
            self.find_element(self.tema).send_keys(tema)
            self.find_element(self.descricao).send_keys(descricao)
            self.find_element(self.vagas).send_keys(vagas)
            self.find_element(self.duracao).send_keys(duracao)

            # DATAS DA ATIVIDADE
            self.find_element(self.btn_definir).click()
            sleep(1)
            self.find_element(self.sala).send_keys(sala)
            self.find_element(self.data).clear()
            self.find_element(self.data).send_keys(data)
            self.find_element(self.hora_inicio).send_keys(hora_inicio)
            self.find_element(self.hora_fim).send_keys(hora_fim)
            self.find_element(self.btn_adicionar).click()
            self.find_element(self.btn_salvar_datas).click()
            self.find_element(self.btn_salvar).click()
            msg = self.espera_mensagem()
            if msg is True:
                txt = self.find_element(self.alert_texto).text
                if txt == "Atividade salva com sucesso":
                    print("\n [!] CT_13 sem erros: atividade criada com sucesso!")
                else:
                    print("\n CT_13 reportou erro: " + self.find_element(self.alert_texto).text)
                    self.find_element(self.btn_ok_alert).click()
        except UnexpectedAlertPresentException as e:
            print("\n CT_13 reportou erro: " + str(e))
        except ElementClickInterceptedException:
            print("\n CT_13 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # --------------- Caso de teste: Hora incoerente -----------------#

    def ct14_criar_atividade(self, tema, descricao, vagas, duracao, sala, data, hora_inicio, hora_fim):
        try:
            sleep(1)
            self.find_element(self.combo_tipo).click()
            self.find_element(self.tipo).click()
            self.find_element(self.tema).send_keys(tema)
            self.find_element(self.descricao).send_keys(descricao)
            self.find_element(self.vagas).send_keys(vagas)
            self.find_element(self.duracao).send_keys(duracao)

            # DATAS DA ATIVIDADE
            self.find_element(self.btn_definir).click()
            sleep(2)
            self.find_element(self.sala).send_keys(sala)
            self.find_element(self.data).clear()
            self.find_element(self.data).send_keys(data)
            self.find_element(self.hora_inicio).send_keys(hora_inicio)
            self.find_element(self.hora_fim).send_keys(hora_fim)
            self.find_element(self.btn_adicionar).click()
            sleep(1)
            self.find_element(self.btn_salvar_datas).click()
            sleep(1)
            self.find_element(self.btn_salvar).click()
            msg = self.espera_mensagem()
            if msg is True:
                txt = self.find_element(self.alert_texto).text
                if txt == "Atividade salva com sucesso":
                    print("\n [!] CT_14 sem erros: " + txt)
                else:
                    print("\n CT_14 reportou erro: " + txt)
                    self.find_element(self.btn_ok_alert).click()
            else:
                print("\n [!] CT_14 sem erros: atividade criada com sucesso!")

        except UnexpectedAlertPresentException as e:
            print("\n CT_14 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n CT_14 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # ------------- Caso de teste: Campos obrigatórios ---------------#
    def ct15_criar_atividade(self, tema, descricao, vagas, duracao, local, sala, data, hora_inicio, hora_fim):
        erro = True
        txt = "Atividade salva com sucesso"
        try:
            sleep(1)
            self.find_element(self.combo_tipo).click()
            self.find_element(self.tipo).click()
            self.find_element(self.tema).send_keys(tema)
            self.find_element(self.descricao).send_keys(descricao)
            self.find_element(self.vagas).send_keys(vagas)
            self.find_element(self.duracao).send_keys(duracao)

            # DATAS DA ATIVIDADE
            self.find_element(self.btn_definir).click()
            sleep(2)
            self.find_element(self.sala).send_keys(sala)
            self.find_element(self.data).clear()
            self.find_element(self.data).send_keys(data)
            self.find_element(self.hora_inicio).send_keys(hora_inicio)
            self.find_element(self.hora_fim).send_keys(hora_fim)
            self.find_element(self.btn_adicionar).click()
            sleep(1)
            self.find_element(self.btn_salvar_datas).click()
            sleep(1)
            # RESPONSAVEL
            self.find_element(self.combo_palestrante).click()
            self.find_element(self.palestrante).click()
            self.find_element(self.btn_add_palestrante).click()

            self.find_element(self.tema).clear()
            self.find_element(self.btn_salvar).click()
            msg = self.espera_mensagem()
            if msg is True:
                erro = False

            if erro is False:
                self.find_element(self.tema).send_keys(tema)
                self.find_element(self.descricao).clear()
                self.find_element(self.btn_salvar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != txt:
                        erro = False

            if erro is False:
                self.find_element(self.descricao).send_keys(descricao)
                self.find_element(self.vagas).clear()
                self.find_element(self.btn_salvar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != txt:
                        erro = False

            if erro is False:
                self.find_element(self.vagas).send_keys(vagas)
                self.find_element(self.duracao).clear()
                self.find_element(self.btn_salvar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != txt:
                        erro = False

            if erro is False:
                self.find_element(self.duracao).send_keys(duracao)
                self.find_element(self.vagas).clear()
                self.find_element(self.btn_salvar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != txt:
                        erro = False

            if erro is False:
                self.find_element(self.descricao).send_keys(duracao)
                self.find_element(self.btn_definir).click()
                self.find_element(self.sala).send_keys(sala)
                self.find_element(self.data).clear()
                self.find_element(self.data).send_keys(data)
                self.find_element(self.hora_inicio).send_keys(hora_inicio)
                self.find_element(self.hora_fim).send_keys(hora_fim)
                self.find_element(self.local).clear()
                self.find_element(self.btn_adicionar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != txt:
                        erro = False

            if erro is False:
                self.find_element(self.local).send_keys(local)
                self.find_element(self.sala).clear()
                self.find_element(self.btn_salvar_datas).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != txt:
                        erro = False

            if erro is False:
                self.find_element(self.sala).send_keys(sala)
                self.find_element(self.data).clear()
                self.find_element(self.btn_salvar_datas).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != txt:
                        erro = False

            if erro is False:
                self.find_element(self.data).send_keys(data)
                self.find_element(self.hora_inicio).clear()
                self.find_element(self.btn_salvar_datas).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != txt:
                        erro = False

            if erro is False:
                self.find_element(self.hora_inicio).send_keys(hora_inicio)
                self.find_element(self.hora_fim).clear()
                self.find_element(self.btn_salvar_datas).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != txt:
                        erro = False

            if erro is False:
                self.find_element(self.hora_fim).send_keys(hora_fim)
                self.find_element(self.hora_inicio).clear()
                self.find_element(self.btn_salvar_datas).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != txt:
                        erro = False

            if erro is False:
                self.find_element(self.hora_inicio).send_keys(hora_inicio)
                self.find_element(self.btn_excluir_datas).click()
                self.find_element(self.btn_salvar_datas).click()
                self.find_element(self.btn_adicionar).click()
                self.find_element(self.btn_salvar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != txt:
                        erro = False

            if erro is False:
                self.find_element(self.btn_excluir_palestrante).clear()
                self.find_element(self.btn_salvar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != txt:
                        erro = False

                if erro is False:
                    self.find_element(self.combo_tipo).send_keys(Keys.BACKSPACE)
                    self.find_element(self.combo_palestrante).click()
                    self.find_element(self.palestrante).click()
                    self.find_element(self.btn_add_palestrante).click()
                    self.find_element(self.btn_salvar).click()
                    msg = self.espera_mensagem()
                    if msg is True:
                        if self.find_element(self.alert_texto).text != txt:
                            erro = False

            if erro is False:
                print("\n CT_15 reportou erro: " + self.find_element(self.alert_texto).text)
            else:
                print("\n [!] CT_15 reportou erro: Evento criado com campos obrigatorios nao preenchidos")

        except UnexpectedAlertPresentException as e:
            print("\n CT_15 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n CT_15 reportou erro: " + self.find_element(self.alert_texto).text)
