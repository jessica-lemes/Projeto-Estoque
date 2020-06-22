from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Banco.estoque_db_tables import Banco
from Banco.estoque_db_querys_autenticacao import Querys


Banco('estoque.db')
comandos_db = Querys('estoque.db')


def Autenticar():
    usuario = telaLogin.txtUsuario.text()
    senha = telaLogin.txtSenha.text()

    if usuario == "" or senha == "":
        QMessageBox.about(telaLogin,"Alerta","Obrigatório o preenchimento de Usuário e Senha")
    else:
        #chama a def q verifica se existe algum user
        #se existe executa oq ja existe
        
        valida_usuario = Autenticar_Banco(usuario,senha)
        if valida_usuario != "" and valida_usuario != "Erro":
            telaLogin.close()
            telaHome.show()
            QMessageBox.about(telaHome,"Bem-vindo(a)","Olá " + valida_usuario)
        else:
            QMessageBox.about(telaLogin,"Alerta","Usuário e Senha inválidos.")

        #senao chama def de cadastrar usuario e passa pra tela de home
  
def Autenticar_Banco(usuario,senha):

    autenticado = Querys.Autenticar(comandos_db, usuario,senha)
    
    return autenticado


app=QtWidgets.QApplication([])
telaLogin=uic.loadUi("Projeto_Login.ui")
telaHome=uic.loadUi("Home.ui")
telaLogin.btnLogar.clicked.connect(Autenticar)
telaLogin.show()
app.exec()