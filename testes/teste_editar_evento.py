from selenium import webdriver
from pages.page_editar_evento import editarEvento
from utils.login import LoginProfessor

webdriver = webdriver.Chrome(r'd:\Downloads\chromedriver_win32\chromedriver.exe')

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login(
    login = 'testes.professor',
    senha = '6kmfDK'
)

editar_evento = editarEvento(webdriver)

# --------- Caso de teste: Edição de evento padrão -------------#
editar_evento.caminho()
editar_evento.ct_06_editar_evento(nome='Evento teste ct07 Alt', descricao='Alterando evento', site='alterei.com.br',
                                  email_responsavel='alterado@teste.com', inicio_evento='02/02/2021',
                                  fim_evento='16/02/2021', inicio_inscricao='02/01/2021', fim_inscricao='01/02/2021',
                                  funcao1='Professor Alterado', funcao2='Gerente Alterado', funcao3='Diretor Alterado',
                                  nome_responsavel='Raquel Alves da Silva')

# --------- Caso de teste: Exclusão de evento -------------#
editar_evento.clicarMain()
editar_evento.caminho(True)
editar_evento.ct_07_editar_evento()

# --------- Caso de teste: Cancelar transação -------------#
editar_evento.clicarMain()
editar_evento.caminho()
editar_evento.ct_08_editar_evento()

# --------- Caso de teste: Nenhum evento selecionado ao editar -------------#
editar_evento.clicarMain()
editar_evento.caminho(False, True)
editar_evento.ct_9_editar_evento()

# --------- Caso de teste: Campos obrigatórios não preenchidos -------------#
editar_evento.clicarMain()
editar_evento.caminho()
editar_evento.ct_10_editar_evento(nome='Evento teste ct07 Alt', descricao='Alterando evento',
                                  inicio_evento='02/02/2021', fim_evento='16/02/2021', inicio_inscricao='02/01/2021',
                                  fim_inscricao='01/02/2021', nome_responsavel='Raquel Alves da Silva')
