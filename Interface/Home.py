# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(600, 600)
        Home.setMinimumSize(QtCore.QSize(600, 600))
        Home.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(Home)
        self.centralwidget.setObjectName("centralwidget")
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setGeometry(QtCore.QRect(0, 10, 600, 600))
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.logo = QtWidgets.QLabel(self.content)
        self.logo.setGeometry(QtCore.QRect(150, 80, 300, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.logo.setFont(font)
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(self.content)
        self.label.setGeometry(QtCore.QRect(40, 230, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.content)
        self.listWidget.setGeometry(QtCore.QRect(40, 260, 521, 261))
        self.listWidget.setObjectName("listWidget")
        Home.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Home)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")
        self.menuEstoque = QtWidgets.QMenu(self.menubar)
        self.menuEstoque.setObjectName("menuEstoque")
        self.menuUsu_rios = QtWidgets.QMenu(self.menubar)
        self.menuUsu_rios.setObjectName("menuUsu_rios")
        self.menuProdutos = QtWidgets.QMenu(self.menubar)
        self.menuProdutos.setObjectName("menuProdutos")
        self.menuMovimenta_o = QtWidgets.QMenu(self.menubar)
        self.menuMovimenta_o.setObjectName("menuMovimenta_o")
        self.menuLogout = QtWidgets.QMenu(self.menubar)
        self.menuLogout.setObjectName("menuLogout")
        Home.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Home)
        self.statusbar.setObjectName("statusbar")
        Home.setStatusBar(self.statusbar)
        self.PaginaInicial = QtWidgets.QAction(Home)
        self.PaginaInicial.setObjectName("PaginaInicial")
        self.ConsultarEstoque = QtWidgets.QAction(Home)
        self.ConsultarEstoque.setObjectName("ConsultarEstoque")
        self.ConsultarUsuario = QtWidgets.QAction(Home)
        self.ConsultarUsuario.setObjectName("ConsultarUsuario")
        self.CadastrarUsuario = QtWidgets.QAction(Home)
        self.CadastrarUsuario.setObjectName("CadastrarUsuario")
        self.ConsultarProdutos = QtWidgets.QAction(Home)
        self.ConsultarProdutos.setObjectName("ConsultarProdutos")
        self.ConsultarMovimentacao = QtWidgets.QAction(Home)
        self.ConsultarMovimentacao.setObjectName("ConsultarMovimentacao")
        self.Logout = QtWidgets.QAction(Home)
        self.Logout.setObjectName("Logout")
        self.CadastrarProdutos = QtWidgets.QAction(Home)
        self.CadastrarProdutos.setObjectName("CadastrarProdutos")
        self.menuHome.addSeparator()
        self.menuHome.addAction(self.PaginaInicial)
        self.menuEstoque.addAction(self.ConsultarEstoque)
        self.menuUsu_rios.addAction(self.ConsultarUsuario)
        self.menuUsu_rios.addAction(self.CadastrarUsuario)
        self.menuProdutos.addAction(self.ConsultarProdutos)
        self.menuProdutos.addAction(self.CadastrarProdutos)
        self.menuMovimenta_o.addAction(self.ConsultarMovimentacao)
        self.menuLogout.addAction(self.Logout)
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuEstoque.menuAction())
        self.menubar.addAction(self.menuUsu_rios.menuAction())
        self.menubar.addAction(self.menuProdutos.menuAction())
        self.menubar.addAction(self.menuMovimenta_o.menuAction())
        self.menubar.addAction(self.menuLogout.menuAction())

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "MainWindow"))
        self.logo.setText(_translate("Home", "Projeto Estoque"))
        self.label.setText(_translate("Home", "Status do estoque:"))
        self.menuHome.setTitle(_translate("Home", "Home"))
        self.menuEstoque.setTitle(_translate("Home", "Estoque"))
        self.menuUsu_rios.setTitle(_translate("Home", "Usuários"))
        self.menuProdutos.setTitle(_translate("Home", "Produtos"))
        self.menuMovimenta_o.setTitle(_translate("Home", "Movimentação"))
        self.menuLogout.setTitle(_translate("Home", "Logout"))
        self.PaginaInicial.setText(_translate("Home", "Pagina Inicial"))
        self.ConsultarEstoque.setText(_translate("Home", "Consultar"))
        self.ConsultarUsuario.setText(_translate("Home", "Consultar"))
        self.CadastrarUsuario.setText(_translate("Home", "Cadastrar Novo"))
        self.ConsultarProdutos.setText(_translate("Home", "Consultar"))
        self.ConsultarMovimentacao.setText(_translate("Home", "Consultar"))
        self.Logout.setText(_translate("Home", "Sair"))
        self.CadastrarProdutos.setText(_translate("Home", "Cadastrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Home = QtWidgets.QMainWindow()
    ui = Ui_Home()
    ui.setupUi(Home)
    Home.show()
    sys.exit(app.exec_())

