<div align="center">  <h1>💰 Controle Financeiro em Python</h1>  <p>
    Sistema de terminal para registrar receitas, gastos, calcular saldo e salvar dados localmente.
  </p>  <p>
    <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Status-Em%20desenvolvimento-F7B731?style=for-the-badge" alt="Status">
    <img src="https://img.shields.io/badge/Projeto-Controle%20Financeiro-2ECC71?style=for-the-badge" alt="Projeto">
    <img src="https://img.shields.io/badge/GitHub-Portf%C3%B3lio-181717?style=for-the-badge&logo=github" alt="GitHub">
  </p></div><hr><h2>📌 Sobre o projeto</h2><p>
  O <strong>Controle Financeiro em Python</strong> é uma aplicação de terminal criada para auxiliar no registro de receitas e gastos, permitindo calcular o saldo atual e manter os dados salvos em um arquivo local.
</p><p>
  O projeto simula uma funcionalidade comum em sistemas reais: o controle de entradas e saídas financeiras.
</p><p>
  A aplicação permite cadastrar valores, visualizar o saldo, remover registros e carregar automaticamente os dados salvos ao iniciar o programa.
</p><hr><h2>🎯 Objetivo</h2><p>
  O objetivo do projeto é criar um sistema simples, funcional e organizado para aplicar conceitos fundamentais de programação em Python.
</p><ul>
  <li>Registrar valores de entrada.</li>
  <li>Registrar valores de saída.</li>
  <li>Calcular o saldo final.</li>
  <li>Salvar dados em arquivo local.</li>
  <li>Carregar dados salvos automaticamente.</li>
  <li>Permitir a exclusão de registros cadastrados.</li>
</ul><hr><h2>🚀 Funcionalidades</h2><ul>
  <li>Cadastrar receitas.</li>
  <li>Cadastrar gastos.</li>
  <li>Visualizar o saldo atual.</li>
  <li>Identificar se o saldo está positivo, zerado ou negativo.</li>
  <li>Apagar receitas cadastradas.</li>
  <li>Apagar gastos cadastrados.</li>
  <li>Salvar os dados localmente em arquivo <code>.txt</code>.</li>
  <li>Carregar os dados salvos ao abrir o programa.</li>
  <li>Utilizar um menu interativo no terminal.</li>
</ul><hr><h2>🧠 Conceitos aplicados</h2><p>
  Durante o desenvolvimento deste projeto, foram aplicados conceitos fundamentais de Python para construir um sistema funcional de controle financeiro.
</p><h3>🔹 Estruturas de dados</h3><ul>
  <li>
    <strong>Listas:</strong> utilizadas para armazenar separadamente os valores de receitas e gastos.
  </li>
</ul><h3>🔹 Entrada e conversão de dados</h3><ul>
  <li>
    <strong>input():</strong> usado para receber as opções do menu e os valores digitados pelo usuário.
  </li>
  <li>
    <strong>float():</strong> usado para converter os valores digitados em números decimais.
  </li>
</ul><h3>🔹 Controle de fluxo</h3><ul>
  <li>
    <strong>if / elif / else:</strong> utilizados para verificar qual opção foi escolhida no menu.
  </li>
  <li>
    <strong>while:</strong> utilizado para manter o programa em execução até o usuário escolher sair.
  </li>
</ul><h3>🔹 Cálculos</h3><ul>
  <li>
    <strong>sum():</strong> utilizado para somar todos os valores cadastrados nas listas de receitas e gastos.
  </li>
</ul><h3>🔹 Manipulação de arquivos</h3><ul>
  <li>
    <strong>open():</strong> utilizado para abrir o arquivo responsável por salvar e carregar os dados.
  </li>
  <li>
    <strong>Leitura de arquivos:</strong> permite carregar os dados salvos quando o programa é iniciado.
  </li>
  <li>
    <strong>Escrita em arquivos:</strong> permite registrar novas receitas e novos gastos no arquivo <code>dados.txt</code>.
  </li>
</ul><h3>🔹 Tratamento de erros</h3><ul>
  <li>
    <strong>try / except:</strong> utilizado para evitar erro caso o arquivo <code>dados.txt</code> ainda não exista.
  </li>
