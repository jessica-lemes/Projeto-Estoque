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
        self.btnEditar.clicked.connect(self.abre_janela_edit)
        self.btnLimpar.clicked.connect(self.limpar)
        self.btnExcluir.clicked.connect(self.excluir)
        self.cons_prod = cadProdutosDB.CadProdutosDB()
        self.resultado = self.cons_prod.selecionar_todos()
        self.obj_edita = editaProdutosMain.EditaProdutosMain()
        self.Querys = cadProdutosMain.CadProdutos()
        self.cad_prod = cadProdutosDB.CadProdutosDB()


    def pesquisar(self):
        resultado = self.cons_prod.selecionar_todos()
        self.tabelaConsultaProdutos.clearContents()
        if self.lineEdit.text() == '':
            l = 0
            for item in resultado:
                c = 0
                for colItem in item:
                    newItem = QTableWidgetItem(str(colItem))
                    self.tabelaConsultaProdutos.setItem(l, c, newItem)
                    c += 1
                l += 1
        elif self.lineEdit.text() != '':
            resultado = self.cons_prod.selecionar(self.lineEdit.text())
            l=0
            c=0
            for item in resultado:
                c = 0
                for colItem in item:
                    newItem = QTableWidgetItem(str(colItem))
                    self.tabelaConsultaProdutos.setItem(l,c, newItem)
                    c += 1
                l += 1
        elif self.cons_prod.selecionar(self.lineEdit.text()) == None:
            QMessageBox.about(ConsultaProdutos, "Erro", "Não encontrado")

    def abre_janela_edit(self):
        row = self.tabelaConsultaProdutos.currentRow()
        id = self.tabelaConsultaProdutos.item(row, 0).text()
        lista = self.buscar_id_bd(int(id,))
        if lista:
            self.obj_edita.lineEdit.setText(str(lista[0][0]))
            self.obj_edita.lineNome.setText(str(lista[0][1]))
            self.obj_edita.lineDescricao.setText(str(lista[0][2]))
            self.obj_edita.lineQtd.setText(str(lista[0][3]))
            self.obj_edita.lineQtdMin.setText(str(lista[0][4]))
            self.obj_edita.lineValor.setText(str(lista[0][5]))
            self.obj_edita.show()
        else:
            QMessageBox.about(ConsultaProdutos(), "Erro", "Não foi possível alterar o produto")

    def buscar_id_bd(self, id):
        lista = self.cad_prod.selecionar(id)
        return lista

    def excluir(self):
        try:
            row = self.tabelaConsultaProdutos.currentRow()
            id = self.tabelaConsultaProdutos.item(row, 0).text()
            obj_db = cadProdutosDB.CadProdutosDB()
            obj_db.excluir(id,)
            QMessageBox.about(ConsultaProdutos(), "Exclusão", "Produto excluido com sucesso")
            self.tabelaConsultaProdutos.clear()
        except ValueError:
            QMessageBox.about(ConsultaProdutos(), "Erro", "Não foi possível excluir o produto selecionado")

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
