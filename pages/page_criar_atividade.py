from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException
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
    sala = (By.CSS_SELECTOR, '')
    hora_inicio = (By.CSS_SELECTOR, 'zk-comp-963')
    hora_fim = (By.CSS_SELECTOR, 'zk-comp-1119')
    botao_adicionar = (By.CSS_SELECTOR, 'table[id$="comp-159!box"] [class$="button-cm"]')
    botao_salvar = (By.CSS_SELECTOR, 'table[id$="comp-159!box"] [class$="button-cm"]')

    salvar = (By.CSS_SELECTOR, 'table[id$="comp-202!box"] [class$="button-cm"]')

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
        sleep(2)
        self.find_element(self.btn_novo).click()

    # --------- Caso de teste: Criação de evento padrão -------------#
    def ct01_criar_atividade(self, tema, descricao, vagas, duracao, sala, data, hora_inicio, hora_fim):

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
            self.find_element(self.sala).send_keys(sala)
            self.find_element(self.data).send_keys(data)
            self.find_element(self.hora_inicio).send_keys(hora_inicio)
            self.find_element(self.hora_fim).send_keys(hora_fim)
            self.find_element(self.botao_adicionar).click()
            self.find_element(self.botao_salvar).click()
            # RESPONSAVEL
            self.find_element(self.combo_palestrante).click()
            self.find_element(self.palestrante).click()

            #self.find_element(self.salvar).click()

            print('\n CT_01 sem erros: o evento foi criado com sucesso')

        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_01 reportou erro: " + str(e))