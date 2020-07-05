from PyQt5 import QtCore, Qt, QtWidgets, QtGui
from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.Qt import QTableWidgetItem
from Interface import consultaProdutos_, cadProdutosMain
from Banco import cadProdutosDB


class ConsultaProdutos(QMainWindow, consultaProdutos_.Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnPesquisar.clicked.connect(self.pesquisar)
        self.actionsair.triggered.connect(self.voltar)
        self.btnNovo.clicked.connect(self.janela_cadastro)
        self.btnVoltar.clicked.connect(self.voltar)
        self.tabelaConsultaProdutos = QTableWidgetItem

    # def pesquisar(self):
    #     cons_prod = cadProdutosDB.CadProdutosDB()
    #     resultado = cons_prod.selecionar_todos()
    #
    #     self.model = TableModel(resultado)
    #     self.tabelaConsultaProdutos.setModel(self.model)
    #     self.setCentralWidget(self.tabelaConsultaProdutos)

    def pesquisar(self):
        l=0
        c=0
        if self.lineEdit.text() == '':
            cons_prod = cadProdutosDB.CadProdutosDB()
            resultado = cons_prod.selecionar_todos()
            print(resultado)
            for item in resultado:
                c = 0
                for colItem in item:
                    newItem = QTableWidgetItem(str(colItem))
                    self.tabelaConsultaProdutos.setItem(l,c,newItem)
                    c+=1
                l+=1
        elif self.lineEdit.text() != '':
            cons_prod = cadProdutosDB.CadProdutosDB()
            resultado = cons_prod.selecionar(self.lineEdit.text())
            for item in resultado:
                for colItem in item:
                    newItem = QTableWidgetItem(colItem)
                    self.tabelaConsultaProdutos.tableWidget.setItem(l,c, newItem)
                    c += 1
                l += 1
        else:
            QMessageBox.about(ConsultaProdutos, "Erro", "Não encontrado")



    def __getitem__(self, item):
        return self.resultado[item]

    def janela_cadastro(self):
        jan_cad = cadProdutosMain.CadProdutos(self)
        jan_cons = ConsultaProdutos(self)
        jan_cons.close()
        jan_cad.show()

    def voltar(self):
        ConsultaProdutos.close(self)


# class TableModel(QtCore.QAbstractTableModel):
#     def __init__(self, dados):
#         super(TableModel, self).__init__()
#         self.dados = dados
#
#     def data(self, index, role):
#         if role == Qt.DisplayRole:
#             return self.dados[index.row()][index.column()]
#
#     def rowCount(self, index):
#         return self.dados.count(self.dados[0])
#
#     def columnCount(self, index):
#         return self.dados.count(self.dados[0])