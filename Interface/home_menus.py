from PyQt5.QtWidgets import QMainWindow, QWidget
from Interface import Home, cadProdutosMain, consultaProdutosMain



class HomeMain(QMainWindow, Home.Ui_Home):

    def __init__(self, parent=None):
        super(HomeMain, self).__init__(parent)
        super().setupUi(self)

        self.CadastrarProdutos.triggered.connect(self.switch_cad_produtos)
        self.ConsultarProdutos.triggered.connect(self.switch_cons_produtos)
        self.menuLogout.triggered.connect(self.sair)

    def switch_cad_produtos(self):
        cad_produtos = cadProdutosMain.CadProdutos(self)
        cad_produtos.show()
        home = HomeMain()
        home.close()


    def switch_cons_produtos(self):
        cons_produtos = consultaProdutosMain.ConsultaProdutos(self)
        cons_produtos.show()
        home = HomeMain()
        home.close()

    def sair(self):
        HomeMain.close(self)