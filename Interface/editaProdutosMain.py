from PyQt5.QtWidgets import QMainWindow, QMessageBox
from Interface import editaProdutos
from Banco import cadProdutosDB
import sqlite3

class EditaProdutosMain(QMainWindow, editaProdutos.Ui_editaProdutos):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnConfirmar.clicked.connect(self.editar)
        self.btnVoltar.clicked.connect(self.voltar)
        self.btnLimpar.clicked.connect(self.limpar)
        self.objDB = cadProdutosDB.CadProdutosDB

    def limpar(self):
        self.lineNome.setText("")
        self.lineDescricao("")
        self.lineQtd("")
        self.lineQtdMin("")
        self.lineValor("")

    def voltar(self):
        EditaProdutosMain.close(self)

    def editar(self):
        idProduto = self.lineEdit.text()
        nome = self.lineNome.text()
        descricao = self.lineDescricao.text()
        qtd = self.lineQtd.text()
        qtd_min = self.lineQtdMin.text()
        valor = self.lineValor.text()
        self.confirmar_edicao(nome, descricao, qtd, qtd_min, valor, idProduto)

    def confirmar_edicao(self, nome, descricao, qtd, qtd_min, valor, idProduto):

        self.objDB.alterar(nome, descricao, qtd, qtd_min, valor, idProduto)

        QMessageBox.about(EditaProdutosMain, "Update", "Alterado com sucesso!")

        QMessageBox.about(EditaProdutosMain, "Erro", "Não foi possível realizar operação")


        # def cadastra(self):
        #     self.cad_produtos = CadProdutosDB()
        #     self.cad_prod = CadProdutos()
        #     if self.lineNome.text() == "" or self.lineDescricao.text() == "" or self.lineQtd.text() == "" \
        #             or self.lineQtdMin.text() == "" or self.lineValor.text() == "":
        #         QMessageBox.about(self.cad_prod, "Erro", "Preecha todos os campos")
        #     else:
        #         nome = self.lineNome.text()
        #         descricao = self.lineDescricao.text()
        #         qtde_estoque = self.lineQtd.text()
        #         qtde_minimo = self.lineQtdMin.text()
        #         valor_produto = self.lineValor.text()
        #
        #         self.cad_produtos.cadastrar(nome, descricao, qtde_estoque, qtde_minimo, valor_produto)
        #         QMessageBox.about(self.cad_prod, "Cadastro", "Cadastrado com sucesso!")
        #         self.limpar()