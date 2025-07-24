# Choose the version:

* [English](#people-registration)
* [PTBR](#cadastro-de-pessoas)


# People registration
Simple Python application that queries, inserts, updates, or deletes people data in a Postgres database. Feel free to make improvements.

# Requirements

- Docker
- Docker compose

# Installation
Clone the project:
```
git clone https://github.com/eduardoocarneiro/python_postgres_form.git

cd python_postgres_form

```

Build the application:

```
docker compose build --no-cache
```

Start the containers:

```
docker compose up -d
```

At this point, two containers will be running:

- ```app```: Python application
- ```postgres```: Postgres database

# Accessing the application
The application exposes port 8000, so to access it, just open the following URL in your browser:

```
http://localhost:8000
```

# Helm version
This project also includes a version for Kubernetes using Helm. [Click here](helm_chart) to access the Helm version and its documentation.

# Cadastro de Pessoas
Aplicação simples em Python que consulta, insere, altera ou deleta dados de pessoas em um banco Postgres. Sinta-se à vontade para fazer melhorias.

# Requisitos

- Docker
- Docker compose

# Instalação
Clonar o projeto:
```
git clone https://github.com/eduardoocarneiro/python_postgres_form.git

cd python_postgres_form

```

Fazer o build da aplicação:

```
docker compose build --no-cache
```

Iniciar os conteiners:

```
docker compose up -d
```

Nesse ponto teremos dois conteiners iniciados:

- ```app```: Aplicação python
- ```postgres```: Banco postgres

# Acessando a aplicação
A aplicação expõe a porta 8000, portanto para acessá-la basta acessar a seguinte URL no browser:

```
http://localhost:8000
```

# Versão helm
Há também nesse projeto, uma versão para kubernetes utilizando o Helm. [Clique aqui](helm_chart) para acessar a versão Helm, bem como a documentação.
