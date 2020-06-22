import sqlite3


class Banco:

    def __init__(self, banco):
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()
        self.criar_db()


    def criar_db(self):

        self.cursor.execute('CREATE TABLE IF NOT EXISTS usuarios('
                    'idUsuario INTEGER PRIMARY KEY AUTOINCREMENT,'
                    'nome VARCHAR(50),'
                    'CPF VARCHAR(11),'
                    'email VARCHAR(50),'
                    'senha VARCHAR(20),'
                    'situacao VARCHAR(10),'
                    'tipoUsuario VARCHAR(20)'
                    ')')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS movimentacao('
                    'idMovimento INTEGER PRIMARY KEY AUTOINCREMENT,'
                    'data_mov DATE,'
                    'tipo VARCHAR (10),'
                    'qtde INTEGER,'
                    'situacao VARCHAR (10),'
                    'canceladoPor VARCHAR(50),'
                    'dataCancelamento DATE,'
                    'idProduto_FK INTEGER,'
                    'idUsuario_FK INTEGER,'
                    'FOREIGN KEY(idUsuario_FK) REFERENCES usuarios(idUsuario),'
                    'FOREIGN KEY(idProduto_FK) REFERENCES produtos(idProduto)'
                    ')')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS produtos('
                    'idProduto INTEGER PRIMARY KEY AUTOINCREMENT,'
                    'nome VARCHAR(50),'
                    'descricao VARCHAR(100),'
                    'qtde_estoque INT,'
                    'qtde_minimo INT,'
                    'valor_produto REAL'
                    ')')

        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()

if __name__ == "__main__":
    banco = Banco('estoque.db')