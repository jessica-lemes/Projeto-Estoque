import sqlite3

class Querys_Autenticacao:

    def __init__(self, banco):
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()

    def Autenticar(self, cpf, senha):

        self.conexao = sqlite3.connect('estoque.db')
        self.cursor = self.conexao.cursor()

        query = "select idUsuario, nome, tipoUsuario from usuarios where CPF = ? and senha = ?"
        try:
            retorno = self.cursor.execute(query,(cpf, senha))

            lista =[]

            for registro in retorno.fetchall():
                return registro

            self.cursor.close()
            self.conexao.close()

        except Exception as e:
            return "Erro"


if __name__ == '__main__':
    banco = Querys_Autenticacao('estoque.db')