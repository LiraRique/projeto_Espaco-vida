
from models import Contato_Pessoa, Endereco_Pessoa, Pessoa, Quadro_Clinico, Usuario

SQL_ID_PESSOA = 'select max(id_pessoa) as id_pessoa from Pessoa'

SQL_CADASTRAR_PESSOA = 'INSERT INTO Pessoa(id_pessoa, nome, data_nascimento, cpf, sexo) VALUES (?,?,?,?,?)'

SQL_CADASTRAR_CONTATO = 'INSERT INTO Contato_Pessoa(id_pessoa, celular, telefone, email, nome_contato) VALUES (?, ?, ?, ?, ?)'

SQL_CADASTRAR_ENDERECO = 'INSERT INTO Endereco_Pessoa(id_pessoa, endereco, numero, cidade, uf, cep) VALUES (?, ?, ?, ?, ?, ?)'

SQL_CADASTRAR_QUADRO_CLINICO = 'INSERT INTO Quadro_Clinico(id_pessoa, artrose, protusao_ernia_disco, cirurgia, medicacao, queixas_atuais) VALUES (?, ?, ?, ?, ?, ? )'


class cadastrar_cliente:
    def __init__(self, db):
        self.__db = db


    def cadastrar_cliente_sistema(self, Pessoa, Contato_Pessoa, Endereco_Pessoa, Quadro_Clinico):
        cursor= self.__db.connection.cursor()

        cursor.execute(SQL_CADASTRAR_PESSOA, (Pessoa.id_pessoa, Pessoa.nome, Pessoa.data_nascimento, Pessoa.cpf, Pessoa.sexo))
        cursor.execute(SQL_CADASTRAR_CONTATO, (Contato_Pessoa.id_pessoa, Contato_Pessoa.celular, Contato_Pessoa.telefone, Contato_Pessoa.email, Contato_Pessoa.nome_contato))
        cursor.execute(SQL_CADASTRAR_ENDERECO, (Endereco_Pessoa.id_pessoa, Endereco_Pessoa.endereco, Endereco_Pessoa.numero, Endereco_Pessoa.cidade, Endereco_Pessoa.uf, Endereco_Pessoa.cep))
        cursor.execute(SQL_CADASTRAR_QUADRO_CLINICO, (Quadro_Clinico.id_pessoa, Quadro_Clinico.artrose, Quadro_Clinico.protusao_ernia_disco, Quadro_Clinico.cirurgia, Quadro_Clinico.medicacao, Quadro_Clinico.queixas_atuais))
        self.__db.connection.commit()
 

    def ultima_posicao_id(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_ID_PESSOA)
        dados = cursor.fetchone()
        idpessoa = int(dados[0])
        return idpessoa