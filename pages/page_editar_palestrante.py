from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from utils.config import PageElement


class editarPalestrante(PageElement):
    # CAMINHO
    calendario = (By.CSS_SELECTOR, "i.fa-calendar")
    admin = (By.CSS_SELECTOR, "a[href$='admEvento/inicial.zul?']")
    cadastro_palestrante = (By.ID, 'zk-comp-112')
    radio_palestrante = (By.ID, 'zk-comp-118!real')
    seleciona_palestrante = (By.CSS_SELECTOR, 'div[id$="zk-comp-124!body"]')
    btn_editar = (By.ID, 'zk-comp-132!box')

    # FORMULÁRIO PADRAO
    nome = (By.ID, 'zk-comp-145')
    email = (By.ID, 'zk-comp-148')
    cpf = (By.ID, 'zk-comp-151')
    rg = (By.ID, 'zk-comp-154')
    pis = (By.ID, 'zk-comp-157')
    resumo_curriculo = (By.ID, 'zk-comp-160')
    link_lates = (By.ID, 'zk-comp-163')
    telefone = (By.ID, 'zk-comp-166')
    endereco = (By.ID, 'zk-comp-169')
    agencia = (By.ID, 'zk-comp-172')
    conta = (By.ID, 'zk-comp-175')
    valor_participacao = (By.ID, 'zk-comp-178')
    valor_transporte = (By.ID, 'zk-comp-181')
    pagou_transporte = (By.ID, 'zk-comp-185!real')  # SELECIONANDO SIM
    valor_alimentacao = (By.ID, 'zk-comp-189')
    pagou_alimentacao = (By.ID, 'zk-comp-193!real')  # SELECIONANDO SIM
    valor_hotel = (By.ID, 'zk-comp-197')
    pagou_hotel = (By.ID, 'zk-comp-201!real')  # SELECIONANDO SIM

    # CONCLUIR
    salvar = (By.CSS_SELECTOR, 'table[id$="zk-comp-205!box"] [class$="button-cm"]')

    # CANCELAR
    btn_cancelar = (By.ID, 'zk-comp-207!chdextr')

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

    def caminho(self, ct29 = False):
        sleep(2)
        self.find_element(self.calendario).click()
        sleep(1)
        self.find_element(self.admin).click()
        sleep(1)
        self.find_element(self.cadastro_palestrante).click()
        sleep(1)
        self.find_element(self.radio_palestrante).click()
        if ct29 is False:
            sleep(2)
            self.find_element(self.seleciona_palestrante).click()
        sleep(2)
        self.find_element(self.btn_editar).click()

