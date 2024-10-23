# Testes automatizados com Selenium 
Primeiros passos com testes automatizados na web com Selenium que servirá como atividade da disciplina de Automação de testes de software do 5° semestre do curso de ADS da Faculdade Impacta.

## Sobre o projeto
Este repositório apresenta meus primeiros passos com testes automatizados utilizando Selenium, na qual extrai elementos e cria ações em uma página HTML.

## Objetivo
Seja você um desenvolvedor experiente ou um iniciante, o objetivo deste guia é ajudar a entender a importância dos testes com alguns exercícios/exemplos de como implementá-los de forma eficaz em seus projetos.

## Introdução
O Selenium é um framework robusto e completo feito com o propósito de automatizar testes para aplicações web amplamente utilizado no mercado por empresas de tecnologia.

## Primeiros passos
Para começar, você precisará ter o Python instalado em sua máquina. Você pode verificar se o Python está instalado executando:

```
python --version
```

Se você não tiver o Python instalado em seu computador, pode baixá-lo no **[site oficial](https://www.python.org/downloads/)**.

Obs: A versão utilizada foi a 3.10, mas fique a vontade de utilizar a versão que mais se adequar e que preferir. Além disso, o framework unittest vem instalado juntamente com a linguagem Python

### Criação do ambiente virtual para desenvolvimento (Windows)
Durante este, foi-se criado um ambiente virtual, o que garante o desenvolvimento estável e consistente sem interferir em outros projetos ou no ambiente global. Para criá-lo e ativá-lo, execute os seguintes comandos:

```
python -m venv venv
venv\Scripts\Activate
```

Já no Linux:

```
python3 -m venv venv
source venv/bin/activate
```

## Pytest
Para se utilizar o Pytest para a execução dos testes, é necessário executar o comando abaixo:

```
pip install pytest
```
Após a estruturação dos testes (neste caso, localizados na raíz do projeto), execute o seguinte comando:

```
pytest nome_arquivo.py
```

## Selenium 
Nesta seção, abordaremos a instalação do selenium e também do webdriver para o gerenciamento automático dos navegadores com os comandos abaixo:  

```
pip install selenium
```

```
pip install webdriver-manager
```

Após isso, você pode utilizar essa poderosa ferramenta para a execução de testes da sua aplicação.

## Contribuindo
Contribuições são sempre bem-vindas! Se você tiver ideias para melhorar este repositório, sinta-se à vontade para abrir uma issue ou enviar um pull request.
