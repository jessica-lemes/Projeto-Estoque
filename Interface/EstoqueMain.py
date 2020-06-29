from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.Qt import QTableWidgetItem
from Banco.db_estoque import Querys

app=QtWidgets.QApplication([])

comandos_db_usuarios = Querys('estoque.db')

def botao_cons_voltar():
    telaConsEstoque.close()
    telaHome.show()

def botao_pesquisar():

    nome = telaConsEstoque.lineProduto.text()
    resultado = pesquisar_banco(nome)

    l = 0
    c = 0
    for item in resultado:
        c=0
        for colItem in item:
            newItem = QTableWidgetItem(str(colItem))
            telaConsEstoque.tableWidget.setItem(l,c,newItem)
            c += 1
        l += 1
    telaConsEstoque.lineProduto.setText('')

def pesquisar_banco(nome):
    pesquisa = Querys.buscar_banco(Querys('estoque.db'), nome)
    return pesquisa

def botao_editar():
    row = telaConsEstoque.tableWidget.currentRow()
    id = telaConsEstoque.tableWidget.item(row, 0).text()
    lista = buscar_id_bd(int(id))

    telaAtualizaEstoque.lineCodigo.setText(str(lista[0][0]))
    telaAtualizaEstoque.lineNomeProduto.setText(str(lista[0][1]))
    telaAtualizaEstoque.lineDescricao.setText(str(lista[0][2]))
    telaAtualizaEstoque.labelQntEstoque.setText(str(lista[0][3]))
    telaAtualizaEstoque.lineAtualizar.setText(str(lista[0][3]))


    telaConsEstoque.close()
    telaAtualizaEstoque.show()

def buscar_id_bd(id):
    lista = Querys.selecionar_id(comandos_db_usuarios, id)
    return lista

def botao_atual_voltar():
    telaAtualizaEstoque.close()
    telaConsEstoque.tableWidget.clearContents()
    telaConsEstoque.show()

def botao_atual_limpar():
    telaAtualizaEstoque.lineCodigo.setText('')
    telaAtualizaEstoque.lineNomeProduto.setText('')
    telaAtualizaEstoque.lineDescricao.setText('')
    telaAtualizaEstoque.labelQntEstoque.setText('')
    telaAtualizaEstoque.lineAtualizar.setText('')

def botao_salvar_atual():
    id = telaAtualizaEstoque.lineCodigo.text()
    qtde_estoque = telaAtualizaEstoque.lineAtualizar.text()
    salvaAlteracaoEstoque(qtde_estoque, id)
    botao_atual_limpar()

def salvaAlteracaoEstoque(qtde_estoque, id):
    if qtde_estoque == "":
        QMessageBox.about(telaAtualizaEstoque,"Alerta","Obrigatório o preenchimento do campo.")
    else:
        Querys.atualizar_estoque(comandos_db_usuarios, qtde_estoque, id)
        QMessageBox.about(telaAtualizaEstoque,"Mensagem","Estoque alterado com sucesso.")


telaConsEstoque = uic.loadUi("consultarEstoque.ui")
telaConsEstoque.btnVoltar.clicked.connect(botao_cons_voltar)
telaConsEstoque.btnPesquisar.clicked.connect(botao_pesquisar)
telaConsEstoque.btnEditar.clicked.connect(botao_editar)

telaAtualizaEstoque = uic.loadUi("editarEstoque.ui")
telaAtualizaEstoque.btnVoltar.clicked.connect(botao_atual_voltar)
telaAtualizaEstoque.btnLimpar.clicked.connect(botao_atual_limpar)
telaAtualizaEstoque.btnSalvar.clicked.connect(botao_salvar_atual)



telaHome=uic.loadUi("Home.ui")
telaConsEstoque.show()
app.exec()