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

    def selecionar_movimentacao(self):
        self.conexao = sqlite3.connect('estoque.db')
        self.cursor = self.conexao.cursor()

        try:
            query = "SELECT * FROM movimentacao"
            retorno = self.cursor.execute(query,)
            lista = []
            for registro in retorno.fetchall():
                lista.append(registro)
            return lista

        except Exception as e:
            return "Erro"

        self.conexao.close()
        self.cursor.close()


    def buscar_banco(self, produto, data, tipo, usuario):
        self.conexao = sqlite3.connect('estoque.db')
        self.cursor = self.conexao.cursor()
        produto = '%'+produto+'%'
        data = '%'+data+'%'
        tipo = '%'+tipo+'%'
        usuario = '%'+usuario+'%'

        query = "SELECT m.idMovimento, strftime('%d/%m/%Y', m.data_mov), m.tipo, p.nome, p.descricao ,m.qtde, u.nome from movimentacao m"\
                "  join produtos p" \
                "  on m.idProduto_FK = p.idProduto"\
                "  join usuarios u" \
                "  on m.idUsuario_FK = u.idUsuario"\
                " where 1 = 1 "
        if produto != "" and produto != "%%":
            query += "and p.nome like '" + produto + "'"
        if data != "" and data != "%%":
            query += "and strftime('%d/%m/%Y', m.data_mov) like '" + data + "'"
        if tipo != "" and tipo != "%%":
            query += "and m.tipo like '" + tipo + "'"
        if usuario != "" and usuario != "%%":
            query += "and u.nome like '" + usuario + "'"


        try:
            retorno = self.cursor.execute(query)
            lista = []
            for registro in retorno.fetchall():
                lista.append(registro)
            return lista

            self.cursor.close()
            self.conexao.close()

        except Exception as e:
            return "Erro"


if __name__ == '__main__':
    banco = Querys_movimentacao('estoque.db')


#SELECT m.idMovimento, m.data_mov, m.tipo, p.nome, p.descricao ,m.qtde, u.nome from movimentacao m
#join produtos p
#	on m.idProduto_FK = p.idProduto
#join usuarios u
#	on m.idUsuario_FK = u.idUsuario
#WHERE 1 = 1

