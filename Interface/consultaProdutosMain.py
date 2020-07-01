from PyQt5.QtWidgets import QMainWindow
from Interface import consultaProdutos_, cadProdutosMain
from Banco import cadProdutosDB

class ConsultaProdutos(QMainWindow, consultaProdutos_.Ui_MainWindow):


    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnPesquisar.clicked.connect(self.pesquisar)
        self.actionsair.triggered.connect(self.sair)
        self.btnNovo.clicked.connect(self.janela_cadastro)

    def pesquisar(self, id = None):
        pesquisa = cadProdutosDB.CadProdutosDB()
        if self.lineEdit == '':
            pesquisa = pesquisa.selecionar_todos()
            self.tabelaConsultaProdutos.

        else:
            pesquisa = pesquisa.selecionar(id)


    def janela_cadastro(self):
        jan_cad = cadProdutosMain.CadProdutos(self)
        jan_cons = ConsultaProdutos(self)
        jan_cons.close()
        jan_cad.show()



    def sair(self):
        pass