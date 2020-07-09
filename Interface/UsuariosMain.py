from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.Qt import QTableWidgetItem
from Interface import consultarEstoque, consultarUsuarios,cadUsuarios, editarUsuarios, Home
from Banco.estoque_db_querys_usuarios import Querys

app=QtWidgets.QApplication([])
telaHome=uic.loadUi("Home.ui")

comandos_db_usuarios = Querys('estoque.db')

class ConsultaUsuarios(QMainWindow, consultarUsuarios.Ui_MainWindow):
    def __init__(self, parent=None):

        super().__init__(parent)
        super().setupUi(self)

        self.btnVoltar.clicked.connect(self.cons_voltar)
        self.btnNovo.clicked.connect(self.botao_novocad)
        self.btnPesquisar.clicked.connect(self.botao_pesquisar)
        self.btnEditar.clicked.connect(self.botao_editar)
        self.btnExcluir.clicked.connect(self.botao_excluir)
        self.actionSair.triggered.connect(self.cons_voltar)
        self.janela_principal = parent

    def cons_voltar(self):
        self.close()

    def botao_novocad(self):
        #self.close()
        tela_cad_usuarios = CadastraUsuarios(self)
        tela_cons_usuarios = ConsultaUsuarios(self)
        #tela_cons_usuarios.close()
        tela_cad_usuarios.show()

    def botao_pesquisar(self):
        self.tableWidget.clearContents()

        nome = self.lineNome.text()
        resultado = self.pesquisar_banco(nome)
        l = 0
        c = 0
        for item in resultado:
            c = 0
            for colItem in item:
                newItem = QTableWidgetItem(str(colItem))
                self.tableWidget.setItem(l, c, newItem)
                c += 1
            l += 1
        self.lineNome.setText('')

    def pesquisar_banco(self, nome):
        pesquisa = Querys.buscar_banco(Querys('estoque.db'), nome)
        return pesquisa

    def buscar_id_bd(self, id):
        lista = Querys.selecionar_id(comandos_db_usuarios, id)
        return lista

    def botao_editar(self):

        row = self.tableWidget.currentRow()
        id = self.tableWidget.item(row, 0).text()
        lista = self.buscar_id_bd(int(id))

        tela_editar = EditarUsuario(self)
        tela_editar.show()
        tela_editar.seta_linhas(lista)
        tela_cons_usuarios = ConsultaUsuarios(self)
        tela_cons_usuarios.close()
        self.close()

    def botao_excluir(self):
        row = self.tableWidget.currentRow()
        id = self.tableWidget.item(row, 0).text()
        Querys.excluir(comandos_db_usuarios, id)
        cons_usuarios = ConsultaUsuarios(self)
        QMessageBox.about(cons_usuarios, "Mensagem", "Cadastro excluído com sucesso.")
        self.tableWidget.clearContents()

    def seleciona_linha(self, selection: list):
        listSelection = []
        for l in selection:
            self.consultarUsuarios.tableWidget.selectedRow(l)
            listSelection.append()
            return listSelection

class CadastraUsuarios(QMainWindow, cadUsuarios.Ui_cadUsuarios):
    def __init__(self, parent=None):

        super().__init__(parent)
        super().setupUi(self)

        self.btnVoltar.clicked.connect(self.cad_voltar)
        self.btnCadastrar.clicked.connect(self.cadastrar)
        self.btnLimpar.clicked.connect(self.cad_limpar)

        self.actionSair.triggered.connect(self.cad_voltar)
        self.janela_principal = parent

    def cad_voltar(self):
        self.close()

    def cad_limpar(self):
        self.lineNome.setText("")
        self.lineCpf.setText("")
        self.lineFuncao.setText("")
        self.lineEmail.setText("")
        self.lineSenha.setText("")
        self.rbtnAtivo.setChecked(True)
        self.rbtnUsuario.setChecked(True)

    def cadastrar(self):
        nome = self.lineNome.text()
        cpf = self.lineCpf.text()
        funcao = self.lineFuncao.text()
        email = self.lineEmail.text()
        senha = self.lineSenha.text()
        if self.rbtnAtivo.isChecked():
            situacao = "Ativo"
        else:
            situacao = "Inativo"
        if self.rbtnUsuario.isChecked():
            tipo_usuario = "Usuário"
        else:
            tipo_usuario = "Administrador"
        self.cadastrar_banco(nome, cpf, email, senha, funcao, situacao, tipo_usuario)

    def cadastrar_banco(self, nome, cpf, email, senha, funcao, situacao, tipo_usuario):
        tela_cadastrar = CadastraUsuarios(self)
        if nome == "" or cpf == "" or email == "" or senha == "" or funcao == "":
            QMessageBox.about(tela_cadastrar, "Alerta", "Obrigatório o preenchimento de todos os campos.")
        else:
            if len(cpf) < 11:
                QMessageBox.about(tela_cadastrar, "Alerta", "CPF Inválido.")
            else:
                verifica_existente = Querys.Verifica_se_existe(comandos_db_usuarios, cpf)
                if verifica_existente is True and verifica_existente != "Erro":
                    QMessageBox.about(tela_cadastrar, "Alerta", "CPF já cadastrado no banco de dados.")
                else:
                    Querys.cadastrar(comandos_db_usuarios, nome, cpf, email, senha, funcao, situacao, tipo_usuario)
                    QMessageBox.about(tela_cadastrar, "Mensagem", "Usuário cadastrado com sucesso.")
                    self.cad_limpar()

