from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.Qt import QTableWidgetItem
from Interface import consultaProdutos_, cadProdutosMain, editaProdutosMain
from Banco import cadProdutosDB


class ConsultaProdutos(QMainWindow, consultaProdutos_.Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnPesquisar.clicked.connect(self.pesquisar)
        self.actionsair.triggered.connect(self.voltar)
        self.btnNovo.clicked.connect(self.janela_cadastro)
        self.btnVoltar.clicked.connect(self.voltar)
        self.btnEditar.clicked.connect(self.editar)
        self.btnLimpar.clicked.connect(self.limpar)
        self.cons_prod = cadProdutosDB.CadProdutosDB()
        self.resultado = self.cons_prod.selecionar_todos()
        self.obj_edita = editaProdutosMain.EditaProdutosMain()

    def pesquisar(self):
        l = 0
        c = 0
        if self.lineEdit.text() == '':
            for item in self.resultado:
                for colItem in item:
                    newItem = QTableWidgetItem(str(colItem))
                    self.tabelaConsultaProdutos.setItem(l, c, newItem)
                    c += 1
                l += 1
        elif self.lineEdit.text() != '':
            resultado = self.cons_prod.selecionar(self.lineEdit.text())
            for item in resultado:
                for colItem in item:
                    newItem = QTableWidgetItem(str(colItem))
                    self.tabelaConsultaProdutos.setItem(l,c, newItem)
                    c += 1
                l += 1
        elif self.cons_prod.selecionar(self.lineEdit.text()) == None:
            QMessageBox.about(ConsultaProdutos, "Erro", "Não encontrado")

    def editar(self):
        lista = []
        row = self.tabelaConsultaProdutos.currentRow()
        nome = self.tabelaConsultaProdutos.item(row, 1).text()
        lista = self.cons_prod.selecionar(nome)
        self.obj_edita.show()
        return lista



    def __getitem__(self, item):
        return self.resultado[item]

    def janela_cadastro(self):
        jan_cad = cadProdutosMain.CadProdutos(self)
        jan_cons = ConsultaProdutos(self)
        jan_cons.close()
        jan_cad.show()

    def voltar(self):
        ConsultaProdutos.close(self)

    def limpar(self):
        self.tabelaConsultaProdutos.clearContents()
