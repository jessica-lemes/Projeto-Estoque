from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
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
        self.cons_prod = cadProdutosDB.CadProdutosDB("estoque.db")


    def pesquisar(self, id = None):
        l=0
        c=0
        if self.lineEdit == '':
            resultado = self.cons_prod.selecionar_todos
            for item in resultado:
                for colItem in item:
                    newItem = QTableWidgetItem(str(colItem))
                    self.tabelaConsultaProdutos.setItem(l, c, newItem)
                    c += 1
                l += 1
        else:
            return False

    def janela_cadastro(self):
        jan_cad = cadProdutosMain.CadProdutos(self)
        jan_cons = ConsultaProdutos(self)
        jan_cons.close()
        jan_cad.show()



    def voltar(self):
        ConsultaProdutos.close(self)

