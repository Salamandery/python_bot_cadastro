# 🤖 Python Bot de Cadastro

<p align="center">
  <img src="https://img.shields.io/pypi/v/pyautogui?label=pyautogui" alt="PyAutoGUI"/>
  <img src="https://img.shields.io/pypi/v/pandas?label=pandas" alt="pandas"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"/>
</p>

Automatize o cadastro de produtos em sistemas web a partir de uma base de dados CSV, utilizando automação de mouse e teclado com Python.

---

## 📑 Sumário
- [✨ Visão Geral](#-visão-geral)
- [🛠️ Tecnologias e Bibliotecas](#️-tecnologias-e-bibliotecas)
- [📐 Padrões de Projeto](#-padrões-de-projeto)
- [⚙️ Setup e Instalação](#️-setup-e-instalação)
- [🚀 Configuração e Uso](#-configuração-e-uso)
- [👤 Autor](#-autor)

---

## ✨ Visão Geral
Este projeto é um bot em Python que automatiza o preenchimento de formulários web para cadastro de produtos, lendo dados de um arquivo CSV e interagindo com o navegador via comandos de mouse e teclado.

## 🛠️ Tecnologias e Bibliotecas
- **Python 3.7+**
- [PyAutoGUI](https://pypi.org/project/pyautogui/): Automação de mouse e teclado
- [pandas](https://pypi.org/project/pandas/): Manipulação e leitura de arquivos CSV

## 📐 Padrões de Projeto
- **Script Procedural:** Ideal para automações simples e diretas
- **Separação de Responsabilidades:** Leitura de dados e automação de interface em arquivos distintos

## ⚙️ Setup e Instalação
```bash
# Clone o repositório
$ git clone https://github.com/seu-usuario/python_bot_cadastro.git
$ cd python_bot_cadastro

# Instale as dependências
$ pip install pyautogui pandas
```

## 🚀 Configuração e Uso
1. Edite o arquivo `produtos.csv` com os dados dos produtos a serem cadastrados.
2. Ajuste as coordenadas de clique no script conforme a resolução/tela do seu computador, se necessário.
3. Execute o script principal:
   ```bash
   python codigo.py
   ```
4. O bot abrirá o navegador, acessará o site de cadastro e preencherá os campos automaticamente.

> **Atenção:** Não mova o mouse ou utilize o teclado durante a execução do bot para evitar interferências.

---

## 👤 Autor
by **Rodolfo M. F. Abreu**