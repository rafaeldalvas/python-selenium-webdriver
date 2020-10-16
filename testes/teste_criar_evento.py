from selenium import webdriver
from utils.config import PageElement
from pages.page_criar_evento import criarEvento
from utils.login import LoginProfessor

webdriver = webdriver.Chrome(r'd:\Downloads\chromedriver_win32\chromedriver.exe')

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login(
    login='testes.professor',
    senha='6kmfDK'
)

criar_evento = criarEvento(webdriver)

criar_evento.caminho()
criar_evento.ct01_criar_evento(
    nome = 'Evento teste',
    descricao = 'testando evento',
    site = 'teste.com.br',
    email_responsavel = 'teste@teste.com',
    inicio_evento = '22/12/2020',
    fim_evento = '01/01/2020',
    inicio_inscricao = '16/10/2020',
    fim_inscricao = '20/12/2020',
    funcao1 = 'Professor',
    funcao2 = 'Gerente',
    funcao3 = 'Diretor',
    nome_pesquisa_responsavel = 'Raquel Alves da Silva'
)








