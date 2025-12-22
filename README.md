

---

# 📌 Sistema de Cadastro e Login em Python

Este projeto é um **sistema simples de cadastro, login e gerenciamento de contas**, feito em **Python**, utilizando **arquivos `.txt`** para armazenar usuários, senhas e registros de login/logout.

O objetivo do projeto é praticar:

* Manipulação de arquivos
* Estruturas de decisão e repetição
* Funções
* Lógica de autenticação básica

---

## ⚙️ Funcionalidades

* ✅ Registrar novos usuários
* ✅ Verificar se o usuário já existe
* ✅ Login com usuário e senha
* ✅ Limite de tentativas para troca de senha
* ✅ Alteração de senha após login
* ✅ Exibição de informações da conta
* ✅ Registro de login e logout com **data e hora**
* ✅ Menu interativo no terminal

---

## 📂 Arquivos gerados pelo sistema

* **`LogEntrada.txt`**

  * Armazena usuários e senhas no formato:

    ```
    usuario;senha
    ```

* **`LogLogout.txt`**

  * Registra logins e logouts com data e hora:

    ```
    usuario Logou - data - hora
    usuario Logout - data - hora
    ```

---

## ▶️ Como executar o projeto

1. Certifique-se de ter o **Python 3** instalado
2. Clone o repositório ou baixe os arquivos
3. No terminal, execute:

   ```bash
   python nome_do_arquivo.py
   ```
4. Use o menu para:

   * Registrar conta
   * Logar
   * Alterar senha
   * Ver informações
   * Sair

---

## 🧠 Observações importantes

* As senhas **não são criptografadas** (uso educacional)
* O sistema usa arquivos `.txt`, não banco de dados
* Ideal para **estudo e prática**, não para produção

---

## 🚀 Possíveis melhorias futuras

* 🔒 Criptografia de senhas
* 🗄️ Uso de banco de dados (SQLite)
* 👤 Sistema de níveis de usuário
* 🖥️ Interface gráfica
* 📧 Recuperação de senha

---

## 📚 Tecnologias utilizadas

* Python 3
* Módulos:

  * `os`
  * `datetime`

---

## ✍️ Autor

**Naldo Silva**
Projeto desenvolvido para fins de aprendizado em programação Python.

---



