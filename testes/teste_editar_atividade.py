from selenium import webdriver
from pages.page_editar_atividade import editarAtividade
from utils.login import LoginProfessor

webdriver = webdriver.Chrome(r'd:\Downloads\chromedriver_win32\chromedriver.exe')

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login(
    login = 'testes.professor',
    senha = '6kmfDK'
)

editar_atividade = editarAtividade(webdriver)

# -------- Casos de teste: Edição de atividade padrão ------------#
webdriver.get(url)
editar_atividade.caminho()
editar_atividade.ct16_editar_atividade(
    tema        = 'ativividade teste ct11',
    descricao   = 'teste nova atividade',
    vagas       = '30',
    duracao     = '8',
    sala        = '101',
    data        = '12/12/2020',
    hora_inicio = '1000',
    hora_fim    = '1800'
)
# ----------- Casos de teste: Exclusão de atividade --------------#
webdriver.get(url)
editar_atividade.caminho(True)
editar_atividade.ct17_editar_atividade()

# -------------- Casos de teste: Cancelar edição -----------------#
# --- Casos de teste: Nenhuma atividade selecionada ao editar ----#
# ----- Casos de teste: Campos obrigatórios não preenchidos ------#
# ---------------- Casos de teste: Data inválida -----------------#