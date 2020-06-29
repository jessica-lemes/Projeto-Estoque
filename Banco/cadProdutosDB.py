import sqlite3


class CadProdutosDB:

    def __init__(self, banco):
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()

    def cadastrar(self, nome, descricao, qtde_estoque, qtde_minimo, valor_produto):

        query = "INSERT OR IGNORE INTO produtos (nome, descricao, qtde_estoque, qtde_minimo, valor_produto)" \
                   "VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(query, (nome, descricao, qtde_estoque, qtde_minimo, valor_produto))
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()


    def alterar(self, nome, descricao, quantidade, qtd_minima, valor, id):
        query = "UPDATE OR IGNORE produtos SET nome = %s, descricao= %s, quantidade = %s, qtd_minima" \
                " = %s, valor=%s WHERE id= %s"
        self.cursor.execute(query, (nome, descricao, quantidade, qtd_minima, valor, id))
        self.conexao.commit()
        self.conexao.close()
        self.cursor.close()

    def selecionar(self, id):
        query = "SELECT * FROM produtos WHERE id = %s"
        self.cursor.execute(query, (id,))

        self.conexao.close()
        self.cursor.close()

    def selecionar_todos(self):
        query = "SELECT * FROM produtos"
        self.cursor.execute(query)
        if self.cursor.fetchall():
            return True
        else:
            return False
        self.conexao.close()
        self.cursor.close()

    def excluir(self, id):
        query = "DELETE FROM produtos WHERE id = %s"
        self.cursor.execute(query, (id,))
        self.conexao.commit()
        self.conexao.close()
        self.cursor.close()

if __name__ == '__main__':
    banco = CadProdutosDB('estoque.db')