import sqlite3

class Dados_Menu:

    def __init__(self, banco):
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()

    def estoque_baixo(self):
        try:
            query = "select * from produtos where qtde_estoque < qtde_minimo"

            retorno = self.cursor.execute(query)

            lista = []
            for registro in retorno.fetchall():
                lista.append(registro)
            return lista

        except Exception as e:
            return "Erro"

        self.cursor.close()
        self.conexao.close()



if __name__ == '__main__':
    banco = Dados_Menu('estoque.db')