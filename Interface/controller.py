from Interface import Home, cadProdutosMain, home_menus


class Controller:

    def __init__(self):
        pass
    #
    # def show_login(self):
    #     self.login = Login()
    #     self.login.switch_window.connect(self.show_main)
    #     self.login.show()

    def show_main(self):
        self.menus = home_menus.HomeMain()
        self.menus.show()
        self.menus.switch_window.connect(self.show_cad_produtos)


    def show_cad_produtos(self):
        self.cad_produtos = cadProdutosMain.CadProdutos()
        self.menus.close()
        self.cad_produtos.switch_window.connect(self.show_main)
        self.cad_produtos.show()

    def show_consulta_produtos(self):
        pass

