import sqlite3


class Querys:

    def __init__(self, banco):
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()

    def cadastrar(self, nome, cpf, email, senha, funcao, situacao, tipo_usuario):
        query = "INSERT OR IGNORE INTO usuarios (nome, cpf, email, senha, funcao, situacao, tipoUsuario)" \
                   "VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.cursor.execute(query, (nome, cpf, email, senha, funcao, situacao, tipo_usuario))
        teste = self.conexao.commit()
        self.cursor.close()
        self.conexao.close()


    def alterar(self, nome, cpf, email, senha=None, funcao=None, situacao=None, tipo_usuario=None, id_usuario=None):
        query = "UPDATE OR IGNORE usuarios SET nome = %s, cpf= %s, email = %s, senha = %s, funcao =%s" \
                "situacao=%s, tipo_usuario=%s WHERE id= %s"
        self.cursor.execute(query, (nome, cpf, email, senha,funcao, situacao, tipo_usuario, id_usuario))
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()


    def selecionar(self, nome):
        query = "SELECT * FROM usuarios WHERE nome = %s"
        self.cursor.execute(query, (nome,))

        self.conexao.close()
        self.cursor.close()

    def selecionar_cpf(self, cpf):
        query = "SELECT * FROM usuarios WHERE cpf = ?"
        self.cursor.execute(query(cpf,))

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
        query = "DELETE FROM usuarios WHERE id = %s"
        self.cursor.execute(query, (id,))
        self.conexao.commit()
        self.conexao.close()
        self.cursor.close()

if __name__ == '__main__':
    banco = Querys('estoque.db')