</ul><h3>🔹 Remoção e listagem de dados</h3><ul>
  <li>
    <strong>enumerate():</strong> utilizado para exibir receitas e gastos com numeração.
  </li>
  <li>
    <strong>pop():</strong> utilizado para remover uma receita ou um gasto escolhido pelo usuário.
  </li>
</ul><h3>🔹 Versionamento</h3><ul>
  <li>
    <strong>Git:</strong> utilizado para registrar as alterações feitas no projeto.
  </li>
  <li>
    <strong>GitHub:</strong> utilizado para hospedar o código e apresentar o projeto no portfólio.
  </li>
</ul><hr><h2>🛠️ Tecnologias utilizadas</h2><div align="center">  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></div><hr><h2>⚙️ Como funciona</h2><p>
  O sistema utiliza duas listas principais: uma para armazenar as receitas e outra para armazenar os gastos.
</p><p>
  Quando o programa é iniciado, ele tenta abrir o arquivo <code>dados.txt</code>. Caso o arquivo exista, o sistema lê cada linha, identifica se ela representa uma receita ou um gasto e carrega o valor para a lista correspondente.
</p><p>
  Durante a execução, o usuário escolhe uma opção no menu. Ao cadastrar uma nova receita ou um novo gasto, o valor é adicionado à lista correta e também registrado no arquivo <code>dados.txt</code>.
</p><p>
  Para calcular o saldo, o programa soma todos os valores da lista de receitas, soma todos os valores da lista de gastos e subtrai os gastos das receitas.
</p><p>
  Quando um registro é apagado, ele é removido da lista correspondente. Depois disso, o arquivo <code>dados.txt</code> é reescrito com os dados atualizados, evitando que informações apagadas continuem salvas.
</p><hr><h2>💾 Armazenamento dos dados</h2><p>
  O programa salva os dados localmente no arquivo <code>dados.txt</code>. Esse arquivo é gerado durante o uso do sistema e fica apenas no ambiente local do usuário.
</p><p>
  No repositório, existe o arquivo <code>dados_exemplo.txt</code>, que mostra um exemplo de como os dados são armazenados.
</p><p>Exemplo de estrutura dos dados:</p><pre><code>RECEITA - 100.0
GASTO - 30.0
RECEITA - 50.0</code></pre><p>
  Ao iniciar o programa, cada linha é lida e separada. O sistema identifica se o registro é uma receita ou um gasto, converte o valor para número decimal e adiciona o valor na lista correta.
</p><hr><h2>📂 Estrutura do projeto</h2><pre><code>controle-financeiro-python/
│
├── controledegastos.py
├── dados_exemplo.txt
├── .gitignore
└── README.md</code></pre><hr><h2>▶️ Como executar</h2><p>Clone o repositório:</p><pre><code>git clone https://github.com/m4rcusgollub/controle-financeiro-python.git</code></pre><p>Entre na pasta do projeto:</p><pre><code>cd controle-financeiro-python</code></pre><p>Execute o arquivo principal:</p><pre><code>python controledegastos.py</code></pre><p>Ou:</p><pre><code>python3 controledegastos.py</code></pre><hr><h2>📈 Melhorias futuras</h2><ul>
  <li>Adicionar descrição para cada receita e gasto.</li>
  <li>Criar histórico completo de movimentações.</li>
  <li>Adicionar categorias para os registros.</li>
  <li>Melhorar a formatação dos valores em reais.</li>
  <li>Organizar o código usando funções.</li>
  <li>Salvar os dados em formato JSON.</li>
  <li>Criar relatórios mensais.</li>
  <li>Adicionar tratamento para entradas inválidas.</li>
  <li>Criar uma interface gráfica futuramente.</li>
</ul><hr><h2>📚 Aprendizados</h2><p>
  Durante o desenvolvimento deste projeto, foram praticados conceitos fundamentais de programação em Python, como listas, condicionais, laços de repetição, manipulação de arquivos e versionamento com Git.
