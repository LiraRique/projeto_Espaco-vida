from ..models import Pessoa, Contato_Pessoa, Endereco_Pessoa, Quadro_Clinico

SQL_ID_PESSOA = 'select max(id_pessoa) as id_pessoa from Pessoa'

SQL_CADASTRAR_PESSOA = 'INSERT INTO Pessoa(id_pessoa, nome, cpf) VALUES (?,?,?)'

SQL_CADASTRAR_CONTATO = 'INSERT INTO Contato_Pessoa(id_pessoa, celular, telefone, email, nome_contato) VALUES (?, ?, ?, ?, ?)'

SQL_CADASTRAR_ENDERECO = 'INSERT INTO Endereco_Pessoa(id_pessoa, endereco, complemento, cidade, uf, cep) VALUES (?, ?, ?, ?, ?, ?)'


class cadastrar_cliente:
    def __init__(self, db):
        self.__db = db


    def cadastrar_cliente_sistema(self, Pessoa, Contato_Pessoa, Endereco_Pessoa, Quadro_Clinico):
        cursor= self.__db(()

        cursor.execute(SQL_CADASTRAR_PESSOA, (Pessoa.id_pessoa, Pessoa.nome, Pessoa.cpf))
        cursor.execute(SQL_CADASTRAR_CONTATO, (Contato_Pessoa.id_pessoa, Contato_Pessoa.celular, Contato_Pessoa.telefone, Contato_Pessoa.email, Contato_Pessoa.nome_contato))
        cursor.execute(SQL_CADASTRAR_ENDERECO, ())


    def ultima_posicao_id(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_ID_PESSOA)
        dados = cursor.fetchone()
        idpessoa = int(dados[0])
        return idpessoa