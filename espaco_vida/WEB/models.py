class Usuario:
    def __init__(self, nome_usuario, email_usuario, dt_cadastro, senha_aplicacao,  id_usuario=None):
        self.id_usuario = id_usuario
        self.nome_usuario = nome_usuario
        self.email_usuario = email_usuario
        self.dt_cadastro = dt_cadastro
        self.senha_aplicacao = senha_aplicacao
    

class Pessoa:
    def __init__(self, id_pessoa, nome, data_nascimento, cpf, sexo):
        self.id_pessoa = id_pessoa
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.sexo = sexo

class Endereco_Pessoa:
    def __init__(self, id_pessoa, endereco, numero, cidade,uf,cep,id_endereco_pessoa= None):
        self.id_endereco_pessoa = id_endereco_pessoa
        self.id_pessoa = id_pessoa
        self.endereco = endereco
        self.numero = numero
        self.cidade = cidade
        self.uf = uf
        self.cep = cep

class Contato_Pessoa:
    def __init__(self, id_pessoa, celular, telefone, email, nome_contato, id_contato_pessoa=None):
        self.id_contato_pessoa = id_contato_pessoa
        self.id_pessoa = id_pessoa
        self.celular = celular
        self.telefone = telefone
        self.email = email
        self.nome_contato = nome_contato

class Quadro_Clinico:
    def __init__(self, id_pessoa, artrose, protusao_ernia_disco, cirurgia, medicacao, queixas_atuais, id_quadro_clinico=None):
        self.id_pessoa = id_pessoa
        self.artrose = artrose
        self.protusao_ernia_disco = protusao_ernia_disco
        self.cirurgia = cirurgia
        self.medicacao = medicacao
        self.queixas_atuais = queixas_atuais


class exibe_usuario:
    def __init__(self, id_pessoa, nome, cpf, endereco):
        self.id_pessoa = id_pessoa
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco