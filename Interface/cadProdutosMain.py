from PyQt5.QtWidgets import QMainWindow, QMessageBox
from Interface import cadProdutos, home_menus
from Banco.cadProdutosDB import CadProdutosDB


class CadProdutos(QMainWindow, cadProdutos.Ui_cadProdutos):

    def __init__(self, parent=None):

        super(CadProdutos, self).__init__(parent)
        super().setupUi(self)
        self.btnCadastrar.clicked.connect(self.cadastra)
        self.btnLimpar.clicked.connect(self.limpar)
        self.btnVoltar.clicked.connect(self.voltar)

        self.actionSair.triggered.connect(self.voltar)
        self.janela_principal = parent

    def cadastra(self):
        self.cad_produtos = CadProdutosDB()
        self.cad_prod = CadProdutos()
        if self.lineNome.text()== "" or self.lineDescricao.text() == "" or self.lineQtd.text() == ""\
                or self.lineQtdMin.text() == "" or self.lineValor.text() == "":
            QMessageBox.about(self.cad_prod, "Erro", "Preecha todos os campos")
        else:
            nome = self.lineNome.text()
            descricao = self.lineDescricao.text()
            qtde_estoque = self.lineQtd.text()
            qtde_minimo = self.lineQtdMin.text()
            valor_produto = self.lineValor.text()

            self.cad_produtos.cadastrar(nome, descricao, qtde_estoque, qtde_minimo, valor_produto)
            QMessageBox.about(self.cad_prod, "Cadastro", "Cadastrado com sucesso!")
            self.limpar()

    def voltar(self):
        CadProdutos.close(self)

    def limpar(self):
        self.lineNome.setText('')
        self.lineDescricao.setText('')
        self.lineQtd.setText('')
        self.lineQtdMin.setText('')
        self.lineValor.setText('')
