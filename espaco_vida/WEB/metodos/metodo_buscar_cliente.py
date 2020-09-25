from models import exibe_usuario


QUERY = 'SELECT u.id_pessoa, u.Nome, u.cpf, e.endereco '
QUERY += 'FROM Pessoa u '
QUERY += 'INNER JOIN Endereco_Pessoa e '
QUERY += 'ON u.id_pessoa= e.id_pessoa '




class busca_usuario:
    def __init__(self, db):
        self.__db = db

    def listar(self):
            cursor = self.__db.connection.cursor()
            cursor.execute(QUERY)
            usuario = traduz_usuario(cursor.fetchall())
            return usuario



def traduz_usuario(lista_usuario):
    def cria_usuario_com_tupla(tupla):
        
        
        return exibe_usuario(tupla[0], tupla[1], tupla[2], tupla[3])
        
    return list(map(cria_usuario_com_tupla, lista_usuario))