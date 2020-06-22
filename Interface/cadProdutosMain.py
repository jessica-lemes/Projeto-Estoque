import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from Interface import cadProdutos
from Banco.cadProdutosDB import CadProdutosDB


class CadProdutos(QMainWindow, cadProdutos.Ui_cadProdutos):

    def __init__(self, parent=None):

        super().__init__(parent)
        super().setupUi(self)
        self.btnCadastrar.clicked.connect(self.cadastra)
        self.btnLimpar.clicked.connect(self.limpar)
        self.btnVoltar.clicked.connect(self.voltar)
        self.cad_prod = CadProdutosDB('estoque.db')
        self.actionSair.triggered.connect(self.voltar)
        self.actionConsultar.triggered.connect(self.consultar)

    def cadastra(self):

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

        cad_produtos.close()
        telaHome.show()

    def limpar(self):

        self.lineNome.setText('')
        self.lineDescricao.setText('')
        self.lineQtd.setText('')
        self.lineQtdMin.setText('')
        self.lineValor.setText('')


if __name__ == '__main__':

    qt = QApplication(sys.argv)
    cad_produtos = CadProdutos()
    cad_produtos.show()
    telaHome = uic.loadUi("Home.ui")
    qt.exec_()