class EditarUsuario(QMainWindow, editarUsuarios.Ui_editUsuarios):

    def __init__(self, parent=None):

        super(EditarUsuario, self).__init__(parent)
        super().setupUi(self)

        self.btnVoltar.clicked.connect(self.edit_voltar)
        self.btnSalvar.clicked.connect(self.botao_editar_usuario)
        self.btnLimpar.clicked.connect(self.edit_limpar)

        self.actionSair.triggered.connect(self.edit_voltar)
        self.janela_principal = parent

    def edit_voltar(self):
        tela_cons_usuarios = ConsultaUsuarios(self)
        tela_cons_usuarios.show()
        self.close()

    def edit_limpar(self):
        self.lineNome.setText("")
        self.lineCpf.setText("")
        self.lineFuncao.setText("")
        self.lineEmail.setText("")
        self.lineSenha.setText("")
        self.rbtnAtivo.setChecked(True)
        self.rbtnUsuario.setChecked(True)
        self.labelId.setText("")

    def seta_linhas(self, lista):

        self.lineNome.setText(str(lista[0][1]))
        self.lineCpf.setText(str(lista[0][2]))
        self.lineFuncao.setText(str(lista[0][3]))
        self.lineEmail.setText(str(lista[0][4]))
        self.lineSenha.setText(str(lista[0][5]))
        if str(lista[0][6]) == "Ativo":
            self.rbtnAtivo.setChecked(True)
        else:
            self.rbtnInativo.setChecked(True)
        if str(lista[0][7]) == "Usuário":
            self.rbtnUsuario.setChecked(True)
        else:
            self.rbtnAdmin.setChecked(True)

        self.labelId.setText(str(lista[0][0]))

    def botao_editar_usuario(self):
        nome = self.lineNome.text()
        cpf = self.lineCpf.text()
        funcao = self.lineFuncao.text()
        email = self.lineEmail.text()
        senha = self.lineSenha.text()
        if self.rbtnAtivo.isChecked():
            situacao = "Ativo"
        else:
            situacao = "Inativo"
        if self.rbtnUsuario.isChecked():
            tipo_usuario = "Usuário"
        else:
            tipo_usuario = "Administrador"
        id = self.labelId.text()

        self.editar_banco(id, nome, cpf, email, senha, funcao, situacao, tipo_usuario)

    def editar_banco(self, id, nome, cpf, email, senha,funcao, situacao,tipo_usuario):
        tela_editar = EditarUsuario(self)

        if nome == "" or cpf == "" or email == "" or senha == "" or funcao == "":
            QMessageBox.about(tela_editar,"Alerta","Obrigatório o preenchimento de todos os campos.")
        else:
            if len(cpf) < 11:
                QMessageBox.about(tela_editar, "Alerta", "CPF Inválido.")
            else:
                verifica_existente = Querys.Verifica_se_existe(comandos_db_usuarios, cpf)
                if verifica_existente is True and verifica_existente != "Erro":
                    QMessageBox.about(tela_editar, "Alerta", "CPF já cadastrado no banco de dados.")
                else:
                    Querys.editar(comandos_db_usuarios, nome, cpf, email, senha,funcao, situacao, tipo_usuario, id)
                    QMessageBox.about(tela_editar,"Mensagem","Cadastro alterado com sucesso.")
                    self.edit_limpar()
