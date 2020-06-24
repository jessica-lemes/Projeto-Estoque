from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Banco.estoque_db_querys_usuarios import Querys
from Banco.estoque_db_querys_autenticacao import Querys_Autenticacao

comandos_db_usuarios = Querys('estoque.db')


def voltar():
    telaCadUsuarios.close()
    telaHome.show()

def limpar():
    telaCadUsuarios.lineNome.setText("")
    telaCadUsuarios.lineCpf.setText("")
    telaCadUsuarios.lineFuncao.setText("")
    telaCadUsuarios.lineEmail.setText("")
    telaCadUsuarios.lineSenha.setText("")
    telaCadUsuarios.rbtnAtivo.setChecked(True)
    telaCadUsuarios.rbtnUsuario.setChecked(True)



def cadastrar():
    nome = telaCadUsuarios.lineNome.text()
    cpf = telaCadUsuarios.lineCpf.text()
    funcao = telaCadUsuarios.lineFuncao.text()
    email = telaCadUsuarios.lineEmail.text()
    senha = telaCadUsuarios.lineSenha.text()
    if telaCadUsuarios.rbtnAtivo.isChecked():
        situacao = "Ativo"
    else:
        situacao = "Inativo"
    if telaCadUsuarios.rbtnUsuario.isChecked():
        tipo_usuario = "Usuário"
    else:
        tipo_usuario = "Administrador"
    cadastrar_banco(nome,cpf,email,senha,funcao,situacao,tipo_usuario)

def cadastrar_banco(nome, cpf, email, senha,funcao, situacao,tipo_usuario):


    if nome == "" or cpf == "" or email == "" or senha == "" or funcao == "":
        QMessageBox.about(telaCadUsuarios,"Alerta","Obrigatório o preenchimento de todos os campos.")
    if len(cpf) < 11:
        QMessageBox.about(telaCadUsuarios, "Alerta", "CPF Inválido.")
    verifica_existente = Autenticar_Banco(cpf, senha)
    if verifica_existente != None and verifica_existente != "Erro":
        QMessageBox.about(telaCadUsuarios, "Alerta", "CPF já cadastrado no banco de dados.")
    else:
        Querys.cadastrar(comandos_db_usuarios, nome, cpf, email, senha,funcao, situacao, tipo_usuario)
        QMessageBox.about(telaCadUsuarios,"Mensagem","Usuário cadastrado com sucesso.")


def Autenticar_Banco(usuario, senha):
    cad_encontrado = Querys_Autenticacao.Autenticar(Querys_Autenticacao('estoque.db'),usuario, senha)
    return cad_encontrado



app=QtWidgets.QApplication([])
telaCadUsuarios=uic.loadUi("cadUsuarios.ui")
telaHome=uic.loadUi("Home.ui")
telaCadUsuarios.btnVoltar.clicked.connect(voltar)
telaCadUsuarios.btnLimpar.clicked.connect(limpar)
telaCadUsuarios.btnCadastrar.clicked.connect(cadastrar)
telaCadUsuarios.show()
app.exec()