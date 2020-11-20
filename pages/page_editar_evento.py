from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.config import PageElement
from time import sleep

class editarEvento(PageElement):
    # CAMINHO
    calendario = (By.CSS_SELECTOR, "i.fa-calendar")
    admin = (By.CSS_SELECTOR, "a[href$='admEvento/inicial.zul?']")
    main = (By.CSS_SELECTOR, "a[href$='inicial.zul']")
    cadastro_evento = (By.ID, 'zk-comp-112')
    radio_evento = (By.ID, 'zk-comp-114!real')
    radio_selec_evento = (By.CSS_SELECTOR, 'div.z-list-cell-cnt input')
    btn_editar = (By.CSS_SELECTOR, 'table[id$="zk-comp-134!box"] [class$="z-button-cm"]')
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
    tipo_evento = (By.ID, 'zk-comp-214') # Selecionar - Feira
    select_tipo_evento = (By.ID, 'zk-comp-185!real')
    # FIM COMBOBOX
    inscricao_externa = (By.ID, 'zk-comp-190!real') # Selecionar - Não
    evento_pago_aluno = (By.ID, 'zk-comp-195!real') # Desmarcar o campo "Aluno"
    evento_pago_externo = (By.ID, 'zk-comp-196!real') # Marcar o campo "Externo"

    # FORMUMARIO RESPONSAVEL
    btn_buscar = (By.CSS_SELECTOR, 'table[id$="comp-159!box"] [class$="button-cm"]')
    nome_responsavel = (By.ID, 'zk-comp-240')  # Pesquisar - Raquel Alves da Silva
    btn_pesquisar_responsavel = (By.CSS_SELECTOR, 'table[id$="comp-247!box"] [class$="button-cm"]')
    checkbox_responsavel = (By.CSS_SELECTOR, '[type="checkbox"]')
    seleciona_nome = (By.ID, 'table[id$="comp-259!box"] [class$="button-cm"]')
    btn_confirma_responsavel = (By.CSS_SELECTOR, 'table[id$="comp-278!box"] [class$="button-cm"]')

    # FORMULARIO CERTIFICADO
    btn_editar_certificado = (By.CSS_SELECTOR, 'table[id$="comp-167!box"] [class$="button-cm"]')
    combo_certificado = (By.ID, "zk-comp-233!btn")  # COMBO BOX
    certificado = (By.CSS_SELECTOR, 'tr[id$="zk-comp-277"] [class="z-combo-item-text"]')  # OPÇÃO PADRAO ICE 2

    combo_assinatura1 = (By.ID, "zk-comp-238!btn")
    assinatura1 = (By.CSS_SELECTOR, 'tr[id$="zk-comp-293"] [class="z-combo-item-text"]')
    funcao1 = (By.ID, "zk-comp-242")

    combo_assinatura2 = (By.ID, "zk-comp-247!btn")
    assinatura2 = (By.CSS_SELECTOR, 'tr[id$="zk-comp-332"] [class="z-combo-item-text"]')
    funcao2 = (By.ID, "zk-comp-251")

    combo_assinatura3 = (By.ID, "zk-comp-256!btn")
    assinatura3 = (By.CSS_SELECTOR, 'tr[id$="zk-comp-387"] [class="z-combo-item-text"]')
    funcao3 = (By.ID, "zk-comp-260")

    btn_salvar = (By.CSS_SELECTOR, 'table[id$="comp-263!box"] [class$="button-cm"]')
    btn_ok = (By.CSS_SELECTOR, 'table[id$="comp-403!box"] [class$="button-cm"]')

    # CONCLUIR
    btn_enviar = (By.CSS_SELECTOR, 'table[id$="comp-199!box"] [class$="button-cm"]')

    # EXCLUIR EVENTO
    btn_excluir = (By.CSS_SELECTOR, 'table[id$="zk-comp-136!box"] [class$="z-button-cm"]')
    confirm_excluir = (By.CSS_SELECTOR, 'table[id$="zk-comp-229!box"] [class$="z-button-cm"]')

    # CANCELAR
    btn_cancelar = (By.CSS_SELECTOR, 'table[id$="comp-201!box"] [class$="button-cm"]')

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


    def caminho(self, ct_08 = False, ct_10 = False):
        sleep(2)
        self.find_element(self.calendario).click()
        sleep(1)
        self.find_element(self.admin).click()
        sleep(1)
        self.find_element(self.cadastro_evento).click()
        sleep(1)
        self.find_element(self.radio_evento).click()
        sleep(1)
        if ct_10 is False:
            self.find_element(self.radio_selec_evento).click()
        sleep(1)
        if ct_08 is False:
            self.find_element(self.btn_editar).click()

    def preenche_certificado(self, funcao1, funcao2, funcao3):
        self.find_element(self.btn_editar_certificado).click()
        sleep(1)
        self.find_element(self.combo_certificado).click()
        self.find_element(self.certificado).click()
        self.find_element(self.combo_assinatura1).click()
        self.find_element(self.assinatura1).click()
        self.find_element(self.funcao1).clear()
        self.find_element(self.funcao1).send_keys(funcao1)
        self.find_element(self.combo_assinatura2).click()
        self.find_element(self.assinatura2).click()
        self.find_element(self.funcao2).clear()
        self.find_element(self.funcao2).send_keys(funcao2)
        self.find_element(self.combo_assinatura3).click()
        self.find_element(self.assinatura3).click()
        self.find_element(self.funcao3).clear()
        self.find_element(self.funcao3).send_keys(funcao3)
        self.find_element(self.btn_salvar).click()
        sleep(1)
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

    # --------- Caso de teste: Edição de evento padrão -------------#
    def ct_06_editar_evento(self,nome, descricao, site, email_responsavel, inicio_evento, fim_evento, inicio_inscricao,
                          fim_inscricao, funcao1, funcao2, funcao3, nome_responsavel):

        try:
            sleep(1)
            self.find_element(self.nome).clear()
            self.find_element(self.nome).send_keys(nome)
            self.find_element(self.descricao).clear()
            self.find_element(self.descricao).send_keys(descricao)
            self.find_element(self.site).clear()
            self.find_element(self.site).send_keys(site)
            self.find_element(self.email_responsavel).clear()
            self.find_element(self.email_responsavel).send_keys(email_responsavel)

            # CERTIFICADO
            self.preenche_certificado(funcao1, funcao2, funcao3)
            # FIM CERTIFICADO

            # RESPONSAVEL
            self.preenche_responsavel(nome_responsavel) # DA ERRO DE JS AQUI
            # FIM RESPONSAVEL

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
            self.find_element(self.evento_pago_aluno).click()
            self.find_element(self.evento_pago_externo).click()

            self.find_element(self.btn_enviar).click()
            sleep(1)
            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text == 'Evento salvo com sucesso':
                    print('\n CT_06 sem erros: o evento foi editado com sucesso')
                else:
                    print("\n [!] CT_06 reportou erro: Não houve edição do evento")
                self.find_element(self.btn_ok_alert).click()
        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_06 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n [!] CT_06 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

