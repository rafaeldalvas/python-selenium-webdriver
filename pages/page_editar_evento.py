from selenium.webdriver.common.by import By
from utils.config import PageElement
from time import sleep

class editarEvento(PageElement):
    # CAMINHO
    calendario = (By.CSS_SELECTOR, "i.fa-calendar")
    admin = (By.CSS_SELECTOR, "a[href$='admEvento/inicial.zul?']")
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
    # FIM COMBOBOX
    inscricao_externa = (By.ID, 'zk-comp-190!real') # Selecionar - Não
    evento_pago_aluno = (By.ID, 'zk-comp-195!real') # Desmarcar o campo "Aluno"
    evento_pago_externo = (By.ID, 'zk-comp-196!real') # Marcar o campo "Externo"

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
    certificado = (By.CSS_SELECTOR, 'tr[id$="comp-272"] [class="z-combo-item-text"]')  # OPÇÃO PADRAO ICE 2

    combo_assinatura1 = (By.ID, "zk-comp-238!btn")
    assinatura1 = (By.CSS_SELECTOR, 'tr[id$="comp-301"] [class="z-combo-item-text"]')
    funcao1 = (By.ID, "zk-comp-242")

    combo_assinatura2 = (By.ID, "zk-comp-247!btn")
    assinatura2 = (By.CSS_SELECTOR, 'tr[id$="comp-325"] [class="z-combo-item-text"]')
    funcao2 = (By.ID, "zk-comp-251")

    combo_assinatura3 = (By.ID, "zk-comp-256!btn")
    assinatura3 = (By.CSS_SELECTOR, 'tr[id$="comp-382"] [class="z-combo-item-text"]')
    funcao3 = (By.ID, "zk-comp-260")

    btn_salvar = (By.CSS_SELECTOR, 'table[id$="comp-263!box"] [class$="button-cm"]')
    btn_ok = (By.CSS_SELECTOR, 'table[id$="comp-403!box"] [class$="button-cm"]')

    # CONCLUIR
    btn_enviar = (By.CSS_SELECTOR, 'table[id$="comp-199!box"] [class$="button-cm"]')

    # EXCLUIR EVENTO
    btn_excluir = (By.CSS_SELECTOR, 'table[id$="zk-comp-136!box"] [class$="z-button-cm"]')

    # CANCELAR
    btn_cancelar = (By.CSS_SELECTOR, 'table[id$="comp-201!box"] [class$="button-cm"]')




    def caminho(self, ct_08 = False, ct_10 = False):
        sleep(1)
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
        sleep(2)
        if ct_08 is False:
            self.find_element(self.btn_editar).click()

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
        # self.sendKeys(Keys.RETURN)
        # sleep(1)
        self.find_element(self.nome_responsavel).send_keys(nome_responsavel)
        self.find_element(self.btn_pesquisar_responsavel).click()
        self.find_element(self.checkbox_responsavel).click()
        self.find_element(self.seleciona_nome).click()
        self.find_element(self.btn_confirma_responsavel).click()

    # --------- Caso de teste: Edição de evento padrão -------------#
    def ct_07_editar_evento(self,nome, descricao, site, email_responsavel, inicio_evento, fim_evento, inicio_inscricao,
                          fim_inscricao, funcao1, funcao2, funcao3, nome_responsavel):
        sleep(1)
        self.find_element(self.nome).send_keys(nome)
        self.find_element(self.descricao).send_keys(descricao)
        self.find_element(self.site).send_keys(site)
        self.find_element(self.email_responsavel).send_keys(email_responsavel)

        # CERTIFICADO
        self.preenche_certificado(funcao1, funcao2, funcao3)
        # FIM CERTIFICADO

        # RESPONSAVEL
        self.preenche_responsavel(nome_responsavel) # DA ERRO DE JS AQUI
        # FIM RESPONSAVEL

        self.find_element(self.inicio_evento).send_keys(inicio_evento)
        self.find_element(self.fim_evento).send_keys(fim_evento)
        self.find_element(self.inicio_inscricao).send_keys(inicio_inscricao)
        self.find_element(self.fim_inscricao).send_keys(fim_inscricao)

        # TIPO DE EVENTO
        self.find_element(self.btn_tipo_evento).click()
        self.find_element(self.tipo_evento).click()
        # FIM TIPO DE EVENTO

        self.find_element(self.inscricao_externa).click()
        self.find_element(self.evento_pago_aluno).click()
        self.find_element(self.evento_pago_externo).click()

        #self.find_element(self.btn_enviar).click()
        sleep(1)


# --------- Caso de teste: Exclusão de eventos -------------#
    def ct_08_editar_evento(self):
        self.find_element(self.btn_excluir).click()

# --------- Caso de teste: Cancelar transação -------------#
    def ct_09_editar_evento(self, nome, descricao):
        sleep(1)
        self.find_element(self.nome).send_keys(nome)
        self.find_element(self.descricao).send_keys(descricao)
        self.find_element(self.btn_cancelar).click()

# --------- Caso de teste: Nenhum evento selecionado ao editar -------------#
    def ct_10_editar_evento(self, ct_10):
        self.caminho(False, ct_10)

# --------- Caso de teste: Campos obrigatórios não preenchidos -------------#
    def ct_11_editar_evento(self):
        self.find_element(self.nome).send_keys('')
        self.find_element(self.descricao).send_keys('')
        #self.find_element(self.btn_enviar).click()
