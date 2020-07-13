from PyQt5.QtWidgets import QMainWindow,QWidget
from PyQt5 import QtWidgets
from Interface import Home, cadProdutosMain, consultaProdutosMain, UsuariosMain, EstoqueMain, MovimentacaoMain
from Banco.menu_dados import Dados_Menu



class HomeMain(QMainWindow, Home.Ui_Home):

    def __init__(self, parent=None):
        super(HomeMain, self).__init__(parent)
        super().setupUi(self)

        self.CadastrarProdutos.triggered.connect(self.switch_cad_produtos)
        self.ConsultarProdutos.triggered.connect(self.switch_cons_produtos)
        self.menuLogout.triggered.connect(self.sair)
        self.ConsultarUsuario.triggered.connect(self.switch_cons_usuarios)
        self.CadastrarUsuario.triggered.connect(self.switch_cad_usuarios)
        self.ConsultarEstoque.triggered.connect(self.switch_cons_estoque)
        self.ConsultarMovimentacao.triggered.connect(self.switch_movimentacao)

        self.listar_dados()

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

    def switch_cons_usuarios(self):
        cons_usuarios = UsuariosMain.ConsultaUsuarios(self)
        cons_usuarios.show()
        home = HomeMain()
        home.close()

    def switch_cad_usuarios(self):
        cad_usuarios = UsuariosMain.CadastraUsuarios(self)
        cad_usuarios.show()
        home = HomeMain()
        home.close()

    def switch_cons_estoque(self):
        cons_estoque = EstoqueMain.Consultar(self)
        cons_estoque.show()
        home = HomeMain()
        home.close()

    def estoque_baixo(self):
        resultado = Dados_Menu.estoque_baixo(Dados_Menu('estoque.db'))
        return resultado

    def listar_dados(self):
        dado_lido = self.estoque_baixo()
        if len(dado_lido) > 0:
            self.listWidget.addItem("Produtos com estoque baixo: \n")
            for item in dado_lido:
                self.listWidget.addItem("Produto: "+ item[1]+" "+item[2]+" - Quantidade em estoque = "+str(item[3]))
                self.listWidget.addItem("")
        else:
            self.listWidget.addItem("Parabéns! Seu estoque está abastecido conforme o esperado!!")

    def switch_movimentacao(self):
        movimentacao = MovimentacaoMain.Movimentacao(self)
        movimentacao.show()
        home = HomeMain()
        home.close()