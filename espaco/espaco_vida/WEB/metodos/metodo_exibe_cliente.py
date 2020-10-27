QUERY = 'SELECT a.Nome, a.CPF, a.Data_nascimento, a.sexo, b.cep, b.cidade, '
QUERY += 'b.uf, b.endereco, b.numero, c.telefone, c.celular, d.artrose, d.protusao_ernia_disco, d.cirurgia, d.medicacao, d.queixas_atuais'
QUERY += 'FROM Pessoa A'
QUERY += 'INNER JOIN Endereco_Pessoa B'  
QUERY += 'ON A.id_pessoa= B.id_pessoa'
QUERY += 'INNER JOIN  Contato_Pessoa C' 
QUERY += 'ON C.id_contato_pessoa= A.id_pessoa'
QUERY += 'INNER JOIN Quadro_Clinico D'
QUERY += 'ON D.id_pessoa = A.id_pessoa'
QUERY += 'WHERE A.id_pessoa= ?'


class busca_cliente_por_id:
    def __init__(self, db):
        self.__db = db

    def listar(self, id):
            cursor = self.__db.connection.cursor()
            cursor.execute(QUERY, id)
         
            dados = []

            for row in cursor:
                dados.append(row)

            return dados
            