# ------------ Caso de teste: Edição de palestrante padrão ---------------#
    def ct27_editar_palestrante(self, nome, email, cpf, rg, pis,resumo_curriculo, link_lates, telefone, endereco,
                                   agencia, conta, valor_participacao, valor_transporte, valor_alimentacao,
                                   valor_hotel):
        try:
            sleep(1)
            self.find_element(self.nome).clear()
            self.find_element(self.nome).send_keys(nome)
            self.find_element(self.email).clear()
            self.find_element(self.email).send_keys(email)
            self.find_element(self.cpf).clear()
            self.find_element(self.cpf).send_keys(cpf)
            self.find_element(self.rg).clear()
            self.find_element(self.rg).send_keys(rg)
            self.find_element(self.pis).clear()
            self.find_element(self.pis).send_keys(pis)
            self.find_element(self.resumo_curriculo).clear()
            self.find_element(self.resumo_curriculo).send_keys(resumo_curriculo)
            self.find_element(self.link_lates).clear()
            self.find_element(self.link_lates).send_keys(link_lates)
            self.find_element(self.telefone).clear()
            self.find_element(self.telefone).send_keys(telefone)
            self.find_element(self.endereco).clear()
            self.find_element(self.endereco).send_keys(endereco)
            self.find_element(self.agencia).clear()
            self.find_element(self.agencia).send_keys(agencia)
            self.find_element(self.conta).clear()
            self.find_element(self.conta).send_keys(conta)
            self.find_element(self.valor_participacao).clear()
            self.find_element(self.valor_participacao).send_keys(valor_participacao)
            self.find_element(self.valor_transporte).clear()
            self.find_element(self.valor_transporte).send_keys(valor_transporte)
            self.find_element(self.pagou_transporte).click()
            self.find_element(self.valor_alimentacao).clear()
            self.find_element(self.valor_alimentacao).send_keys(valor_alimentacao)
            self.find_element(self.pagou_alimentacao).click()
            self.find_element(self.valor_hotel).clear()
            self.find_element(self.valor_hotel).send_keys(valor_hotel)
            self.find_element(self.pagou_hotel).click()

            self.find_element(self.salvar).click()

            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text == 'Palestrante salvo com sucesso':
                    print('\n CT_27 sem erros: o palestrante foi cadastrado com sucesso')
                else:
                    print("\n [!] CT_27 reportou erro: " + self.find_element(self.alert_texto).text)
                self.find_element(self.btn_ok_alert).click()
        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_27 reportou erro: " + str(e))
        except ElementClickInterceptedException:
            print("\n CT_27 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # ------------ Caso de teste: Cancelar edição ---------------#
    def ct_28_editar_palestrante(self):
        try:
            sleep(1)
            self.find_element(self.btn_cancelar).click()
            print('\n CT_28 sem erros: A operação foi cancelada com sucesso')

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT28 reportou erro: " + str(e))

    # ------------ Caso de teste: Palestrante não selecionado ---------------#
    def ct_29_editar_palestrante(self):
        try:
            sleep(1)
            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text == 'Selecione um palestrante':
                    print("\n CT_29 reportou erro: O sistema pediu para selecionar um palestrante")
                else:
                    print("\n [!] CT_29 reportou erro: " + self.find_element(self.alert_texto).text)
                self.find_element(self.btn_ok_alert).click()
            else:
                 print("\n [!] CT_29 reportou erro: Houve acesso ao formulário sem selecionar um palestrante")
            self.find_element(self.btn_ok_alert).click()
        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_29 reportou erro: " + str(e))
        except ElementClickInterceptedException:
            print("\n CT_19 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

    # ------------ Caso de teste: Caracteres inválidos ---------------#
    def ct_30_editar_palestrante(self, cpf, rg, pis, telefone, agencia, conta):
        erro = False
        try:
            sleep(1)
            cpf_old = self.find_element(self.cpf).get_attribute('value')
            self.find_element(self.cpf).clear()
            self.find_element(self.cpf).send_keys(cpf)
            self.find_element(self.salvar).click()
            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text == 'Palestrante salvo com sucesso':
                    erro = True
                self.find_element(self.btn_ok_alert).click()

            if erro is False:
                self.find_element(self.cpf).send_keys(cpf_old)
                rg_old = self.find_element(self.rg).get_attribute('value')
                self.find_element(self.rg).clear()
                self.find_element(self.rg).send_keys(rg)
                self.find_element(self.salvar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text == 'Palestrante salvo com sucesso':
                        erro = True
                    self.find_element(self.btn_ok_alert).click()

            if erro is False:
                self.find_element(self.rg).send_keys(rg_old)
                pis_old = self.find_element(self.pis).get_attribute('value')
                self.find_element(self.pis).clear()
                self.find_element(self.pis).send_keys(pis)
                self.find_element(self.salvar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text == 'Palestrante salvo com sucesso':
                        erro = True
                    self.find_element(self.btn_ok_alert).click()

            if erro is False:
                self.find_element(self.pis).send_keys(pis_old)
                telefone_old = self.find_element(self.telefone).get_attribute('value')
                self.find_element(self.telefone).clear()
                self.find_element(self.telefone).send_keys(telefone)
                self.find_element(self.salvar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text == 'Palestrante salvo com sucesso':
                        erro = True
                    self.find_element(self.btn_ok_alert).click()

            if erro is False:
                self.find_element(self.telefone).send_keys(telefone_old)
                agencia_old = self.find_element(self.agencia).get_attribute('value')
                self.find_element(self.agencia).clear()
                self.find_element(self.agencia).send_keys(agencia)
                self.find_element(self.salvar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text == 'Palestrante salvo com sucesso':
                        erro = True
                    self.find_element(self.btn_ok_alert).click()

            if erro is False:
                self.find_element(self.agencia).send_keys(agencia_old)
                conta_old = self.find_element(self.conta).get_attribute('value')
                self.find_element(self.conta).clear()
                self.find_element(self.conta).send_keys(conta)
                self.find_element(self.salvar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text == 'Palestrante salvo com sucesso':
                        erro = True
                    self.find_element(self.btn_ok_alert).click()

            if erro is False:
                print("\n CT_30 reportou erro: O sistema não permitiu caracteres inválidos")
            else:
                print("\n [!] CT_30 reportou erro: Palestrante editado com campos numéricos sem números")

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_30 reportou erro: " + str(e))

        except ElementClickInterceptedException as e:
            print("\n [!] CT_30 reportou erro: " + str(e))

# ------------ Caso de teste: Campos obrigatórios em branco ---------------#
    def ct_31_editar_palestrante(self, nome, email):
        erro = False
        try:
            sleep(2)
            self.find_element(self.nome).clear()
            self.find_element(self.salvar).click()
            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text == 'Palestrante salvo com sucesso':
                    erro = True
                self.find_element(self.btn_ok_alert).click()

            if erro is False:
                self.find_element(self.nome).send_keys(nome)
                self.find_element(self.email).clear()
                self.find_element(self.salvar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text == 'Palestrante salvo com sucesso':
                        erro = True
                    self.find_element(self.btn_ok_alert).click()


            if erro is False:
                self.find_element(self.nome).send_keys(email)
                self.find_element(self.cpf).clear()
                self.find_element(self.salvar).click()
                msg = self.espera_mensagem()
                if msg is True:
                    if self.find_element(self.alert_texto).text == 'Palestrante salvo com sucesso':
                        erro = True
                    self.find_element(self.btn_ok_alert).click()

            if erro is False:
                print("\n CT_31 reportou erro: O sistema exibiu os campos faltantes")
            else:
                print("\n [!] CT_31 reportou erro: Palestrante editado com campos obrigatorios nao preenchidos")

        except UnexpectedAlertPresentException as e:
            print("\n CT_31 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n [!] CT_31 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()

# ------------ Caso de teste: CPF inválido ---------------#
    def ct_32_editar_palestrante(self, cpf):
        erro = False
        try:
            sleep(2)
            self.find_element(self.cpf).clear()
            self.find_element(self.cpf).send_keys(cpf)
            self.find_element(self.salvar).click()
            msg = self.espera_mensagem()
            if msg is True:
                if self.find_element(self.alert_texto).text == 'Palestrante salvo com sucesso':
                    erro = True
                self.find_element(self.btn_ok_alert).click()

            if erro is False:
                print("\n CT_32 reportou erro: O sistema não permitiu um CPF inválido")
            else:
                print("\n [!] CT_32 reportou erro: Palestrante editado com CPF inválido")

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_32 reportou erro: " + str(e))

        except ElementClickInterceptedException:
            print("\n [!] CT_32 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()




























