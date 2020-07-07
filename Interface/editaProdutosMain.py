from PyQt5.QtWidgets import QMainWindow, QMessageBox
from Interface import editaProdutos, consultaProdutosMain
from Banco import cadProdutosDB

class EditaProdutosMain(QMainWindow, editaProdutos.Ui_editaProdutos):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnConfirmar.clicked.connect(self.confirmar_edicao)
        self.btnVoltar.clicked.connect(self.voltar)
        self.btnLimpar.clicked.connect(self.limpar)
        self.objCons = consultaProdutosMain.ConsultaProdutos()
        self.objDB = cadProdutosDB.CadProdutosDB()



    def limpar(self):
        self.tabelaConsultaProdutos.clearContents()

    def voltar(self):
        EditaProdutosMain.close(self)

    def editar(self):
        lista = []
        lista = self.objCons.editar()
        nome = self.lineNome.setText(str(lista[0][1]))
        descricao = self.lineDescricao.lineCpf.setText(str(lista[0][2]))
        qtd = self.lineQtd.setText(str(lista[0][3]))
        qtd_min = self.lineQtdMin.setText(str(lista[0][4]))
        valor = self.lineValor.setText(str(lista[0][5]))
        self.confirmar_edicao(nome, descricao, qtd, qtd_min, valor)

    def confirmar_edicao(self, nome, descricao, qtd, qtd_min, valor):
        if self.objDB.alterar(nome, descricao, qtd, qtd_min, valor):

            QMessageBox.about(EditaProdutosMain, "Update", "Alterado com sucesso!")
        else:
            QMessageBox.about(EditaProdutosMain, "Erro", "Não foi possível realizar operação")


        # def cadastra(self):
        #     self.cad_produtos = CadProdutosDB()
        #     self.cad_prod = CadProdutos()
        #     if self.lineNome.text() == "" or self.lineDescricao.text() == "" or self.lineQtd.text() == "" \
        #             or self.lineQtdMin.text() == "" or self.lineValor.text() == "":
        #         QMessageBox.about(self.cad_prod, "Erro", "Preecha todos os campos")
        #     else:
        #         nome = self.lineNome.text()
        #         descricao = self.lineDescricao.text()
        #         qtde_estoque = self.lineQtd.text()
        #         qtde_minimo = self.lineQtdMin.text()
        #         valor_produto = self.lineValor.text()
        #
        #         self.cad_produtos.cadastrar(nome, descricao, qtde_estoque, qtde_minimo, valor_produto)
        #         QMessageBox.about(self.cad_prod, "Cadastro", "Cadastrado com sucesso!")
        #         self.limpar()