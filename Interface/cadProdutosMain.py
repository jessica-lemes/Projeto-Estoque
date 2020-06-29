import sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore
from Interface import cadProdutos
from Banco.cadProdutosDB import CadProdutosDB
from Interface import controller


class CadProdutos(QMainWindow, cadProdutos.Ui_cadProdutos):

    switch_window = QtCore.pyqtSignal()

    def __init__(self, parent=None):

        super(CadProdutos, self).__init__(parent)
        super().setupUi(self)
        self.btnCadastrar.clicked.connect(self.cadastra)
        self.btnLimpar.clicked.connect(self.limpar)
        self.btnVoltar.clicked.connect(self.voltar)
        self.cad_prod = CadProdutosDB('estoque.db')
        self.actionSair.triggered.connect(self.voltar)
        self.actionConsultar.triggered.connect(self.consultar)
        self.janela_principal = parent

    def cadastra(self):
        cad_produtos = CadProdutos()
        if self.lineNome.text()== "" or self.lineDescricao.text() == "" or self.lineQtd.text() == ""\
                or self.lineQtdMin.text() == "" or self.lineValor.text() == "":
            QMessageBox.about(cad_produtos,"Erro","Preecha todos os campos")
        else:
            nome = self.lineNome.text()
            descricao = self.lineDescricao.text()
            qtde_estoque = self.lineQtd.text()
            qtde_minimo = self.lineQtdMin.text()
            valor_produto = self.lineValor.text()

            self.cad_prod.cadastrar(nome, descricao, qtde_estoque, qtde_minimo, valor_produto)
            QMessageBox.about(cad_produtos,"Cadastro","Cadastrado com sucesso!")
            self.limpar()

    def consultar(self):
        pass

    def voltar(self):
        self.switch_window.emit()

    def limpar(self):
        self.lineNome.setText('')
        self.lineDescricao.setText('')
        self.lineQtd.setText('')
        self.lineQtdMin.setText('')
        self.lineValor.setText('')
