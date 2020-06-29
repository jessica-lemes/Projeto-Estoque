from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QApplication
from PyQt5.Qt import QTableWidgetItem, QAbstractItemView
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
    telaEditUsuarios.labelId.setText("")

def botao_novocad():
    telaConsUsuarios.close()
    telaCadUsuarios.show()

def botao_editar():
    row = telaConsUsuarios.tableWidget.currentRow()
    id = telaConsUsuarios.tableWidget.item(row, 0).text()
    lista = buscar_id_bd(int(id))

    telaEditUsuarios.lineNome.setText(str(lista[0][1]))
    telaEditUsuarios.lineCpf.setText(lista[0][2])
    telaEditUsuarios.lineFuncao.setText(lista[0][3])
    telaEditUsuarios.lineEmail.setText(lista[0][4])
    telaEditUsuarios.lineSenha.setText(lista[0][5])
    if lista[0][6] == "Ativo":
        telaEditUsuarios.rbtnAtivo.setChecked(True)
    else:
        telaEditUsuarios.rbtnInativo.setChecked(True)
    if lista[0][7] == "Usuário":
        telaEditUsuarios.rbtnUsuario.setChecked(True)
    else:
        telaEditUsuarios.rbtnAdmin.setChecked(True)

    telaEditUsuarios.labelId.setText(str(lista[0][0]))

    telaConsUsuarios.close()
    telaEditUsuarios.show()

def buscar_id_bd(id):
    lista = Querys.selecionar_id(comandos_db_usuarios, id)
    return lista

def botao_excluir():
    row = telaConsUsuarios.tableWidget.currentRow()
    id = telaConsUsuarios.tableWidget.item(row, 0).text()
    Querys.excluir(comandos_db_usuarios, id)
    QMessageBox.about(telaConsUsuarios, "Mensagem", "Cadastro excluído com sucesso.")
    telaConsUsuarios.tableWidget.clearContents()

def seleciona_linha(selection: list):
    listSelection = []
    for l in selection:
        telaConsUsuarios.tableWidget.selectedRow(l)
        listSelection.append()
        return listSelection

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
    cadastrar_banco(nome,cpf,funcao,email,senha,situacao,tipo_usuario)

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


    id = telaEditUsuarios.labelId.text()

    editar_banco(id, nome, cpf, email, senha, funcao, situacao, tipo_usuario)

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
                cad_limpar()


def editar_banco(id, nome, cpf, email, senha,funcao, situacao,tipo_usuario):
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
                Querys.editar(comandos_db_usuarios, nome, cpf, email, senha,funcao, situacao, tipo_usuario, id)
                QMessageBox.about(telaEditUsuarios,"Mensagem","Cadastro alterado com sucesso.")

def Autenticar_Banco(usuario, senha):
    cad_encontrado = Querys_Autenticacao.Autenticar(Querys_Autenticacao('estoque.db'),usuario, senha)
    return cad_encontrado

def pesquisar_banco(nome):
    pesquisa = Querys.buscar_banco(Querys('estoque.db'), nome)
    return pesquisa

def botao_pesquisar():
    telaConsUsuarios.tableWidget.clearContents()

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
    telaConsUsuarios.lineNome.setText('')


telaCadUsuarios=uic.loadUi("cadUsuarios.ui")
telaCadUsuarios.btnVoltar.clicked.connect(cad_voltar)
telaCadUsuarios.btnLimpar.clicked.connect(cad_limpar)
telaCadUsuarios.btnCadastrar.clicked.connect(cadastrar)

telaConsUsuarios = uic.loadUi("consultarUsuarios.ui")
telaConsUsuarios.btnVoltar.clicked.connect(cons_voltar)
telaConsUsuarios.btnNovo.clicked.connect(botao_novocad)
telaConsUsuarios.btnPesquisar.clicked.connect(botao_pesquisar)
telaConsUsuarios.btnEditar.clicked.connect(botao_editar)
telaConsUsuarios.btnExcluir.clicked.connect(botao_excluir)

telaEditUsuarios=uic.loadUi("editarUsuarios.ui")
telaEditUsuarios.btnVoltar.clicked.connect(edit_voltar)
telaEditUsuarios.btnLimpar.clicked.connect(edit_limpar)
telaEditUsuarios.btnSalvar.clicked.connect(botao_editar_usuario)

telaConsUsuarios.show()
app.exec()