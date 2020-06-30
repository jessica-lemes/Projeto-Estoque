from Interface import cadProdutosMain, home_menus, consultaProdutosMain


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
        if home_menus.HomeMain.switch_cons_produtos:
            self.menus.switch_window.connect(self.show_consulta_produtos)
        elif home_menus.HomeMain.switch_cad_produtos:
            self.menus.switch_window.connect(self.show_cad_produtos)


    def show_cad_produtos(self):
        self.cad_produtos = cadProdutosMain.CadProdutos()
        self.cad_produtos.switch_window.connect(self.show_main)
        self.menus.close()
        self.cad_produtos.show()

    def show_consulta_produtos(self):
        self.consulta_produtos = consultaProdutosMain.ConsultaProdutos()
        self.consulta_produtos.switch_window.connect(self.show_main)
        self.menus.close()
        self.consulta_produtos.show()

