DROP DATABASE Espaco_Terapia
CREATE DATABASE Espaco_Terapia
USE Espaco_Terapia

CREATE TABLE Usuario(
        id_usuario SMALLINT IDENTITY(1,1) NOT NULL ,
        nome_usuario VARCHAR(40) ,
		email_usuario VARCHAR(40),
        dt_cadastro DATE ,
        senha_aplicacao VARCHAR(500),
        CONSTRAINT pkcod_usuario PRIMARY KEY (id_usuario),
		CONSTRAINT uq_email_usuario  UNIQUE (email_usuario)
    )

INSERT INTO Usuario(nome_usuario,email_usuario,senha_aplicacao) VALUES ('ADMINISTRADOR','administrador@administrador.com','91f5167c34c400758115c2a6826ec2e3')

CREATE TABLE Pessoa(
	id_pessoa SMALLINT NOT NULL,
	Nome VARCHAR(40),
	Data_nascimento Date,
	CPF VARCHAR(11),
	sexo VARCHAR(10),

	CONSTRAINT pk_id_pessoa PRIMARY KEY (id_pessoa)
)

insert into Pessoa(id_pessoa) values ('0')

CREATE TABLE Endereco_Pessoa(
	id_endereco_pessoa SMALLINT IDENTITY(1,1) NOT NULL,
	id_pessoa SMALLINT,
	endereco VARCHAR(90),
    numero SMALLINT,
    cidade VARCHAR(60),
    uf VARCHAR(2),
    cep INT,

	CONSTRAINT pk_id_endereco_pessoa PRIMARY KEY (id_endereco_pessoa),
	CONSTRAINT fk_idpessoa FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa)
)


CREATE TABLE Contato_Pessoa(
	id_contato_pessoa SMALLINT IDENTITY (1,1) NOT NULL,
	id_pessoa SMALLINT,
	celular VARCHAR(15),
    telefone VARCHAR(14),
    email VARCHAR(200),
    nome_contato VARCHAR(50),

	CONSTRAINT pk_id_contatopessoa PRIMARY KEY (id_contato_pessoa),
	CONSTRAINT fkidPessoa FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa)

)


CREATE TABLE Quadro_Clinico(
	id_quadro_clinico SMALLINT IDENTITY (1,1) NOT NULL,
	id_pessoa SMALLINT,
	artrose VARCHAR(3),
	protusao_ernia_disco VARCHAR(3),
	cirurgia VARCHAR(50),
	medicacao VARCHAR(50),
	queixas_atuais VARCHAR(80),

	CONSTRAINT pk_id_quadro_clinico PRIMARY KEY (id_quadro_clinico),
	CONSTRAINT fkidpessoa_quadro FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa)
)