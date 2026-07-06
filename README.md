<div align="center">

# 💰 Controle Financeiro em Python

Sistema de controle financeiro desenvolvido em Python, com versão de terminal e versão web simples usando Flask.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-111827?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)

</div>

---

## 📌 Sobre o projeto

Este projeto foi criado para praticar conceitos fundamentais de programação e desenvolvimento backend com Python.

A primeira versão funcionava diretamente no terminal, permitindo cadastrar receitas, gastos, visualizar saldo e apagar movimentações.

Depois, o projeto evoluiu para uma aplicação web simples utilizando Flask, mantendo a mesma lógica principal, mas adicionando rotas, formulários HTML, templates e persistência de dados em JSON.

O foco principal do projeto é o aprendizado de backend, organização de dados e manipulação de informações.

---

## 🚀 Funcionalidades

- Adicionar receitas
- Adicionar gastos
- Visualizar saldo atual
- Ver total de receitas
- Ver total de gastos
- Listar histórico de movimentações
- Apagar movimentações
- Salvar dados localmente em JSON
- Utilizar interface web simples com Flask

---

## 🧠 Conceitos praticados

- Variáveis
- Listas
- Dicionários
- Funções
- Condicionais
- Laços de repetição
- Manipulação de arquivos
- JSON
- Rotas com Flask
- Métodos HTTP GET e POST
- Templates HTML
- Separação básica entre backend, templates e arquivos estáticos
- Git e GitHub

---

## 🛠️ Tecnologias utilizadas

- Python
- Flask
- HTML
- CSS
- JSON
- Git
- GitHub

---

## 📁 Estrutura do projeto

```text
controle-financeiro-python/
├── app.py
├── controledegastos.py
├── dados_exemplo.json
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
```

---

## 🖥️ Versão terminal

O arquivo `controledegastos.py` contém a primeira versão do sistema, executada diretamente pelo terminal.

Essa versão permite adicionar receitas, adicionar gastos, visualizar saldo e apagar registros usando menus no próprio terminal.

Para executar:

```bash
python controledegastos.py
```

Ou:

```bash
python3 controledegastos.py
```

---

## 🌐 Versão web com Flask

O arquivo `app.py` contém a versão web do sistema.

Essa versão utiliza Flask para criar rotas, receber dados de formulários e exibir as informações em uma página HTML.

Para instalar as dependências:

```bash
pip install -r requirements.txt
```

Para executar o projeto:

```bash
python app.py
```

Ou:

```bash
python3 app.py
```

Depois, acesse no navegador:

```text
http://127.0.0.1:5000
```

---

## 💾 Armazenamento dos dados

Os dados do sistema são salvos localmente no arquivo:

```text
dados.json
```

Esse arquivo não é enviado para o GitHub, pois pode conter informações pessoais do usuário, como receitas, gastos, categorias e valores.

Para demonstrar o formato esperado dos dados, o projeto possui o arquivo:

```text
dados_exemplo.json
```

Exemplo de estrutura:

```json
[
  {
    "tipo": "receita",
    "descricao": "Salário",
    "categoria": "Trabalho",
    "valor": 1000.0
  },
  {
    "tipo": "gasto",
    "descricao": "Mercado",
    "categoria": "Alimentação",
    "valor": 80.0
  }
]
```

---

## ⚙️ Como executar o projeto

Clone o repositório:

```bash
git clone https://github.com/m4rcusgollub/controle-financeiro-python.git
```

Entre na pasta do projeto:

```bash
cd controle-financeiro-python
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação web:

```bash
python app.py
```

Acesse no navegador:

```text
http://127.0.0.1:5000
```

---

## 📌 Objetivo do projeto

O objetivo deste projeto não é criar uma interface visual complexa, mas sim praticar fundamentos importantes para desenvolvimento backend.

O projeto trabalha com entrada de dados, processamento de informações, persistência local, organização de código e criação de rotas web com Flask.

---

## 🔮 Melhorias futuras

- Adicionar banco de dados SQLite
- Criar validações mais completas
- Separar melhor as responsabilidades do código
- Criar uma API REST
- Adicionar testes automatizados
- Melhorar a organização em camadas
- Recriar futuramente o projeto em Java com Spring Boot

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, foram praticados conceitos importantes de lógica de programação, manipulação de arquivos, estruturação de dados, criação de funções e introdução ao desenvolvimento backend com Flask.

O projeto também serviu para praticar o uso de Git, GitHub, commits, `.gitignore` e organização de repositório.

---

## 👨‍💻 Autor

Desenvolvido por **Marcus Gollub**.

GitHub: [m4rcusgollub](https://github.com/m4rcusgollub)

---

<div align="center">

Projeto desenvolvido como parte dos meus estudos em programação backend.

</div>
