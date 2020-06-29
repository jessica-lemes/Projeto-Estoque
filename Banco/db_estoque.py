import sqlite3


class Querys:

    def __init__(self, banco):
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()


    def selecionar_id(self, id):
        self.conexao = sqlite3.connect('estoque.db')
        self.cursor = self.conexao.cursor()
        try:
            query = "SELECT * FROM produtos WHERE idProduto = ?"
            retorno = self.cursor.execute(query,(id,))
            lista = []
            for registro in retorno.fetchall():
                lista.append(registro)
            return lista

        except Exception as e:
            return "Erro"

        self.conexao.close()
        self.cursor.close()

    def buscar_banco(self, nome):
        self.conexao = sqlite3.connect('estoque.db')
        self.cursor = self.conexao.cursor()
        nome = '%'+nome+'%'
        query = "select idProduto, nome, qtde_minimo, qtde_estoque from produtos where nome like ?"
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

    def atualizar_estoque(self, qtde_estoque, id):
        self.conexao = sqlite3.connect('estoque.db')
        self.cursor = self.conexao.cursor()
        query = "UPDATE produtos SET qtde_estoque = ? WHERE idProduto = ?"
        try:
            self.cursor.execute(query, (qtde_estoque,id,))
            self.conexao.commit()
            self.conexao.close()
            self.cursor.close()

        except Exception as e:
            return "Erro"

if __name__ == '__main__':
    banco = Querys('estoque.db')