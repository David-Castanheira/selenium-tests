import os 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.common.by import By

# Inicializa o driver do navegador
chrome = Chrome()

# Informa o caminho/diretório do projeto
local_path = f'file://{os.path.dirname(os.path.realpath(__file__))}'

# Ação que inicializa o template no Chrome
chrome.get(f'{local_path}/templates/exercicio01.html')

# Recupera o título da página definido no arquivo HTML
titulo = chrome.title
print(titulo)

# Recupera o parágrafo
paragrafo_tag = chrome.find_element(By.TAG_NAME, 'p')
print(paragrafo_tag.text)

# Recupera a tag HTML definida no arquivo HTML
paragrafo_css = chrome.find_element(By.CSS_SELECTOR, 'p.content')
print(paragrafo_css.text)
