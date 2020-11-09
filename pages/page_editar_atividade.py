from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, \
    ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.config import PageElement
from time import sleep


class editarAtividade(PageElement):
    # CAMINHO
    calendario = (By.CSS_SELECTOR, "i.fa-calendar")
    admin = (By.CSS_SELECTOR, "a[href$='admEvento/inicial.zul?']")
    cadastro_atividade = (By.ID, 'zk-comp-112')
    radio_atividade = (By.ID, 'zk-comp-116!real')
    combo_atividade = (By.ID, "zk-comp-125!btn")  # COMBO BOX
    evento = (By.XPATH, '/html/body/div[3]/table/tbody/tr[2]/td[2]')  # EVENTO TESTES DALVAS E JP
    atividade = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div['
                           '1]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div['
                           '1]/div/div/div/table/tbody/tr[1]/td/div/div[2]/table/tbody[2]/tr[6]/td['
                           '1]/div/input')  # atividade teste
    atividade_2 = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div['
                             '1]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div['
                             '1]/div/div/div/table/tbody/tr[1]/td/div/div[2]/table/tbody[2]/tr[10]/td[1]/div/input')
    btn_editar = (By.CSS_SELECTOR, '#zk-comp-137\!box > tbody > tr:nth-child(2) > td.z-button-cm')

    # FORMULARIO BASICO
    combo_tipo = (By.ID, 'zk-comp-155!btn')
    tipo = (By.CSS_SELECTOR, 'tr[id$="comp-216"] [class="z-combo-item-text"]')
    tema = (By.ID, 'zk-comp-163')
    descricao = (By.ID, 'zk-comp-166')
    vagas = (By.ID, 'zk-comp-169')
    duracao = (By.ID, 'zk-comp-173')
    combo_palestrante = (By.ID, 'zk-comp-192!btn')
    palestrante = (By.CSS_SELECTOR, 'tr[id$="comp-228"] [class="z-combo-item-text"]')  # Alcione de Paiva Oliveira
    btn_add_palestrante = (By.ID, 'zk-comp-194!hvig')
    btn_excluir_palestrante = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div['
                                         '1]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div['
                                         '2]/div[1]/div/div/div/div/div[2]/table/tbody[2]/tr[9]/td['
                                         '2]/div/table/tbody/tr[3]/td/div/div[2]/table/tbody[2]/tr/td['
                                         '2]/div/span/table')

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
    btn_excluir_datas = (By.XPATH, '/html/body/div[6]/div[2]/div[1]/div/div/div/div[2]/div[2]/table/tbody[2]/tr/td['
                                   '6]/div/span/table/tbody/tr[2]/td[2]')

    btn_salvar = (By.CSS_SELECTOR, 'table[id$="comp-202!box"] [class$="button-cm"]')
    btn_cancelar = (By.CSS_SELECTOR, 'table[id$="comp-204!box"] [class$="button-cm"]')
    btn_excluir = (By.CSS_SELECTOR, 'table[id$="-comp-138!box"] [class$="button-cm"]')
    confirm_excluir = (By.XPATH, '/html/body/div[5]/div[2]/div[1]/div/div/div/div/div[2]/div/table[2]/tbody/tr/td['
                                 '1]/span/table/tbody/tr[2]/td[2]')

    alert_tipo = (By.CSS_SELECTOR, 'div[class="z-separator-hor-bar"]')
    alert_texto = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[1]/tbody/tr/td[3]/div/span')
    btn_ok_alert = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[2]/tbody/tr/td/span/table/tbody/tr['
                              '2]/td[2]')

    def caminho(self, ct16=False, ct17=False, ct19=False):
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
        if ct19 == False:
            if ct16 == False:
                self.find_element(self.atividade).click()
                sleep(1)
            else:
                self.find_element(self.atividade_2).click()
                sleep(1)
        if ct17 == False:
            self.find_element(self.btn_editar).click()
            sleep(1)

    def espera_mensagem(self):
        try:
            alert_tipo = WebDriverWait(self.webdriver, poll_frequency=0.2, timeout=10)
            alert_tipo.until(expected_conditions.visibility_of_element_located(self.alert_tipo))
            if alert_tipo is not None:
                return True
        except TimeoutException:
            return False

    def data_hora_atividade_ct21_ct22(self, sala, data, hora_inicio, hora_fim):
        sala1 = (By.XPATH, '/html/body/div[5]/div[2]/div[1]/div/div/div/div[1]/div[2]/table/tbody[2]/tr[2]/td[2]/div/input')
        data1 = (By.XPATH, '/html/body/div[5]/div[2]/div[1]/div/div/div/div[1]/div[2]/table/tbody[2]/tr[3]/td[2]/div/span/input')
        hora_inicio1 = (By.XPATH, '/html/body/div[5]/div[2]/div[1]/div/div/div/div[1]/div[2]/table/tbody[2]/tr[4]/td[2]/div/input')
        hora_fim1 = (By.XPATH, '/html/body/div[5]/div[2]/div[1]/div/div/div/div[1]/div[2]/table/tbody[2]/tr[5]/td[2]/div/input')
        btn_adicionar = (By.XPATH, '/html/body/div[5]/div[2]/div[1]/div/div/div/span/table/tbody/tr[2]/td[2]')
        btn_salvar_datas = (By.XPATH, '/html/body/div[5]/div[2]/div[1]/div/div/div/hbox/span[1]/table/tbody/tr[2]/td[2]')
        btn_excluir_datas = (By.XPATH, '/html/body/div[5]/div[2]/div[1]/div/div/div/div[2]/div[2]/table/tbody['
                                       '2]/tr/td[6]/div/span/table/tbody/tr[2]/td[2]')
        sleep(2)
        self.find_element(btn_excluir_datas).click()
        sleep(1)
        self.find_element(btn_salvar_datas).click()
        sleep(1)
        self.find_element(self.btn_definir).click()
        sleep(2)
        self.find_element(sala1).send_keys(sala)
        self.find_element(data1).clear()
        self.find_element(data1).send_keys(data)
        self.find_element(hora_inicio1).send_keys(hora_inicio)
        self.find_element(hora_fim1).send_keys(hora_fim)
        self.find_element(btn_adicionar).click()
        sleep(1)
        self.find_element(btn_salvar_datas).click()
        sleep(2)
        self.find_element(self.btn_salvar).click()


    # -------- Casos de teste: Edição de atividade padrão ------------#
    def ct16_editar_atividade(self, tema, descricao, vagas, duracao, sala, data, hora_inicio, hora_fim):
        try:
            sleep(1)
            self.find_element(self.combo_tipo).click()
            self.find_element(self.tipo).click()
            self.find_element(self.tema).clear()
            self.find_element(self.tema).send_keys(tema)
            self.find_element(self.descricao).clear()
            self.find_element(self.descricao).send_keys(descricao)
            self.find_element(self.vagas).clear()
            self.find_element(self.vagas).send_keys(vagas)
            self.find_element(self.duracao).clear()
            self.find_element(self.duracao).send_keys(duracao)

            # DATAS DA ATIVIDADE
            self.find_element(self.btn_definir).click()
            sleep(2)
            self.find_element(self.btn_excluir_datas).click()
            sleep(1)
            self.find_element(self.btn_salvar_datas).click()
            sleep(1)
            self.find_element(self.btn_definir).click()
            sleep(2)
            self.find_element(self.sala).clear()
            self.find_element(self.sala).send_keys(sala)
            self.find_element(self.data).clear()
            self.find_element(self.data).send_keys(data)
            self.find_element(self.hora_inicio).clear()
            self.find_element(self.hora_inicio).send_keys(hora_inicio)
            self.find_element(self.hora_fim).clear()
            self.find_element(self.hora_fim).send_keys(hora_fim)
            self.find_element(self.btn_adicionar).click()
            sleep(1)
            self.find_element(self.btn_salvar_datas).click()
            sleep(2)
            # RESPONSAVEL
            self.find_element(self.btn_excluir_palestrante).click()
            sleep(2)
            self.find_element(self.combo_palestrante).click()
            self.find_element(self.palestrante).click()
            self.find_element(self.btn_add_palestrante).click()
            self.find_element(self.btn_salvar).click()
            sleep(1)
            msg = self.espera_mensagem()
            if msg is True:
                txt = self.find_element(self.alert_texto).text
                if txt == "Atividade salva com sucesso":
                    print("\n CT_16 sem erros: " + txt)
                    self.find_element(self.btn_ok_alert).click()
                else:
                    print("\n [!] CT_16 reportou erro: " + txt)
                    self.find_element(self.btn_ok_alert).click()
            else:
                print("\n CT_16 sem erros: atividade editada com sucesso!")

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_16 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n [!] CT_16 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # ----------- Casos de teste: Exclusão de atividade --------------#
    def ct17_editar_atividade(self):
        try:
            self.find_element(self.btn_excluir).click()
            sleep(1)
            self.find_element(self.confirm_excluir).click()
            sleep(1)
            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text == 'Atividade excluída com sucesso':
                    print('\n CT_17 sem erros: o atividade foi excluída com sucesso')
                else:
                    print("\n [!] CT_17 reportou erro: Não houve exclusão da atividade")
                self.find_element(self.btn_ok_alert).click()

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_17 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n [!] CT_17 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # -------------- Casos de teste: Cancelar edição -----------------#
    def ct18_editar_atividade(self):
        try:
            sleep(1)
            self.find_element(self.combo_tipo).click()
            self.find_element(self.tipo).click()
            self.find_element(self.btn_cancelar).click()
            msg = self.espera_mensagem()
            if msg is True:
                print("\n [!] CT_18 reportou erro: " + self.find_element(self.alert_texto).text)
                self.find_element(self.btn_ok_alert).click()
            else:
                print("\n CT_18 sem erros: atividade cancelada com sucesso!")

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_18 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n [!] CT_18 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # --- Casos de teste: Nenhuma atividade selecionada ao editar ----#
    def ct19_editar_atividade(self):
        try:
            msg = self.espera_mensagem()
            if msg is True:
                print("\n CT_19 reportou erro: " + self.find_element(self.alert_texto).text)
                self.find_element(self.btn_ok_alert).click()
            else:
                print("\n [!] CT_19 sem erros: sistema não reportou erros!")

        except UnexpectedAlertPresentException as e:
            print("\n CT_19 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n CT_19 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # ----- Casos de teste: Campos obrigatórios não preenchidos ------#
    def ct20_editar_atividade(self, tema, descricao, vagas, duracao, local, sala, data, hora_inicio, hora_fim):
        erro = True
        txt = "Atividade salva com sucesso"
        try:
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
                print("\n CT_20 reportou erro: " + self.find_element(self.alert_texto).text)
            else:
                print("\n [!] CT_20 reportou erro: Evento criado com campos obrigatorios nao preenchidos")

        except UnexpectedAlertPresentException as e:
            print("\n CT_20 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n CT_20 reportou erro: " + self.find_element(self.alert_texto).text)

    # ---------------- Casos de teste: Data inválida -----------------#
    def ct21_editar_atividade(self, sala, data, hora_inicio, hora_fim):
        txt = "Atividade salva com sucesso"
        try:
            self.find_element(self.btn_definir).click()
            self.data_hora_atividade_ct21_ct22(sala, data, hora_inicio, hora_fim)
            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text != txt:
                    print("\n CT_21 reportou erro: " + self.find_element(self.alert_texto).text)
                else:
                    print("\n [!] CT_21 reportou erro: " + self.find_element(self.alert_texto).text)
                self.find_element(self.btn_ok_alert).click()
            else:
                print("\n [!] CT_21 sem erros: atividade criada com sucesso!")

        except UnexpectedAlertPresentException as e:
            print("\n CT_21 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n CT_21 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # ---------------- Casos de teste: Hora inválida -----------------#
    def ct22_editar_atividade(self, sala, data, hora_inicio, hora_fim):
        txt = "Atividade salva com sucesso"
        try:
            self.find_element(self.btn_definir).click()
            self.data_hora_atividade_ct21_ct22(sala, data, hora_inicio, hora_fim)
            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text != txt:
                    print("\n CT_21 reportou erro: " + self.find_element(self.alert_texto).text)
                else:
                    print("\n [!] CT_21 reportou erro: " + self.find_element(self.alert_texto).text)
                self.find_element(self.btn_ok_alert).click()
            else:
                print("\n [!] CT_22 sem erros: atividade criada com sucesso!")

        except UnexpectedAlertPresentException as e:
            print("\n CT_22 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n CT_22 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()