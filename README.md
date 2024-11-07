
# Toro take-home test

Esta aplicação possui endpoints que permitem operações CRUD relativas ao desenvolvimento da US TORO-001: 
Eu, como investidor, gostaria de acessar a plataforma Toro usando minhas credenciais de usuário e senha, para que eu possa aprender mais, investir mais e acompanhar meus investimentos. 

Você pode executar esta aplicação em seu ambiente local.


## Descrição

Esta API foi construída com **FastAPI** para gerenciamento de usuários, incluindo funcionalidades de criação, leitura, atualização e exclusão de usuários. Além disso, inclui um endpoint de login simples onde é possível autenticar-se utilizando o e-mail e a senha.

#### Importante

os arquivos de configuração como .env estão presentes para facilitar a execução da aplicação ao clonar o repositório.

## Tecnologias Utilizadas

- **FastAPI** - Framework para a construção da API
- **SQLAlchemy** - ORM para interação com o banco de dados
- **Pydantic** - Para validação dos dados
- **SQLite** - Banco de dados utilizado para armazenar informações dos usuários
- **HTTP Status** - Utilizado para gerenciamento de respostas HTTP

## Endpoints

### 1. **GET /**
Retorna uma mensagem de boas-vindas.

- **Resposta:**  
  - **Status Code:** 200 OK
  - **Body:**  
    ```json
    {
      "message": "Hello World"
    }
    ```

---

### 2. **GET /users/**

Retorna uma lista de todos os usuários cadastrados.

- **Parâmetros:**
  - `skip` (opcional): Número de registros a serem pulados.
  - `limit` (opcional): Número máximo de registros a serem retornados.

- **Resposta:**  
  - **Status Code:** 200 OK  
  - **Body:**  
    ```json
    {
      "users": [
        {
          "id": 1,
          "username": "julia",
          "email": "julia@tamagno.com.br"
        }
      ]
    }
    ```

---

### 3. **POST /users/**

Cria um novo usuário com os dados fornecidos.

- **Parâmetros:**
  - `username`: Nome de usuário.
  - `email`: Endereço de e-mail.
  - `password`: Senha do usuário.

- **Resposta:**  
  - **Status Code:** 201 Created  
  - **Body:**  
    ```json
    {
      "id": 1,
      "username": "julia",
      "email": "julia@tamagno.com.br"
    }
    ```

---

### 4. **PUT /users/{user_id}**

Atualiza as informações de um usuário.

- **Parâmetros:**
  - `user_id`: ID do usuário a ser atualizado.
  - `username`: Novo nome de usuário.
  - `email`: Novo e-mail.
  - `password`: Nova senha.

- **Resposta:**  
  - **Status Code:** 200 OK  
  - **Body:**  
    ```json
    {
      "id": 1,
      "username": "maria",
      "email": "maria@test.com"
    }
    ```

---

### 5. **DELETE /users/{user_id}**

Deleta um usuário pelo ID fornecido.

- **Parâmetros:**
  - `user_id`: ID do usuário a ser excluído.

- **Resposta:**  
  - **Status Code:** 200 OK  
  - **Body:**  
    ```json
    {
      "message": "User deleted"
    }
    ```

---

### 6. **POST /login**

Autentica um usuário com o e-mail e senha fornecidos.

- **Parâmetros:**
  - `email`: Endereço de e-mail do usuário.
  - `password`: Senha do usuário.

- **Resposta:**  
  - **Status Code:** 200 OK  
  - **Body:**  
    ```json
    {
      "message": "Login successful"
    }
    ```

  - **Erros:**
    - **404 Not Found** - Se o usuário não for encontrado.
    - **401 Unauthorized** - Se a senha estiver incorreta.

---

## Instalação

Para rodar a API localmente, siga os passos abaixo:

### 1. Clone o repositório

```bash
git clone https://github.com/JATamagno/toro-test.git
cd toro-test
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

- **No Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **No Linux/macOS:**
  ```bash
  source venv/bin/activate
  ```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Rode a aplicação

```bash
uvicorn toro_test.app:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

---

## Testes

Para rodar os testes, utilize o **pytest**:

1. Execute os testes:

```bash
pytest
```

Os testes serão executados e você verá os resultados no terminal.

---

## Deploy

### 1. Deploy no **AWS EC2** 

Para fazer o deploy em uma instância EC2 da AWS, siga os passos abaixo:

#### 1.1. Crie uma instância EC2

1. Vá até o [AWS EC2 Dashboard](https://console.aws.amazon.com/ec2/).
2. Crie uma nova instância EC2 com a configuração de sua preferência.
3. A instância deve ter uma chave SSH para acesso remoto.

#### 1.2. Acesse a instância via SSH

Com a chave privada (.pem) que você gerou, acesse a instância:

```bash
ssh -i "sua-chave.pem" ec2-user@ec2-xx-xx-xx-xx.compute-1.amazonaws.com
```

#### 1.3. Instale as dependências

Uma vez na instância EC2, instale o Python, Git e pip (se necessário):

```bash
sudo yum update -y
sudo yum install python3 git -y
pip3 install --upgrade pip
```

#### 1.4. Faça o clone do repositório

Clone o repositório na instância EC2:

```bash
git clone https://github.com/JATamagno/toro-test.git
cd toro-test-api
```

#### 1.5. Instale as dependências

Instale as dependências da aplicação:

```bash
pip install -r requirements.txt
```

#### 1.6. Rode a aplicação

Use o `uvicorn` para rodar a aplicação:

```bash
uvicorn toro_test.app:app --reload
```

A API estará disponível em `http://<public-ip-da-instancia>:8000`.

---

## Observações

Talvez seja necessário utilizar um proxy reverso como NGINX e um gerenciador de processos como o PM2 caso você deseje deixar a aplicação disponível 24/7.

---
