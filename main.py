from selenium import webdriver
from login import *

login_professor = loginProfessor(webdriver)

login_professor.realizaLogin(
    login = 'testes.professor',
    senha = '6kmfDK'
)
