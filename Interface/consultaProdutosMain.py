from PyQt5.QtWidgets import QMainWindow
from Interface import consultaProdutos


class ConsultaProdutos(QMainWindow, consultaProdutos.Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnPesquisar.clicked.connect(self.pesquisar)


    def pesquisar(self, produto_nome):
        pass