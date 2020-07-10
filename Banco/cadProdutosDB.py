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


    def alterar(self, nome, descricao, quantidade, qtd_minima, valor, idProduto=None):
        query = "UPDATE produtos SET nome = %s, descricao= %s, qtde_estoque = %s, qtde_minimo" \
                " = %s, valor_produto=%s WHERE idProduto = ?"
        self.cursor.execute(query, (nome, descricao, quantidade, qtd_minima, valor, int(idProduto),))
        self.conexao.commit()
        self.conexao.close()
        self.cursor.close()

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

    def excluir(self, nome):
        query = "DELETE FROM produtos WHERE nome = %s"
        self.cursor.execute(query, (nome,))
        self.conexao.commit()
        self.conexao.close()
        self.cursor.close()

    def __getitem__(self, item):
        return self.resultado[item]