from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException
from selenium.webdriver.common.by import By
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
    tipo_evento = (By.ID, 'zk-comp-213')  # Selecionar - Escola
    select_tipo_evento = (By.ID, 'zk-comp-185!real')
    # FIM COMBOBOX
    inscricao_externa = (By.ID, 'zk-comp-189!real')
    evento_pago = (By.ID, 'zk-comp-195!real')
    alert_tipo = (By.CSS_SELECTOR, 'div[class$="modal-cm-noborder"] div[class="myMultiMessageBox"]')

    # FORMUMARIO RESPONSAVEL
    btn_buscar = (By.CSS_SELECTOR, 'table[id$="comp-159!box"] [class$="button-cm"]')
    nome_responsavel = (By.ID, 'zk-comp-240')  # Pesquisa - Raquel Alves da Silva
    btn_pesquisar_responsavel = (By.CSS_SELECTOR, 'table[id$="comp-247!box"] [class$="button-cm"]')
    checkbox_responsavel = (By.CSS_SELECTOR, '[type="checkbox"]')
    seleciona_nome = (By.ID, 'table[id$="comp-259!box"] [class$="button-cm"]')
    btn_confirma_responsavel = (By.CSS_SELECTOR, 'table[id$="comp-278!box"] [class$="button-cm"]')

    # FORMULARIO CERTIFICADO
    btn_editar_certificado = (By.CSS_SELECTOR, 'table[id$="comp-167!box"] [class$="button-cm"]')
    combo_certificado = (By.ID, "zk-comp-233!btn")  # COMBO BOX
    certificado = (By.CSS_SELECTOR, 'tr[id$="comp-271"] [class="z-combo-item-text"]')  # OPÇÃO PADRAO ICE

    combo_assinatura1 = (By.ID, "zk-comp-238!btn")
    assinatura1 = (By.CSS_SELECTOR, 'tr[id$="comp-285"] [class="z-combo-item-text"]')
    funcao1 = (By.ID, "zk-comp-242")

    combo_assinatura2 = (By.ID, "zk-comp-247!btn")
    assinatura2 = (By.CSS_SELECTOR, 'tr[id$="comp-322"] [class="z-combo-item-text"]')
    funcao2 = (By.ID, "zk-comp-251")

    combo_assinatura3 = (By.ID, "zk-comp-256!btn")
    assinatura3 = (By.CSS_SELECTOR, 'tr[id$="comp-361"] [class="z-combo-item-text"]')
    funcao3 = (By.ID, "zk-comp-260")

    btn_salvar = (By.CSS_SELECTOR, 'table[id$="comp-263!box"] [class$="button-cm"]')
    btn_ok = (By.CSS_SELECTOR, 'table[id$="comp-403!box"] [class$="button-cm"]')

    # CONCLUIR
    btn_enviar = (By.CSS_SELECTOR, 'table[id$="comp-199!box"] [class$="button-cm"]')
    # CANCELAR
    btn_cancelar = (By.CSS_SELECTOR, 'table[id$="comp-201!box"] [class$="button-cm"]')

    # ALERT
    alert_tipo_window = (By.CSS_SELECTOR, 'div[class="z-separator-hor-bar"]')
    alert_texto = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[1]/tbody/tr/td[3]/div/span')
    btn_ok_alert = (By.XPATH, '//*/div[2]/div[1]/div/div/div/div/div[2]/div/table[2]/tbody/tr/td/span/table/tbody/tr[''2]/td[2]')

    def espera_mensagem(self):
        try:
            element = self.find_element(self.alert_tipo)
            return True
        except NoSuchElementException:
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
        self.find_element(self.certificado).click()
        self.find_element(self.combo_assinatura1).click()
        self.find_element(self.assinatura1).click()
        self.find_element(self.funcao1).send_keys(funcao1)
        self.find_element(self.combo_assinatura2).click()
        self.find_element(self.assinatura2).click()
        self.find_element(self.funcao2).send_keys(funcao2)
        self.find_element(self.combo_assinatura3).click()
        self.find_element(self.assinatura3).click()
        self.find_element(self.funcao3).send_keys(funcao3)
        self.find_element(self.btn_salvar).click()
        sleep(2)
        self.find_element(self.btn_ok).click()

    def preenche_responsavel(self, nome_responsavel):
        sleep(1)
        self.find_element(self.btn_buscar).click()
        sleep(1)
        self.find_element(self.nome_responsavel).send_keys(nome_responsavel)
        self.find_element(self.btn_pesquisar_responsavel).click()
        self.find_element(self.checkbox_responsavel).click()
        self.find_element(self.seleciona_nome).click()
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
            self.find_element(self.tipo_evento).click()
            # FIM TIPO DE EVENTO

            self.find_element(self.inscricao_externa).click()
            self.find_element(self.evento_pago).click()

            self.find_element(self.btn_enviar).click()

            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text.find('Evento salvo com sucesso') > -1:
                    print('\n CT_01 sem erros: o evento foi criado com sucesso')
                else:
                    print("\n [!] CT_01 reportou erro: " + self.find_element(self.alert_texto).text)
                self.find_element(self.btn_ok_alert).click()
        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_01 reportou erro: " + str(e))
        except ElementClickInterceptedException:
            print("\n [!] CT_01 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # ------------ Caso de teste: Trocar responsável ---------------#
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
            self.find_element(self.tipo_evento).click()
            # FIM TIPO DE EVENTO
            self.find_element(self.inscricao_externa).click()
            self.find_element(self.evento_pago).click()
            self.find_element(self.btn_enviar).click()
            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text.find('Evento salvo com sucesso') > -1:
                    print('\n CT_02 sem erros: a troca de responsável foi feita com sucesso')
                else:
                    print("\n [!] CT_02 reportou erro: " + self.find_element(self.alert_texto).text)
                self.find_element(self.btn_ok_alert).click()
                
        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_02 reportou erro: " + str(e))
        except ElementClickInterceptedException:
            print("\n [!] CT_02 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # ------------ Caso de teste: Cancelar transação ---------------#
    def ct03_criar_evento(self, nome, descricao):
        try:
            sleep(1)
            self.find_element(self.nome).send_keys(nome)
            self.find_element(self.descricao).send_keys(descricao)
            self.find_element(self.btn_cancelar).click()
            sleep(1)

            print('\n CT_03 sem erros: evento cancelado com sucesso')

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_03 reportou erro: " + str(e))

    # ----- Caso de teste: Campos obrigatórios não preenchidos -----#
    def ct04_criar_evento(self, nome, descricao, inicio_evento, fim_evento, inicio_inscricao, fim_inscricao):
        erro = True
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
            self.find_element(self.tipo_evento).click()
            # FIM TIPO DE EVENTO
            sleep(1)
            self.find_element(self.nome).clear()
            self.find_element(self.btn_enviar).click()
            msg = self.espera_mensagem()
            if msg is True:
                erro = False

            if erro is False:
                self.find_element(self.nome).send_keys(nome)
                self.find_element(self.descricao).clear()
                self.find_element(self.btn_enviar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    erro = False

            if erro is False:
                self.find_element(self.descricao).send_keys(descricao)
                self.find_element(self.inicio_evento).clear()
                self.find_element(self.btn_enviar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    erro = False

            if erro is False:
                self.find_element(self.inicio_evento).send_keys(inicio_evento)
                self.find_element(self.fim_evento).clear()
                self.find_element(self.btn_enviar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    erro = False

            if erro is False:
                self.find_element(self.fim_evento).send_keys(fim_evento)
                self.find_element(self.inicio_inscricao).clear()
                self.find_element(self.btn_enviar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    erro = False

            if erro is False:
                self.find_element(self.inicio_inscricao).send_keys(inicio_inscricao)
                self.find_element(self.fim_inscricao).clear()
                self.find_element(self.btn_enviar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    erro = False

            if erro is False:
                self.find_element(self.fim_inscricao).send_keys(fim_inscricao)
                self.find_element(self.select_tipo_evento).clear()
                self.find_element(self.btn_enviar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    erro = False

            if erro is False:
                print("\n CT_04 reportou erro: O sistema exibiu os campos faltantes")
            else:
                print("\n [!] CT_04 reportou erro: Evento criado com campos obrigatorios nao preenchidos")

        except UnexpectedAlertPresentException as e:
            print("\n CT_04 reportou erro: " + str(e))
        except ElementClickInterceptedException:
            print("\n [!] CT_04 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

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
            self.find_element(self.tipo_evento).click()
            # FIM TIPO DE EVENTO
            self.find_element(self.btn_enviar).click()
            sleep(1)
            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text.find('Evento salvo com sucesso') > -1:
                    print('\n [!] CT_05 reportou erro: Evento criado com datas inválidas')
                elif self.find_element(self.alert_texto).text.find('Evento com data inválida') > -1:
                    print("\n CT_05 reportou erro: o sistema informou que as data são inválidas")
                else:
                    print("\n [!] CT_05 reportou erro: " + self.find_element(self.alert_texto).text)
                self.find_element(self.btn_ok_alert).click()
        except UnexpectedAlertPresentException as e:
            print("\n CT_05 reportou erro: " + str(e))
        except ElementClickInterceptedException:
            print("\n [!] CT_05 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()
