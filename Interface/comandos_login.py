from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from Banco.estoque_db_tables import Banco
from Banco.estoque_db_querys_autenticacao import Querys_Autenticacao
from Banco.estoque_db_querys_usuarios import Querys
from Interface import Projeto_Login, Home

app = QtWidgets.QApplication([])

#telaLogin=uic.loadUi("Projeto_Login.ui")
#telaLogin.show()
app.exec()

Banco('estoque.db')
comandos_db = Querys_Autenticacao('estoque.db')
comandos_db_usuarios = Querys('estoque.db')
telaHome = uic.loadUi("Home.ui")

class Login(QMainWindow,Projeto_Login.Ui_Login):
    def __init__(self, parent=None):

        super(Login, self).__init__(parent)
        super().setupUi(self)

        self.btnLogar.clicked.connect(self.Autenticar)
        self.janela_principal = parent

    def Autenticar(self):
        usuario = self.txtUsuario.text()
        senha = self.txtSenha.text()

        if usuario == "" or senha == "":
            QMessageBox.about(self,"Alerta","Obrigatório o preenchimento de Usuário e Senha")
        else:
            if Querys.selecionar_todos(comandos_db_usuarios) == False:
                Querys.cadastrar(comandos_db_usuarios, "", usuario, "", senha,"", "ativo", "admin")
                self.close()
                telaHome.show()
                QMessageBox.about(telaHome,"","Bem-vindo(a)")
            else:
                valida_usuario = self.Autenticar_Banco(usuario, senha)
                if valida_usuario != None and valida_usuario != "Erro":

                    self.close()
                    telaHome.show()
                    QMessageBox.about(telaHome,"Bem-vindo(a)","Olá " + valida_usuario)
                else:
                    QMessageBox.about(self,"Alerta","Usuário e Senha inválidos.")

    def Autenticar_Banco(self, usuario ,senha):

        autenticado = Querys_Autenticacao.Autenticar(comandos_db, usuario,senha)

        return autenticado


