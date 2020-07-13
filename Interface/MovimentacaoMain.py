from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem

from Banco.Movimentacao_dados import Querys_movimentacao
from Interface import consultarMovimentacao

app=QtWidgets.QApplication([])


class Movimentacao(QMainWindow, consultarMovimentacao.Ui_MainWindow):
    def __init__(self, parent=None):

        super().__init__(parent)
        super().setupUi(self)

        self.btnVoltar.clicked.connect(self.voltar)
        self.btnPesquisar.clicked.connect(self.botao_pesquisar)
        self.actionSair.triggered.connect(self.voltar)
        self.janela_principal = parent

    def voltar(self):
        self.close()

    def pesquisar_banco(self, produto, data, tipo, usuario):
        pesquisa = Querys_movimentacao.buscar_banco(Querys_movimentacao('estoque.db'), produto, data, tipo, usuario)
        return pesquisa

    def botao_pesquisar(self):
        self.tableWidget.clearContents()

        produto = self.lineProduto.text()
        data = self.lineData.text()
        tipo = self.lineTipo.text()
        usuario = self.lineUsuario.text()

        resultado = self.pesquisar_banco(produto, data, tipo, usuario)

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
        self.lineData.setText('')
        self.lineTipo.setText('')
        self.lineUsuario.setText('')


