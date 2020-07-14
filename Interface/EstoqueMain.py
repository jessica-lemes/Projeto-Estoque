from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from PyQt5.Qt import QTableWidgetItem
from Banco.Movimentacao_dados import Querys_movimentacao
from Banco.cadProdutosDB import CadProdutosDB
from Banco.db_estoque import Querys
from Interface import consultarEstoque, editarEstoque, app_data

app=QtWidgets.QApplication([])

comandos_db_usuarios = Querys('estoque.db')
comandos_db_movimentacao = Querys_movimentacao('estoque.db')
comandos_db_produto = CadProdutosDB()

class Consultar(QMainWindow, consultarEstoque.Ui_MainWindow):
    def __init__(self, parent=None):

        super().__init__(parent)
        super().setupUi(self)

        self.btnVoltar.clicked.connect(self.cons_voltar)
        self.btnPesquisar.clicked.connect(self.botao_pesquisar)
        self.actionSair.triggered.connect(self.cons_voltar)
        self.btnEditar.clicked.connect(self.permissao)

        self.janela_principal = parent

    def permissao(self):
        permissaoUsuario = app_data.__userPermissao__
        if permissaoUsuario != "admin":
            QMessageBox.about(self, "Mensagem", "Somente para administradores.")
        else:
            self.botao_editar()


    def cons_voltar(self):
        self.close()

    def botao_pesquisar(self):

        nome = self.lineProduto.text()
        resultado = self.pesquisar_banco(nome)

        l = 0
        c = 0
        for item in resultado:
            c=0
            for colItem in item:
                newItem = QTableWidgetItem(str(colItem))
                self.tableWidget.setItem(l,c,newItem)
                c += 1
            l += 1
        self.lineProduto.setText('')

    def pesquisar_banco(self, nome):
        pesquisa = Querys.buscar_banco(Querys('estoque.db'), nome)
        return pesquisa

    def botao_editar(self):
        row = self.tableWidget.currentRow()
        id = self.tableWidget.item(row, 0).text()
        lista = self.buscar_id_bd(int(id))
        self.close()

        tela_editar = Editar(self)
        tela_editar.show()
        tela_editar.lineCodigo.setText(str(lista[0][0]))
        tela_editar.lineNomeProduto.setText(str(lista[0][1]))
        tela_editar.lineDescricao.setText(str(lista[0][2]))
        tela_editar.labelQntEstoque.setText(str(lista[0][3]))
        tela_editar.lineAtualizar.setText(str(lista[0][3]))

    def buscar_id_bd(self, id):
        lista = Querys.selecionar_id(comandos_db_usuarios, id)
        return lista

class Editar(QMainWindow, editarEstoque.Ui_editarEstoque):
    def __init__(self, parent=None):

        super().__init__(parent)
        super().setupUi(self)

        self.btnVoltar.clicked.connect(self.botao_voltar)
        self.btnLimpar.clicked.connect(self.botao_limpar)
        self.actionSair.triggered.connect(self.botao_voltar)
        self.btnSalvar.clicked.connect(self.botao_salvar)
        self.janela_principal = parent

    def botao_voltar(self):
        self.close()

    def botao_limpar(self):
        self.lineCodigo.setText('')
        self.lineNomeProduto.setText('')
        self.lineDescricao.setText('')
        self.labelQntEstoque.setText('')
        self.lineAtualizar.setText('')

    def botao_salvar(self):
        id = self.lineCodigo.text()
        qtde_estoque = self.lineAtualizar.text()
        idUsuario = app_data.__userId__
        self.salvaAlteracaoEstoque(qtde_estoque, id, idUsuario)
        self.close()

    def salvaAlteracaoEstoque(self, qtde_estoque, idProduto, idUsuario_FK):
        tela_edita_estoque = Editar(self)
        tela_consulta = Consultar(self)
        if qtde_estoque == "":
            QMessageBox.about(tela_edita_estoque,"Alerta","Obrigatório o preenchimento do campo.")
        else:
            tipo_mov = self.define_tipo_mov(idProduto,qtde_estoque)
            quantidade_mov = self.define_quantidade_mov(idProduto,qtde_estoque)

            Querys.atualizar_estoque(comandos_db_usuarios, qtde_estoque, idProduto)
            Querys_movimentacao.cadastra_movimentacao(comandos_db_movimentacao, tipo_mov, quantidade_mov, idProduto, idUsuario_FK)
            QMessageBox.about(tela_edita_estoque,"Mensagem","Estoque alterado com sucesso.")
            tela_consulta.show()

    def define_tipo_mov(self, idProduto, qtde_estoque):
        produto = CadProdutosDB.selecionar(comandos_db_produto, idProduto)
        qnt_produto_antes = produto[0][3]
        if int(qnt_produto_antes) > int(qtde_estoque):
            return "baixa"
        else:
            return "entrada"

    def define_quantidade_mov(self, idProduto, qtde_estoque):
        produto = CadProdutosDB.selecionar(comandos_db_produto, idProduto)
        qnt_produto_antes = produto[0][3]
        diferenca = int(qnt_produto_antes) - int(qtde_estoque)
        return abs(diferenca)

