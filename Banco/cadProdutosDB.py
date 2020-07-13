import sqlite3


class CadProdutosDB:

    def __init__(self):
        self.conexao = sqlite3.connect('estoque.db')
        self.cursor = self.conexao.cursor()
        self.resultado = []

    def cadastrar(self, nome, descricao, qtde_estoque, qtde_minimo, valor_produto):

        query = "INSERT OR IGNORE INTO produtos (nome, descricao, qtde_estoque, qtde_minimo, valor_produto)" \
                   "VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(query, (nome, descricao, qtde_estoque, qtde_minimo, valor_produto))
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()


    def alterar(nome, descricao, qtde_estoque, qtde_minimo, valor_produto, idProduto):
        query = "UPDATE produtos SET nome = ?, descricao= ?, qtde_estoque = ?, qtde_minimo = ?, valor_produto = ? WHERE idProduto = ?"
        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()
        cursor.execute(query, (nome, descricao, qtde_estoque, qtde_minimo, valor_produto, idProduto))
        conexao.commit()

    def selecionar(self, id):
        query = "SELECT * FROM produtos WHERE idProduto = ?"
        self.resultado = self.cursor.execute(query, (id,))
        return self.resultado.fetchall()
        self.conexao.close()
        self.cursor.close()

    def selecionar_todos(self):
        query = "SELECT * FROM produtos"
        self.resultado = self.cursor.execute(query)
        return self.resultado.fetchall()
        self.conexao.close()
        self.cursor.close()

    def excluir(self, id):
        query = "DELETE FROM produtos WHERE idProduto = ?"
        self.cursor.execute(query, (id,))
        self.conexao.commit()


    def __getitem__(self, item):
        return self.resultado[item]