</p><p>
  O projeto também ajudou a entender como sistemas simples podem salvar, carregar, calcular e modificar dados de forma persistente.
</p><hr><h2>📌 Status do projeto</h2><p>
  Projeto em desenvolvimento. Novas funcionalidades e melhorias serão adicionadas conforme a evolução do sistema.
</p><hr><div align="center">  <h2>👨‍💻 Autor</h2>  <p>
    Desenvolvido por <strong>Marcus Gollub</strong>
  </p>  <p>
    <a href="https://github.com/m4rcusgollub">
      GitHub: @m4rcusgollub
    </a>
  </p></div></p><p>
  O projeto simula uma funcionalidade comum em sistemas reais: o controle de entradas e saídas financeiras.
</p><p>
  A aplicação permite cadastrar valores, visualizar o saldo, remover registros e carregar automaticamente os dados salvos ao iniciar o programa.
</p><hr><h2>🎯 Objetivo</h2><p>
  O objetivo do projeto é criar um sistema simples, funcional e organizado para aplicar conceitos fundamentais de programação em Python.
</p><ul>
  <li>Registrar valores de entrada.</li>
  <li>Registrar valores de saída.</li>
  <li>Calcular o saldo final.</li>
  <li>Salvar dados em arquivo local.</li>
  <li>Carregar dados salvos automaticamente.</li>
  <li>Permitir a exclusão de registros cadastrados.</li>
</ul><hr><h2>🚀 Funcionalidades</h2><ul>
  <li>Cadastrar receitas.</li>
  <li>Cadastrar gastos.</li>
  <li>Visualizar o saldo atual.</li>
  <li>Identificar se o saldo está positivo, zerado ou negativo.</li>
  <li>Apagar receitas cadastradas.</li>
  <li>Apagar gastos cadastrados.</li>
  <li>Salvar os dados localmente em arquivo <code>.txt</code>.</li>
  <li>Carregar os dados salvos ao abrir o programa.</li>
  <li>Utilizar um menu interativo no terminal.</li>
</ul><hr><h2>🧠 Conceitos aplicados</h2><p>
  Durante o desenvolvimento deste projeto, foram aplicados conceitos fundamentais de Python para construir um sistema funcional de controle financeiro.
</p><h3>🔹 Estruturas de dados</h3><ul>
  <li>
    <strong>Listas:</strong> utilizadas para armazenar separadamente os valores de receitas e gastos.
  </li>
</ul><h3>🔹 Entrada e conversão de dados</h3><ul>
  <li>
    <strong>input():</strong> usado para receber as opções do menu e os valores digitados pelo usuário.
  </li>
  <li>
    <strong>float():</strong> usado para converter os valores digitados em números decimais.
  </li>
</ul><h3>🔹 Controle de fluxo</h3><ul>
  <li>
    <strong>if / elif / else:</strong> utilizados para verificar qual opção foi escolhida no menu.
  </li>
  <li>
    <strong>while:</strong> utilizado para manter o programa em execução até o usuário escolher sair.
  </li>
</ul><h3>🔹 Cálculos</h3><ul>
  <li>
    <strong>sum():</strong> utilizado para somar todos os valores cadastrados nas listas de receitas e gastos.
  </li>
</ul><h3>🔹 Manipulação de arquivos</h3><ul>
  <li>
    <strong>open():</strong> utilizado para abrir o arquivo responsável por salvar e carregar os dados.
  </li>
  <li>
    <strong>Leitura de arquivos:</strong> permite carregar os dados salvos quando o programa é iniciado.
  </li>
  <li>
    <strong>Escrita em arquivos:</strong> permite registrar novas receitas e novos gastos no arquivo <code>dados.txt</code>.
  </li>
</ul><h3>🔹 Tratamento de erros</h3><ul>
  <li>
    <strong>try / except:</strong> utilizado para evitar erro caso o arquivo <code>dados.txt</code> ainda não exista.
  </li>
</ul><h3>🔹 Remoção e listagem de dados</h3><ul>
  <li>
    <strong>enumerate():</strong> utilizado para exibir receitas e gastos com numeração.
  </li>
  <li>
    <strong>pop():</strong> utilizado para remover uma receita ou um gasto escolhido pelo usuário.
  </li>
