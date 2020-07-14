from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from Interface import Home, cadProdutosMain, consultaProdutosMain, UsuariosMain, EstoqueMain, MovimentacaoMain, app_data, comandos_login
from Banco import cadProdutosDB
from Banco.menu_dados import Dados_Menu
from datetime import datetime

class HomeMain(QMainWindow, Home.Ui_Home):

    def __init__(self, parent=None):
        super(HomeMain, self).__init__(parent)
        super().setupUi(self)

        self.CadastrarProdutos.triggered.connect(self.permissao_novo_cad_produtos)
        self.ConsultarProdutos.triggered.connect(self.switch_cons_produtos)
        self.menuLogout.triggered.connect(self.sair)
        self.ConsultarUsuario.triggered.connect(self.permissao_consulta_usuario)
        self.CadastrarUsuario.triggered.connect(self.permissao_novo_cad_usuario)
        self.ConsultarEstoque.triggered.connect(self.switch_cons_estoque)
        self.ConsultarMovimentacao.triggered.connect(self.switch_movimentacao)
        self.Logout.triggered.connect(self.switch_login)
        obj_cad_db = cadProdutosDB.CadProdutosDB()
        self.Atualizar.triggered.connect(self.listar_dados)
        self.listar_dados()

    def permissao_consulta_usuario(self):
        permissaoUsuario = app_data.__userPermissao__
        if permissaoUsuario != "admin":
            QMessageBox.about(self, "Mensagem", "Somente para administradores.")
        else:
            self.ConsultarUsuario.triggered.connect(self.switch_cons_usuarios)

    def permissao_novo_cad_usuario(self):
        permissaoUsuario = app_data.__userPermissao__
        if permissaoUsuario != "admin":
            QMessageBox.about(self, "Mensagem", "Somente para administradores.")
        else:
            self.CadastrarUsuario.triggered.connect(self.switch_cad_usuarios)

    def permissao_novo_cad_produtos(self):
        permissaoUsuario = app_data.__userPermissao__
        if permissaoUsuario != "admin":
            QMessageBox.about(self, "Mensagem", "Somente para administradores.")
        else:
            self.CadastrarProdutos.triggered.connect(self.switch_cad_produtos)

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

    def switch_cad_usuarios(self):
        cad_usuarios = UsuariosMain.CadastraUsuarios(self)
        cad_usuarios.show()

    def switch_cons_estoque(self):
        cons_estoque = EstoqueMain.Consultar(self)
        cons_estoque.show()

    def estoque_baixo(self):
        resultado = Dados_Menu.estoque_baixo(Dados_Menu('estoque.db'))
        return resultado

    def listar_dados(self):
        self.listWidget.clear()
        dado_lido = self.estoque_baixo()
        if len(dado_lido) > 0:
            data_e_hora = datetime.now()
            controle_atualizacao = data_e_hora.strftime('%d/%m/%Y %H:%M')
            self.label_atualizacao.setText("Última atualização: "+controle_atualizacao)
            self.listWidget.addItem("Você tem itens com estoque baixo!! \n")
            for item in dado_lido:
                self.listWidget.addItem("Estoque de: "+ item[1]+" "+item[2]+" = "+str(item[3]))
                self.listWidget.addItem("")
        else:
            self.listWidget.addItem("Parabéns! Seu estoque está abastecido conforme o esperado! =D")

    def switch_movimentacao(self):
        movimentacao = MovimentacaoMain.Movimentacao(self)
        movimentacao.show()

    def switch_login(self):
        login = comandos_login.Login(self)
        self.listar_dados()
        login.show()
