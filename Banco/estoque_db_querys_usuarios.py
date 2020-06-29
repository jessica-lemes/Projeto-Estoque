import sqlite3


class Querys:

    def __init__(self, banco):
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()

    def cadastrar(self, nome, cpf, email, senha, funcao, situacao, tipo_usuario):

        self.conexao = sqlite3.connect('estoque.db', timeout=10)
        self.cursor = self.conexao.cursor()
        query = "INSERT OR IGNORE INTO usuarios (nome, cpf, email, senha, funcao, situacao, tipoUsuario)" \
                   "VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.cursor.execute(query, (nome, cpf, email, senha, funcao, situacao, tipo_usuario))
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()


    def editar(self, nome, cpf, email, senha=None, funcao=None, situacao=None, tipo_usuario=None, id_usuario=None):
        try:

            query = "UPDATE OR IGNORE usuarios SET nome = ?, cpf= ?, email = ?, senha = ?, funcao =?, situacao=?, tipoUsuario=?" \
                    " WHERE idUsuario= ?"
            self.cursor.execute(query, (nome, cpf, email, senha,funcao, situacao, tipo_usuario,id_usuario,))
            self.conexao.commit()
            self.cursor.close()
            self.conexao.close()

        except Exception as e:
            return "Erro"


    def selecionar(self, nome):
        query = "SELECT * FROM usuarios WHERE nome = %s"
        self.cursor.execute(query, (nome,))

        self.conexao.close()
        self.cursor.close()

    def selecionar_cpf(self, cpf):
        query = "SELECT * FROM usuarios WHERE cpf = ?"
        self.cursor.execute(query, (cpf,))

        self.conexao.close()
        self.cursor.close()

    def selecionar_id(self, id):
        try:
            query = "SELECT * FROM usuarios WHERE idUsuario = ?"
            retorno = self.cursor.execute(query,(id,))
            lista = []
            for registro in retorno.fetchall():
                lista.append(registro)
            return lista

        except Exception as e:
            return "Erro"

        self.conexao.close()
        self.cursor.close()

    def selecionar_todos(self):
        query = "SELECT * FROM usuarios"
        self.cursor.execute(query)
        if self.cursor.fetchall():
            return True
        else:
            return False
        self.cursor.close()
        self.conexao.close()


    def excluir(self, id):
        query = "DELETE FROM usuarios WHERE idUsuario = ?"
        self.cursor.execute(query, (id,))
        self.conexao.commit()
        self.conexao.close()

    def buscar_banco(self, nome):
        nome = '%'+nome+'%'
        query = "select * from usuarios where nome like ?"
        try:
            retorno = self.cursor.execute(query, (nome,))
            lista = []
            for registro in retorno.fetchall():
                lista.append(registro)
            return lista

            self.cursor.close()
            self.conexao.close()

        except Exception as e:
            return "Erro"




if __name__ == '__main__':
    banco = Querys('estoque.db')