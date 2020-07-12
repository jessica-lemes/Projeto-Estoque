import sqlite3

class Querys_movimentacao:

    def __init__(self, banco):
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()

    def cadastra_movimentacao(self,tipo, qtde, idProduto_FK, idUsuario_FK):
        try:
            self.conexao = sqlite3.connect('estoque.db', timeout=10)
            self.cursor = self.conexao.cursor()
            query = "INSERT INTO movimentacao (data_mov, tipo, qtde, idProduto_FK, idUsuario_FK)" \
                    "VALUES (current_date , ?, ?, ?, ?)"
            self.cursor.execute(query, (tipo, qtde, idProduto_FK, idUsuario_FK,))
            self.conexao.commit()
            self.cursor.close()
            self.conexao.close()
        except Exception as e:
            return "Erro"

if __name__ == '__main__':
    banco = Querys_movimentacao('estoque.db')