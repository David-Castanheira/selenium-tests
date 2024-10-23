import pytest 
from actions import titulo, paragrafo_tag, paragrafo_css

def test_recuperar_titulo():
    assert titulo == 'Exercicio 1'

def test_recuperar_paragrafo():
    assert paragrafo_tag.text == 'O conteudo do site vem aqui'

def test_recuperar_tag_paragrafo():
    assert paragrafo_css.text == 'O conteudo do site vem aqui'