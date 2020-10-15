from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utils.login import LoginProfessor
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
    tipo_evento = (By.ID, 'zk-comp-213') # Selecionar - Escola
    # FIM COMBOBOX
    inscricao_externa = (By.ID, 'zk-comp-189!real')
    evento_pago = (By.ID, 'zk-comp-195!real')

    # FORMUMARIO RESPONSAVEL
    btn_buscar = (By.CSS_SELECTOR, '.z-button-cm')
    nome_responsavel = (By.ID, 'zk-comp-240')  # Pesquisa - Raquel Alves da Silva
    btn_pesquisar_responsavel = (By.CSS_SELECTOR, "[class|=z-button]")
    checkbox_responsavel = (By.ID, 'zk-comp-318!cm')
    seleciona_nome = (By.ID, 'zk-comp-259!hvig')
    btn_confirma_responsavel = (By.CSS_SELECTOR, "[class|=z-button]")

    # FORMULARIO CERTIFICADO
    btn_editar_certificado = (By.CSS_SELECTOR, '.z-button-cm:nth(2)')
    combo_certificado = (By.CSS_SELECTOR, "#zk-comp-1949!btn")  # COMBO BOX
    certificado = (By.CSS_SELECTOR, "#zk-comp-1988")  # OPÇÃO PADRAO ICE

    combo_assinatura1 = (By.CSS_SELECTOR, "zk-comp-1954!btn")
    assinatura1 = (By.CSS_SELECTOR, "#zk-comp-2001")
    funcao1 = (By.CSS_SELECTOR, "zk-comp-1958")

    combo_assinatura2 = (By.CSS_SELECTOR, "zk-comp-1963!btn")
    assinatura2 = (By.CSS_SELECTOR, "#zk-comp-2038")
    funcao2 = (By.CSS_SELECTOR, "zk-comp-1967")

    combo_assinatura3 = (By.CSS_SELECTOR, "#zk-comp-1972!btn")
    assinatura3 = (By.CSS_SELECTOR, "#zk-comp-2076")
    funcao3 = (By.CSS_SELECTOR, "zk-comp-1976")

    btn_salvar = (By.CSS_SELECTOR, "[class|=z-button]")
    btn_ok = (By.CSS_SELECTOR, "[class|=z-button]")

    # CONCLUIR
    btn_enviar = (By.CSS_SELECTOR, '[class|=z-button]')

    def caminho(self):
        sleep(1)
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
        sleep(2)
        self.find_element(self.btn_editar_certificado).click()
        self.find_element(self.combo_certificado).click()
        self.find_element(self.certificado).click()
        sleep(1)
        self.find_element(self.combo_assinatura1).click()
        self.find_element(self.assinatura1).click()
        self.find_element(self.funcao1).send_keys(funcao1)
        sleep(1)
        self.find_element(self.combo_assinatura2).click()
        self.find_element(self.assinatura2).click()
        self.find_element(self.funcao2).send_keys(funcao2)
        sleep(1)
        self.find_element(self.combo_assinatura3).click()
        self.find_element(self.assinatura3).click()
        self.find_element(self.funcao3).send_keys(funcao3)
        sleep(1)
        self.find_element(self.btn_salvar).click()
        self.find_element(self.btn_ok).click()

    def preenche_responsavel(self, nome_responsavel):
        sleep(1)
        self.find_element(self.btn_buscar).click()
        self.find_element(self.nome_responsavel).send_keys(nome_responsavel)
        self.find_element(self.btn_pesquisar_responsavel).click()
        self.find_element(self.checkbox_responsavel).click()
        self.find_element(self.seleciona_nome).click()
        self.find_element(self.btn_confirma_responsavel).click()

    def ct01_criar_evento(self, nome, descricao, site, email_responsavel, inicio_evento, fim_evento, inicio_inscricao,
                          fim_inscricao, funcao1, funcao2, funcao3):
        sleep(1)
        self.find_element(self.nome).send_keys(nome)
        self.find_element(self.descricao).send_keys(descricao)
        self.find_element(self.site).send_keys(site)
        self.find_element(self.email_responsavel).send_keys(email_responsavel)

        # CERTIFICADO
        self.preenche_certificado(funcao1, funcao2, funcao3)
        # FIM CERTIFICADO

        self.find_element(self.inicio_evento).send_keys(inicio_evento)
        self.find_element(self.fim_evento).send_keys(fim_evento)
        self.find_element(self.inicio_inscricao).send_keys(inicio_inscricao)
        self.find_element(self.fim_inscricao).send_keys(fim_inscricao)

        # TIPO DE EVENTO
        self.find_element(self.btn_tipo_evento).click()
        self.find_element(self.tipo_evento).click()
        # FIM TIPO DE EVENTO

        self.find_element(self.inscricao_externa).click()
        self.find_element(self.evento_pago).click()



