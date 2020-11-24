from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from utils.config import PageElement

class inscricao(PageElement):
    #CAMINHO
    calendario = (By.CSS_SELECTOR, "i.fa-calendar")
    menu_evento = (By.CSS_SELECTOR, "a[href$='inicial.zul?pag=listaEventos']")
    mais_info = (By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/div/div[2]/div["
                           "1]/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td/div/div[1]/div/div[2]/div["
                           "1]/div/div/div/span/table/tbody/tr[3]/td[2]")
    skip = (By.ID, "zk-comp-137!tb_l")
    mais_info_vencido = (By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/div/div[2]/div["
                                   "1]/div/div/div/div/div/div/div/div/table/tbody/tr[23]/td/div/div[1]/div/div["
                                   "2]/div[1]/div/div/div/span/table")

    # CASOS DE TESTE
    atividade = (By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/div/div[2]/div["
                           "1]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[1]/div/div/div/div[3]/div["
                           "2]/table/tbody[2]/tr[3]/td[7]/div/table/tbody/tr/td/span/table/tbody/tr[1]/td[2]")

    atividade_vencida = (By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/div/div[2]/div["
                                   "1]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[1]/div/div/div/div[3]/div["
                                   "2]/table/tbody[2]/tr[2]/td[3]/div/table/tbody/tr/td/span/table/tbody/tr[2]/td[2]")

    horario_indisp_atividade_1 = (By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/div/div[2]/div["
                                            "1]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[1]/div/div/div/div["
                                            "3]/div[2]/table/tbody[2]/tr[4]/td[7]/div/table/tbody/tr["
                                            "1]/td/span/table/tbody/tr[2]/td[2]")

    horario_indisp_atividade_2 = (By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/div/div[2]/div["
                                            "1]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[1]/div/div/div/div["
                                            "3]/div[2]/table/tbody[2]/tr[4]/td[7]/div/table/tbody/tr["
                                            "3]/td/span/table/tbody/tr[2]/td[2]")

    reenviar_inscricao = (By.XPATH, '/html/body/div/div/div/div/div[2]/div[2]/div/div[2]/div['
                                    '1]/div/div/div/div/div/div/div/div[3]/table/tbody/tr/td/div/table['
                                    '1]/tbody/tr/td/span/table')
    inscrever_se = (By.ID, "zk-comp-158!box")
    inscritos = (By.ID, "zk-comp-162!box")
    voltar = (By.ID, "zk-comp-164!box")

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

    def caminho(self, vencido = False):
        sleep(2)
        self.find_element(self.calendario).click()
        sleep(1)
        self.find_element(self.menu_evento).click()
        sleep(1)
        if vencido is False:
            self.find_element(self.mais_info).click()
        else:
            self.find_element(self.mais_info_vencido).click()
        sleep(1)
        if vencido is False:
            self.find_element(self.skip).click()

# ------------ Caso de teste: Inscrição padrão  ---------------#
    def ct40_inscricao(self):
        try:
            sleep(1)
            self.find_element(self.atividade).click()
            sleep(1)
            self.find_element(self.inscrever_se).click()
            sleep(2)
            msg = self.espera_mensagem()
            if msg is True:
                self.find_element(self.btn_ok_alert).click()
                sleep(10)
                msgConfirmacao = self.espera_mensagem()
                if msgConfirmacao is True:
                    if self.find_element(self.alert_texto).text.find('Inscrição solicitada!') > -1:
                        print('\n CT_40 sem erros: a inscrição foi solicitada com sucesso')
                        assert True
                    else:
                        print("\n [!] CT_40 reportou erro: " + self.find_element(self.alert_texto).text)
                        assert False
                    self.find_element(self.btn_ok_alert).click()
                else:
                    print("\n [!] CT_40 reportou erro: a inscrição não foi solicitada")
                    assert False
        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_40 reportou erro: " + str(e))
            assert False
        except ElementClickInterceptedException:
            print("\n [!] CT_40 reportou erro: " + self.find_element(self.alert_texto).text)
            self.find_element(self.btn_ok_alert).click()
            assert False

# ------------ Prazo para inscrição vencido  ---------------#
    def ct41_inscricao(self):
        try:
            sleep(3)
            self.find_element(self.atividade_vencida).click()
            sleep(1)
            self.find_element(self.reenviar_inscricao).click()

            reenviar_inscricao = WebDriverWait(self.webdriver, poll_frequency=0.2, timeout=3)
            reenviar_inscricao.until(expected_conditions.element_to_be_clickable(self.reenviar_inscricao))
            if reenviar_inscricao is not None:
                self.find_element(self.reenviar_inscricao).click()
                if self.find_element(self.alert_texto).text.find('Inscrição solicitada!') > -1:
                    print('\n [!] CT_41 sem erro: a inscrição foi solicitada após o vencimento do prazo')
                    assert False
        except TimeoutException:
            assert True
            print('\n CT_41 reportou erro: tempo de inscrição para esta atividade terminou')

        except UnexpectedAlertPresentException as e:
            print("\n CT_41 reportou erro: " + str(e))
            assert True
        except NoSuchElementException:
            print("\n CT_41 reportou erro: tempo de inscrição para esta atividade terminou")
            assert True

# ------------ Ver Inscritos  ---------------#
    def ct42_inscricao(self):
        try:
            sleep(1)
            self.find_element(self.atividade).click()
            sleep(1)
            self.find_element(self.inscritos).click()
            sleep(1)
            url = self.webdriver.current_url
            if url.find('pag=listaInscritos') > 0:
                print('\n CT_42 sem erros: a lista de inscritos foi exibida')
                assert True
            else:
                print('\n [!] CT_42 reportou erro: a lista de inscritos não foi exibida')
                assert False
        except UnexpectedAlertPresentException as e:
            print("\n [!] CT_42 reportou erro: " + str(e))
            assert False
        except NoSuchElementException as e:
            print("\n [!] CT_42 reportou erro: a lista de inscritos não foi exibida")
            assert False
# ------------ Horário indisponível  ---------------#
    def ct43_inscricao(self):
        try:
            self.find_element(self.horario_indisp_atividade_1).click()
            sleep(1)
            self.find_element(self.inscrever_se).click()
            msg = self.espera_mensagem()
            if msg is True:
                self.find_element(self.btn_ok_alert).click()
            self.find_element(self.voltar).click()

            self.find_element(self.horario_indisp_atividade_2).click()
            self.find_element(self.inscrever_se).click()
            sleep(10)
            msg = self.espera_mensagem()
            if msg is True:
                self.find_element(self.btn_ok_alert).click()
                sleep(10)
                msgConfirmacao = self.espera_mensagem()
                if msgConfirmacao is True:
                    if self.find_element(self.alert_texto).text.find('Inscrição solicitada!') > -1:
                        print("\n [!] CT_43 reportou erro: a inscrição foi solicitada sendo que o usuário não possui horário disponível")
                        assert False
                    else:
                        print('\n CT_43 reportou erro: o sistema não permitiu a inscrição do usuário')
                        assert True
                    self.find_element(self.btn_ok_alert).click()
        except UnexpectedAlertPresentException as e:
            print("\n CT_43 reportou erro: " + str(e))
            assert True
        except NoSuchElementException as e:
            print("\n CT_43 reportou erro: usuário já inscrito na atividade")
            assert True

