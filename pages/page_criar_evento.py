from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, \
    ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.config import PageElement
from time import sleep


class criarEvento(PageElement):
    # CAMINHO
    calendario = (By.CSS_SELECTOR, "i.fa-calendar")
    admin = (By.CSS_SELECTOR, "a[href$='admEvento/inicial.zul?']")
    cadastro_evento = (By.ID, 'zk-comp-112')
    radio_evento = (By.ID, 'zk-comp-114!real')
    btn_novo = (By.CSS_SELECTOR, '.z-button-cm')

    # FORMULARIO PADRAO
    nome = (By.ID, 'zk-comp-148')
    descricao = (By.ID, 'zk-comp-151')
    site = (By.ID, 'zk-comp-154')
    email_responsavel = (By.ID, 'zk-comp-162')
    inicio_evento = (By.ID, 'zk-comp-173!real')
    fim_evento = (By.ID, 'zk-comp-176!real')
    inicio_inscricao = (By.ID, 'zk-comp-179!real')
    fim_inscricao = (By.ID, 'zk-comp-182!real')
    # COMBOBOX TIPO EVENTO
    btn_tipo_evento = (By.ID, 'zk-comp-185!btn')
    tipo_evento = (By.XPATH, '/html/body/div[3]/table/tbody/tr[4]/td[2]')  # Selecionar - Escola
    select_tipo_evento = (By.ID, 'zk-comp-185!real')
    # FIM COMBOBOX
    inscricao_externa = (By.ID, 'zk-comp-189!real')
    evento_pago = (By.ID, 'zk-comp-195!real')
    alert_tipo = (By.CSS_SELECTOR, 'div[class$="modal-cm-noborder"] div[class="myMultiMessageBox"]')

    # FORMUMARIO RESPONSAVEL
    btn_buscar = (By.CSS_SELECTOR, 'table[id$="comp-159!box"] [class$="button-cm"]')
    nome_responsavel = (By.XPATH, '/html/body/div[4]/div[2]/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div['
                               '1]/div/div/div/table/tbody/tr[2]/td[2]/input')  # Pesquisa - Raquel Alves da Silva
    btn_pesquisar_responsavel = (By.XPATH, '/html/body/div[4]/div[2]/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div['
                                           '1]/div/div/div/table/tbody/tr[2]/td[5]/span/table/tbody/tr[2]/td[2]')
    checkbox_responsavel = (By.XPATH, '/html/body/div[4]/div[2]/div[1]/div/div/div/div[1]/div[2]/table/tbody/tr['
                                      '1]/td[1]/div/div[2]/table/tbody[2]/tr/td[1]/div/input')
    seleciona_nome = (By.XPATH, '/html/body/div[4]/div[2]/div[1]/div/div/div/div[1]/div[2]/table/tbody/tr[1]/td['
                                '2]/div/span')
    btn_confirma_responsavel = (By.XPATH, '/html/body/div[4]/div[2]/div[1]/div/div/div/div[1]/div[3]/span')

    # FORMULARIO CERTIFICADO
    btn_editar_certificado = (By.CSS_SELECTOR, 'table[id$="comp-167!box"] [class$="button-cm"]')
    combo_certificado = (By.XPATH, "//*/div[4]/div[2]/div[1]/div/div/div/div[1]/div/div/table[1]/tbody/tr[2]/td[2]/span/span")  # COMBO BOX
    certificado = (By.XPATH, '/html/body/div[6]/table/tbody/tr[2]/td[2]')  # OPÇÃO PADRAO ICE

    combo_assinatura1 = (By.XPATH, "//*/div[4]/div[2]/div[1]/div/div/div/div[1]/div/div/table[1]/tbody/tr[3]/td[2]/span/span")
    assinatura1 = (By.XPATH, '//*/div[7]/table/tbody/tr[6]/td[2]')
    funcao1 = (By.XPATH, "//*/div[4]/div[2]/div[1]/div/div/div/div[1]/div/div/table[1]/tbody/tr[3]/td[4]/input")

    combo_assinatura2 = (By.XPATH, "//*/div/div/div/div[1]/div/div/table[1]/tbody/tr[4]/td[2]/span/span")
    assinatura2 = (By.XPATH, '//*/div[8]/table/tbody/tr[9]/td[2]')
    funcao2 = (By.XPATH, "//*/div[4]/div[2]/div[1]/div/div/div/div[1]/div/div/table[1]/tbody/tr[4]/td[4]/input")

    combo_assinatura3 = (By.XPATH, "//*/div/div/div/div[1]/div/div/table[1]/tbody/tr[5]/td[2]/span/span")
    assinatura3 = (By.XPATH, '/html/body/div[9]/table/tbody/tr[11]/td[2]')
    funcao3 = (By.XPATH, "//*/div[4]/div[2]/div[1]/div/div/div/div[1]/div/div/table[1]/tbody/tr[5]/td[4]/input")

    btn_salvar = (By.XPATH, '//*/div/div/div/div[1]/div/div/table[2]/tbody/tr/td[1]/span/table/tbody/tr[2]/td[2]')
    btn_ok = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[2]/tbody/tr/td/span/table/tbody/tr[2]/td[2]')

    # CONCLUIR
    btn_enviar = (By.CSS_SELECTOR, 'table[id$="comp-199!box"] [class$="button-cm"]')
    # CANCELAR
    btn_cancelar = (By.CSS_SELECTOR, 'table[id$="comp-201!box"] [class$="button-cm"]')

    # ALERT
    alert_tipo_erro = (By.CSS_SELECTOR, 'div[class="z-separator-hor-bar"]')
    alert_texto = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[1]/tbody/tr/td[3]/div/span')
    btn_ok_alert = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[2]/tbody/tr/td/span/table/tbody/tr[2]/td[2]')

    def espera_mensagem(self):
        try:
            alert_tipo = WebDriverWait(self.webdriver, poll_frequency=0.2, timeout=10)
            alert_tipo.until(expected_conditions.visibility_of_element_located(self.alert_tipo_erro))
            if alert_tipo is not None:
                return True
        except TimeoutException:
            return False

    def caminho(self):
        sleep(2)
        self.find_element(self.calendario).click()
        sleep(1)
        self.find_element(self.admin).click()
        sleep(1)
        self.find_element(self.cadastro_evento).click()
        sleep(1)
        self.find_element(self.radio_evento).click()
        sleep(2)
        self.find_element(self.btn_novo).click()



    def preenche_certificado(self, funcao1, funcao2, funcao3):
        self.find_element(self.btn_editar_certificado).click()
        sleep(2)
        self.find_element(self.combo_certificado).click()
        sleep(1)
        self.find_element(self.certificado).click()
        self.find_element(self.combo_assinatura1).click()
        sleep(1)
        self.find_element(self.assinatura1).click()
        self.find_element(self.funcao1).send_keys(funcao1)
        self.find_element(self.combo_assinatura2).click()
        sleep(1)
        self.find_element(self.assinatura2).click()
        self.find_element(self.funcao2).send_keys(funcao2)
        self.find_element(self.combo_assinatura3).click()
        sleep(1)
        self.find_element(self.assinatura3).click()
        self.find_element(self.funcao3).send_keys(funcao3)
        self.find_element(self.btn_salvar).click()
        sleep(3)
        self.find_element(self.btn_ok).click()

    def preenche_responsavel(self, nome_responsavel):
        sleep(1)
        self.find_element(self.btn_buscar).click()
        sleep(1)
        self.find_element(self.nome_responsavel).send_keys(nome_responsavel)
        sleep(1)
        self.find_element(self.btn_pesquisar_responsavel).click()
        sleep(1)
        self.find_element(self.checkbox_responsavel).click()
        sleep(2)
        self.find_element(self.seleciona_nome).click()
        sleep(1)
        self.find_element(self.btn_confirma_responsavel).click()

    # --------- Caso de teste: Criação de evento padrão -------------#
    def ct01_criar_evento(self, nome, descricao, site, email_responsavel, inicio_evento, fim_evento, inicio_inscricao,
                          fim_inscricao, funcao1, funcao2, funcao3):
        try:
            sleep(1)
            self.find_element(self.nome).send_keys(nome)
            self.find_element(self.descricao).send_keys(descricao)
            self.find_element(self.site).send_keys(site)
            self.find_element(self.email_responsavel).send_keys(email_responsavel)

            # CERTIFICADO
            self.preenche_certificado(funcao1, funcao2, funcao3)
            # FIM CERTIFICADO

            self.find_element(self.inicio_evento).clear()
            self.find_element(self.inicio_evento).send_keys(inicio_evento)
            self.find_element(self.fim_evento).clear()
            self.find_element(self.fim_evento).send_keys(fim_evento)
            self.find_element(self.inicio_inscricao).clear()
            self.find_element(self.inicio_inscricao).send_keys(inicio_inscricao)
            self.find_element(self.fim_inscricao).clear()
            self.find_element(self.fim_inscricao).send_keys(fim_inscricao)

            # TIPO DE EVENTO
            self.find_element(self.btn_tipo_evento).click()
            sleep(1)
            self.find_element(self.tipo_evento).click()
            # FIM TIPO DE EVENTO

            self.find_element(self.inscricao_externa).click()
            self.find_element(self.evento_pago).click()

            self.find_element(self.btn_enviar).click()

            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text == 'Evento salvo com sucesso':
                    print('\n CT_01 sem erros: o evento foi criado com sucesso')
                    assert True
                else:
                    print("\n [!] CT_01 reportou erro: " + self.find_element(self.alert_texto).text)
                    assert False
                self.find_element(self.btn_ok_alert).click()

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_01 reportou erro: " + str(e))
            assert False
        except ElementClickInterceptedException:
            print("\n [!] CT_01 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()
            assert False

    #------------ Caso de teste: Trocar responsável ---------------#
    def ct02_criar_evento(self, nome, descricao, site, email_responsavel, inicio_evento, fim_evento,
                          inicio_inscricao,
                          fim_inscricao, funcao1, funcao2, funcao3, nome_responsavel):
        try:
            sleep(1)
            self.find_element(self.nome).send_keys(nome)
            self.find_element(self.descricao).send_keys(descricao)
            self.find_element(self.site).send_keys(site)
            self.find_element(self.email_responsavel).send_keys(email_responsavel)

            self.preenche_responsavel(nome_responsavel)

            # CERTIFICADO
            self.preenche_certificado(funcao1, funcao2, funcao3)
            # FIM CERTIFICADO

            self.find_element(self.inicio_evento).clear()
            self.find_element(self.inicio_evento).send_keys(inicio_evento)
            self.find_element(self.fim_evento).clear()
            self.find_element(self.fim_evento).send_keys(fim_evento)
            self.find_element(self.inicio_inscricao).clear()
            self.find_element(self.inicio_inscricao).send_keys(inicio_inscricao)
            self.find_element(self.fim_inscricao).clear()
            self.find_element(self.fim_inscricao).send_keys(fim_inscricao)

            # TIPO DE EVENTO
            self.find_element(self.btn_tipo_evento).click()
            sleep(1)
            self.find_element(self.tipo_evento).click()
            # FIM TIPO DE EVENTO
            self.find_element(self.inscricao_externa).click()
            self.find_element(self.evento_pago).click()
            self.find_element(self.btn_enviar).click()
            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text.find('Evento salvo com sucesso') > -1:
                    print('\n CT_02 sem erros: a troca de responsável foi feita com sucesso')
                    assert True
                else:
                    print("\n [!] CT_02 reportou erro: " + self.find_element(self.alert_texto).text)
                    assert False
                self.find_element(self.btn_ok_alert).click()

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_02 reportou erro: " + str(e))
            assert False
        except ElementClickInterceptedException:
            print("\n [!] CT_02 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()
            assert False

    # ------------ Caso de teste: Cancelar transação ---------------#
    def ct03_criar_evento(self, nome, descricao):
        try:
            sleep(1)
            self.find_element(self.nome).send_keys(nome)
            self.find_element(self.descricao).send_keys(descricao)
            self.find_element(self.btn_cancelar).click()
            sleep(1)

            print('\n CT_03 sem erros: evento cancelado com sucesso')
            assert True

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_03 reportou erro: " + str(e))
            assert False

        except ElementClickInterceptedException:
            print("\n [!] CT_03 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()
            assert False

    # ----- Caso de teste: Campos obrigatórios não preenchidos -----#
    def ct04_criar_evento(self, nome, descricao, inicio_evento, fim_evento, inicio_inscricao, fim_inscricao):
        erro = True
        txt = "Evento salvo com sucesso"
        try:
            sleep(1)
            self.find_element(self.nome).send_keys(nome)
            self.find_element(self.descricao).send_keys(descricao)
            self.find_element(self.inicio_evento).clear()
            self.find_element(self.inicio_evento).send_keys(inicio_evento)
            self.find_element(self.fim_evento).clear()
            self.find_element(self.fim_evento).send_keys(fim_evento)
            self.find_element(self.inicio_inscricao).clear()
            self.find_element(self.inicio_inscricao).send_keys(inicio_inscricao)
            self.find_element(self.fim_inscricao).clear()
            self.find_element(self.fim_inscricao).send_keys(fim_inscricao)
            # TIPO DE EVENTO
            self.find_element(self.btn_tipo_evento).click()
            sleep(1)
            self.find_element(self.tipo_evento).click()
            # FIM TIPO DE EVENTO
            sleep(1)
            self.find_element(self.nome).clear()
            sleep(1)
            self.find_element(self.btn_enviar).click()
            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text != txt:
                    erro = False

            if erro is False:
                self.find_element(self.nome).send_keys(nome)
                self.find_element(self.descricao).clear()
                sleep(1)
                self.find_element(self.btn_enviar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != txt:
                        erro = False

            if erro is False:
                self.find_element(self.descricao).send_keys(descricao)
                self.find_element(self.inicio_evento).clear()
                sleep(1)
                self.find_element(self.btn_enviar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != txt:
                        erro = False

            if erro is False:
                self.find_element(self.inicio_evento).send_keys(inicio_evento)
                self.find_element(self.fim_evento).clear()
                sleep(1)
                self.find_element(self.btn_enviar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != txt:
                        erro = False

            if erro is False:
                self.find_element(self.fim_evento).send_keys(fim_evento)
                self.find_element(self.inicio_inscricao).clear()
                sleep(1)
                self.find_element(self.btn_enviar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != txt:
                        erro = False

            if erro is False:
                self.find_element(self.inicio_inscricao).send_keys(inicio_inscricao)
                self.find_element(self.fim_inscricao).clear()
                sleep(1)
                self.find_element(self.btn_enviar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != txt:
                        erro = False

            if erro is False:
                self.find_element(self.fim_inscricao).send_keys(fim_inscricao)
                self.find_element(self.select_tipo_evento).clear()
                sleep(1)
                self.find_element(self.btn_enviar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != txt:
                        erro = False

            if erro is False:
                print("\n CT_04 reportou erro: " + self.find_element(self.alert_texto).text)
                assert True
            else:
                print("\n [!] CT_04 reportou erro: Evento criado com campos obrigatorios nao preenchidos")
                assert False

        except UnexpectedAlertPresentException as e:
            print("\n CT_04 reportou erro: " + str(e))
            assert True

        except ElementClickInterceptedException:
            print("\n CT_04 reportou erro: " + self.find_element(self.alert_texto).text)
            assert True

    # --------------- Caso de teste: Data inválida ----------------#
    def ct05_criar_evento(self, nome, descricao, inicio_evento, fim_evento, inicio_inscricao,
                          fim_inscricao):
        try:
            sleep(1)
            self.find_element(self.nome).send_keys(nome)
            self.find_element(self.descricao).send_keys(descricao)
            self.find_element(self.inicio_evento).clear()
            self.find_element(self.inicio_evento).send_keys(inicio_evento)
            self.find_element(self.fim_evento).clear()
            self.find_element(self.fim_evento).send_keys(fim_evento)
            self.find_element(self.inicio_inscricao).clear()
            self.find_element(self.inicio_inscricao).send_keys(inicio_inscricao)
            self.find_element(self.fim_inscricao).clear()
            self.find_element(self.fim_inscricao).send_keys(fim_inscricao)
            # TIPO DE EVENTO
            self.find_element(self.btn_tipo_evento).click()
            sleep(1)
            self.find_element(self.tipo_evento).click()
            # FIM TIPO DE EVENTO
            self.find_element(self.btn_enviar).click()
            sleep(1)
            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text.find('Evento salvo com sucesso') > -1:
                    print('\n [!] CT_05 reportou erro: Evento criado com datas inválidas')
                    assert False
                elif self.find_element(self.alert_texto).text.find('Evento com data inválida') > -1:
                    print("\n CT_05 reportou erro: o sistema informou que as data são inválidas")
                    assert True
                else:
                    print("\n [!] CT_05 reportou erro: " + self.find_element(self.alert_texto).text)
                    assert False
                self.find_element(self.btn_ok_alert).click()

        except UnexpectedAlertPresentException as e:
            print("\n CT_05 reportou erro: " + str(e))
            assert True
        except ElementClickInterceptedException:
            print("\n CT_05 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()
            assert True