# --------- Caso de teste: Exclusão de eventos -------------#
    def ct_07_editar_evento(self):
        try:
            self.find_element(self.btn_excluir).click()
            sleep(1)
            self.find_element(self.confirm_excluir).click()
            sleep(1)
            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text == 'Evento excluído com sucesso':
                    print('\n CT_07 sem erros: o evento foi excluído com sucesso')
                else:
                    print("\n [!] CT_07 reportou erro: Não houve exclusão do evento")
                self.find_element(self.btn_ok_alert).click()

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_07 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n [!] CT_07 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()


# --------- Caso de teste: Cancelar transação -------------#
    def ct_08_editar_evento(self):
        try:
            sleep(1)
            self.find_element(self.btn_cancelar).click()
            print('\n CT_08 sem erros: A operação foi cancelada com sucesso')

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_08 reportou erro: " + str(e))

# -- Caso de teste: Nenhum evento selecionado ao editar ---#
    def ct_9_editar_evento(self):
        try:
            sleep(1)
            msg = self.espera_mensagem()
            if msg is True:
                print("\n CT_09 reportou erro: O sistema pediu para selecionar um evento")
                sleep(1)
            else:
                 print("\n [!] CT_09 reportou erro: Houve acesso ao formulário sem selecionar um evento")
            self.find_element(self.btn_ok_alert).click()
        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_09 reportou erro: " + str(e))

# -- Caso de teste: Campos obrigatórios não preenchidos ---#
    def ct_10_editar_evento(self, nome, descricao, inicio_evento, fim_evento, inicio_inscricao, fim_inscricao, nome_responsavel):
        erro = True
        sleep(1)
        try:
            self.find_element(self.nome).clear()
            self.find_element(self.btn_enviar).click()
            msg = self.espera_mensagem()

            if msg is True:
                if self.find_element(self.alert_texto).text != 'Evento salvo com sucesso':
                    erro = False

            if erro is False:
                self.find_element(self.nome).send_keys(nome)
                self.find_element(self.descricao).clear()
                self.find_element(self.btn_enviar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != 'Evento salvo com sucesso':
                        erro = False

            if erro is False:
                self.find_element(self.descricao).send_keys(descricao)
                self.find_element(self.inicio_evento).clear()
                self.find_element(self.btn_enviar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != 'Evento salvo com sucesso':
                        erro = False

            if erro is False:
                self.find_element(self.inicio_evento).send_keys(inicio_evento)
                self.find_element(self.fim_evento).clear()
                self.find_element(self.btn_enviar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != 'Evento salvo com sucesso':
                        erro = False

            if erro is False:
                self.find_element(self.fim_evento).send_keys(fim_evento)
                self.find_element(self.inicio_inscricao).clear()
                self.find_element(self.btn_enviar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != 'Evento salvo com sucesso':
                        erro = False

            if erro is False:
                self.find_element(self.inicio_inscricao).send_keys(inicio_inscricao)
                self.find_element(self.fim_inscricao).clear()
                self.find_element(self.btn_enviar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != 'Evento salvo com sucesso':
                        erro = False

            if erro is False:
                self.find_element(self.fim_inscricao).send_keys(fim_inscricao)
                self.find_element(self.select_tipo_evento).clear()
                self.find_element(self.btn_enviar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text != 'Evento salvo com sucesso':
                        erro = False

            if erro is False:
                self.preenche_responsavel(nome_responsavel)

            if erro is False:
                print("\n CT_10 reportou erro: O sistema exibiu os campos faltantes")
            else:
                print("\n [!] CT_10 reportou erro: Evento editado com campos obrigatorios nao preenchidos")

        except UnexpectedAlertPresentException as e:
            print("\n CT_10 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n [!] CT_10 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()