</ul><h3>🔹 Versionamento</h3><ul>
  <li>
    <strong>Git:</strong> utilizado para registrar as alterações feitas no projeto.
  </li>
  <li>
    <strong>GitHub:</strong> utilizado para hospedar o código e apresentar o projeto no portfólio.
  </li>
</ul><hr><h2>🛠️ Tecnologias utilizadas</h2><div align="center">  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></div><hr><h2>⚙️ Como funciona</h2><p>
  O sistema utiliza duas listas principais: uma para armazenar as receitas e outra para armazenar os gastos.
</p><p>
  Quando o programa é iniciado, ele tenta abrir o arquivo <code>dados.txt</code>. Caso o arquivo exista, o sistema lê cada linha, identifica se ela representa uma receita ou um gasto e carrega o valor para a lista correspondente.
</p><p>
  Durante a execução, o usuário escolhe uma opção no menu. Ao cadastrar uma nova receita ou um novo gasto, o valor é adicionado à lista correta e também registrado no arquivo <code>dados.txt</code>.
</p><p>
  Para calcular o saldo, o programa soma todos os valores da lista de receitas, soma todos os valores da lista de gastos e subtrai os gastos das receitas.
</p><p>
  Quando um registro é apagado, ele é removido da lista correspondente. Depois disso, o arquivo <code>dados.txt</code> é reescrito com os dados atualizados, evitando que informações apagadas continuem salvas.
</p><hr><h2>💾 Armazenamento dos dados</h2><p>
  Os dados são armazenados no arquivo <code>dados.txt</code>, usando um formato simples de texto.
</p><p>Exemplo:</p><pre><code>RECEITA - 100.0
GASTO - 30.0
RECEITA - 50.0</code></pre><p>
  Ao iniciar o programa, cada linha é lida e separada. O sistema identifica se o registro é uma receita ou um gasto, converte o valor para número decimal e adiciona o valor na lista correta.
</p><hr><h2>📂 Estrutura do projeto</h2><pre><code>controle-financeiro-python/
│
├── main.py
├── dados.txt
└── README.md</code></pre><hr><h2>▶️ Como executar</h2><p>Clone o repositório:</p><pre><code>git clone https://github.com/m4rcusgollub/controle-financeiro-python.git</code></pre><p>Entre na pasta do projeto:</p><pre><code>cd controle-financeiro-python</code></pre><p>Execute o arquivo principal:</p><pre><code>python main.py</code></pre><p>Ou:</p><pre><code>python3 main.py</code></pre><hr><h2>📈 Melhorias futuras</h2><ul>
  <li>Adicionar descrição para cada receita e gasto.</li>
  <li>Criar histórico completo de movimentações.</li>
  <li>Adicionar categorias para os registros.</li>
  <li>Melhorar a formatação dos valores em reais.</li>
  <li>Organizar o código usando funções.</li>
  <li>Salvar os dados em formato JSON.</li>
  <li>Criar relatórios mensais.</li>
  <li>Adicionar tratamento para entradas inválidas.</li>
  <li>Criar uma interface gráfica futuramente.</li>
</ul><hr><h2>📚 Aprendizados</h2><p>
  Durante o desenvolvimento deste projeto, foram praticados conceitos fundamentais de programação em Python, como listas, condicionais, laços de repetição, manipulação de arquivos e versionamento com Git.
</p><p>
  O projeto também ajudou a entender como sistemas simples podem salvar, carregar, calcular e modificar dados de forma persistente.
</p><hr><h2>📌 Status do projeto</h2><p>
  Projeto em desenvolvimento. Novas funcionalidades e melhorias serão adicionadas conforme a evolução do sistema.
</p><hr><div align="center">  <h2>👨‍💻 Autor</h2>  <p>
    Desenvolvido por <strong>Marcus Gollub</strong>
  </p>  <p>
    <a href="https://github.com/m4rcusgollub">
      GitHub: @m4rcusgollub
    </a>
  </p></div>
