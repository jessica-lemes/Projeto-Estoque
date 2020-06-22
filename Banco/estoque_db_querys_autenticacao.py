import sqlite3


class Querys:

    def __init__(self, banco):
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()

    def Autenticar(self, cpf, senha):

            query = "select nome from usuarios where CPF = ? and senha = ?"
            try:
                retorno = self.cursor.execute(query,(cpf, senha))
                nome = ""

                for registro in retorno.fetchall():
                    nome = registro[0]        
                    
                self.cursor.close()
                self.conexao.close()

                return nome

            except Exception as e:
                return "Erro"

if __name__ == '__main__':
    banco = Querys('estoque.db')