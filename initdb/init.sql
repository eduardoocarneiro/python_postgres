-- Criação do schema
CREATE SCHEMA IF NOT EXISTS flask;

-- Criação da tabela no schema flask
CREATE TABLE IF NOT EXISTS flask.pessoas (
    Nome VARCHAR(100),
    Idade INT,
    Sexo VARCHAR(10),
    Apelido VARCHAR(50),
    Endereco VARCHAR(200)
);
