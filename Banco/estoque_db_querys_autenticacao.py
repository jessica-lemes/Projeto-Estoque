import sqlite3

class Querys_Autenticacao:

    def __init__(self, banco):
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()

    def Autenticar(self, cpf, senha):

        self.conexao = sqlite3.connect('estoque.db')
        self.cursor = self.conexao.cursor()

        query = "select nome from usuarios where CPF = ? and senha = ?"
        try:
            retorno = self.cursor.execute(query,(cpf, senha))

            for registro in retorno.fetchall():
                return registro[0]

            self.cursor.close()
            self.conexao.close()

        except Exception as e:
            return "Erro"

    def buscar_banco(self, nome):
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
    banco = Querys_Autenticacao('estoque.db')