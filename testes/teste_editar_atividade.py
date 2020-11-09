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
editar_atividade.caminho(True)
editar_atividade.ct16_editar_atividade(
    tema        = 'editar ativividade teste ct16',
    descricao   = 'teste editar atividade',
    vagas       = '34',
    duracao     = '4',
    sala        = '100',
    data        = '12/12/2020',
    hora_inicio = '1000',
    hora_fim    = '1400'
)
# ----------- Casos de teste: Exclusão de atividade --------------#
webdriver.get(url)
editar_atividade.caminho(False, True, False)
editar_atividade.ct17_editar_atividade()

# -------------- Casos de teste: Cancelar edição -----------------#
webdriver.get(url)
editar_atividade.caminho()
editar_atividade.ct18_editar_atividade()

# --- Casos de teste: Nenhuma atividade selecionada ao editar ----#
webdriver.get(url)
editar_atividade.caminho(False, False, True)
editar_atividade.ct19_editar_atividade()

# ----- Casos de teste: Campos obrigatórios não preenchidos ------#
webdriver.get(url)
editar_atividade.caminho()
editar_atividade.ct20_editar_atividade(
    tema        = 'teste editar campos obrigatorios ct20',
    descricao   = 'teste editar campos obrigatorios',
    vagas       = '60',
    duracao     = '7',
    local       = 'ICE',
    sala        = '110',
    data        = '12/12/2020',
    hora_inicio = '0800',
    hora_fim    = '1500'
)
# ---------------- Casos de teste: Data inválida -----------------#
webdriver.get(url)
editar_atividade.caminho()
editar_atividade.ct21_editar_atividade(
    sala        = '10',
    data        = '12/12/2005',
    hora_inicio = '1000',
    hora_fim    = '1400'
)
# ---------------- Casos de teste: Hora inválida -----------------#
webdriver.get(url)
editar_atividade.caminho()
editar_atividade.ct22_editar_atividade(
    sala        = '10',
    data        = '13/12/2020',
    hora_inicio = '0800',
    hora_fim    = '0900'
)