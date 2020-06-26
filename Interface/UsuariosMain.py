from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from Banco.estoque_db_querys_usuarios import Querys
from Banco.estoque_db_querys_autenticacao import Querys_Autenticacao

app=QtWidgets.QApplication([])
telaHome=uic.loadUi("Home.ui")

comandos_db_usuarios = Querys('estoque.db')

def cad_voltar():
    telaCadUsuarios.close()
    telaHome.show()

def cons_voltar():
    telaConsUsuarios.close()
    telaHome.show()

def edit_voltar():
    telaEditUsuarios.close()
    telaConsUsuarios.show()

def cad_limpar():
    telaCadUsuarios.lineNome.setText("")
    telaCadUsuarios.lineCpf.setText("")
    telaCadUsuarios.lineFuncao.setText("")
    telaCadUsuarios.lineEmail.setText("")
    telaCadUsuarios.lineSenha.setText("")
    telaCadUsuarios.rbtnAtivo.setChecked(True)
    telaCadUsuarios.rbtnUsuario.setChecked(True)

def edit_limpar():
    telaEditUsuarios.lineNome.setText("")
    telaEditUsuarios.lineCpf.setText("")
    telaEditUsuarios.lineFuncao.setText("")
    telaEditUsuarios.lineEmail.setText("")
    telaEditUsuarios.lineSenha.setText("")
    telaEditUsuarios.rbtnAtivo.setChecked(True)
    telaEditUsuarios.rbtnUsuario.setChecked(True)

def botao_novocad():
    telaConsUsuarios.close()
    telaCadUsuarios.show()

def botao_editar():
 #logica que pega a celula selecionada e traz um valor
    telaConsUsuarios.close()
    telaEditUsuarios.show()

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

def botao_editar_usuario():
    nome = telaEditUsuarios.lineNome.text()
    cpf = telaEditUsuarios.lineCpf.text()
    funcao = telaEditUsuarios.lineFuncao.text()
    email = telaEditUsuarios.lineEmail.text()
    senha = telaEditUsuarios.lineSenha.text()
    if telaEditUsuarios.rbtnAtivo.isChecked():
        situacao = "Ativo"
    else:
        situacao = "Inativo"
    if telaEditUsuarios.rbtnUsuario.isChecked():
        tipo_usuario = "Usuário"
    else:
        tipo_usuario = "Administrador"
    editar_banco(nome, cpf, email, senha, funcao, situacao, tipo_usuario)

def cadastrar_banco(nome, cpf, email, senha,funcao, situacao,tipo_usuario):

    if nome == "" or cpf == "" or email == "" or senha == "" or funcao == "":
        QMessageBox.about(telaCadUsuarios,"Alerta","Obrigatório o preenchimento de todos os campos.")
    else:
        if len(cpf) < 11:
            QMessageBox.about(telaCadUsuarios, "Alerta", "CPF Inválido.")
        else:
            verifica_existente = Autenticar_Banco(cpf, senha)
            if verifica_existente != None and verifica_existente != "Erro":
                QMessageBox.about(telaCadUsuarios, "Alerta", "CPF já cadastrado no banco de dados.")
            else:
                Querys.cadastrar(comandos_db_usuarios, nome, cpf, email, senha,funcao, situacao, tipo_usuario)
                QMessageBox.about(telaCadUsuarios,"Mensagem","Usuário cadastrado com sucesso.")

def editar_banco(nome, cpf, email, senha,funcao, situacao,tipo_usuario):
    if nome == "" or cpf == "" or email == "" or senha == "" or funcao == "":
        QMessageBox.about(telaEditUsuarios,"Alerta","Obrigatório o preenchimento de todos os campos.")
    else:
        if len(cpf) < 11:
            QMessageBox.about(telaEditUsuarios, "Alerta", "CPF Inválido.")
        else:
            verifica_existente = Autenticar_Banco(cpf, senha)
            if verifica_existente != None and verifica_existente != "Erro":
                QMessageBox.about(telaEditUsuarios, "Alerta", "CPF já cadastrado no banco de dados.")
            else:
                Querys.editar(comandos_db_usuarios, nome, cpf, email, senha,funcao, situacao, tipo_usuario)
                QMessageBox.about(telaEditUsuarios,"Mensagem","Cadastro alterado com sucesso.")

def Autenticar_Banco(usuario, senha):
    cad_encontrado = Querys_Autenticacao.Autenticar(Querys_Autenticacao('estoque.db'),usuario, senha)
    return cad_encontrado

def pesquisar_banco(nome):
    pesquisa = Querys_Autenticacao.buscar_banco(Querys_Autenticacao('estoque.db'), nome)
    return pesquisa

def botao_pesquisar():
    nome = telaConsUsuarios.lineNome.text()
    resultado = pesquisar_banco(nome)
    l = 0
    c = 0
    for item in resultado:
        for colItem in item:
            newItem = QTableWidgetItem(str(colItem))
            telaConsUsuarios.tableWidget.setItem(l,c,newItem)
            c += 1
        l += 1


telaCadUsuarios=uic.loadUi("cadUsuarios.ui")
telaCadUsuarios.btnVoltar.clicked.connect(cad_voltar)
telaCadUsuarios.btnLimpar.clicked.connect(cad_limpar)
telaCadUsuarios.btnCadastrar.clicked.connect(cadastrar)


telaConsUsuarios = uic.loadUi("consultarUsuarios.ui")
telaConsUsuarios.btnVoltar.clicked.connect(cons_voltar)
telaConsUsuarios.btnNovo.clicked.connect(botao_novocad)
telaConsUsuarios.btnPesquisar.clicked.connect(botao_pesquisar)
telaConsUsuarios.btnEditar.clicked.connect(botao_editar)
#telaConsUsuarios.btnExcluir.clicked.connect()


telaEditUsuarios=uic.loadUi("editarUsuarios.ui")
telaEditUsuarios.btnVoltar.clicked.connect(edit_voltar)
telaEditUsuarios.btnLimpar.clicked.connect(edit_limpar)
telaEditUsuarios.btnSalvar.clicked.connect(botao_editar_usuario)

telaConsUsuarios.show()
app.exec()