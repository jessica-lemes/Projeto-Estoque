# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editaProdutos.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editaProdutos(object):
    def setupUi(self, editaProdutos):
        editaProdutos.setObjectName("editaProdutos")
        editaProdutos.resize(530, 258)
        self.centralwidget = QtWidgets.QWidget(editaProdutos)
        self.centralwidget.setObjectName("centralwidget")
        self.lineNome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineNome.setGeometry(QtCore.QRect(96, 9, 381, 25))
        self.lineNome.setObjectName("lineNome")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 9, 42, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(9, 40, 66, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(9, 71, 81, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(9, 102, 51, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(9, 133, 36, 17))
        self.label_5.setObjectName("label_5")
        self.lineDescricao = QtWidgets.QLineEdit(self.centralwidget)
        self.lineDescricao.setGeometry(QtCore.QRect(96, 40, 381, 25))
        self.lineDescricao.setObjectName("lineDescricao")
        self.lineQtd = QtWidgets.QLineEdit(self.centralwidget)
        self.lineQtd.setGeometry(QtCore.QRect(96, 71, 381, 25))
        self.lineQtd.setObjectName("lineQtd")
        self.lineQtdMin = QtWidgets.QLineEdit(self.centralwidget)
        self.lineQtdMin.setGeometry(QtCore.QRect(96, 102, 381, 25))
        self.lineQtdMin.setObjectName("lineQtdMin")
        self.lineValor = QtWidgets.QLineEdit(self.centralwidget)
        self.lineValor.setGeometry(QtCore.QRect(96, 133, 381, 25))
        self.lineValor.setObjectName("lineValor")
        self.btnLimpar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpar.setGeometry(QtCore.QRect(300, 170, 80, 25))
        self.btnLimpar.setObjectName("btnLimpar")
        self.btnConfirmar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConfirmar.setGeometry(QtCore.QRect(90, 170, 80, 25))
        self.btnConfirmar.setObjectName("btnConfirmar")
        self.btnVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnVoltar.setGeometry(QtCore.QRect(190, 170, 89, 25))
        self.btnVoltar.setObjectName("btnVoltar")
        editaProdutos.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(editaProdutos)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 530, 22))
        self.menubar.setObjectName("menubar")
        self.menuProdutos = QtWidgets.QMenu(self.menubar)
        self.menuProdutos.setObjectName("menuProdutos")
        editaProdutos.setMenuBar(self.menubar)
        self.actionCadastrar = QtWidgets.QAction(editaProdutos)
        self.actionCadastrar.setObjectName("actionCadastrar")
        self.actionSair = QtWidgets.QAction(editaProdutos)
        self.actionSair.setObjectName("actionSair")
        self.actionConsultar = QtWidgets.QAction(editaProdutos)
        self.actionConsultar.setObjectName("actionConsultar")
        self.menuProdutos.addAction(self.actionConsultar)
        self.menuProdutos.addAction(self.actionSair)
        self.menubar.addAction(self.menuProdutos.menuAction())

        self.retranslateUi(editaProdutos)
        QtCore.QMetaObject.connectSlotsByName(editaProdutos)

    def retranslateUi(self, editaProdutos):
        _translate = QtCore.QCoreApplication.translate
        editaProdutos.setWindowTitle(_translate("editaProdutos", "Edição de Produtos"))
        self.label.setText(_translate("editaProdutos", "Nome"))
        self.label_2.setText(_translate("editaProdutos", "Descrição"))
        self.label_3.setText(_translate("editaProdutos", "Quantidade"))
        self.label_4.setText(_translate("editaProdutos", "Mínimo"))
        self.label_5.setText(_translate("editaProdutos", "Valor"))
        self.btnLimpar.setText(_translate("editaProdutos", "Limpar"))
        self.btnConfirmar.setText(_translate("editaProdutos", "Confirmar"))
        self.btnVoltar.setText(_translate("editaProdutos", "Voltar"))
        self.menuProdutos.setTitle(_translate("editaProdutos", "Produtos"))
        self.actionCadastrar.setText(_translate("editaProdutos", "Cadastrar"))
        self.actionSair.setText(_translate("editaProdutos", "Sair"))
        self.actionConsultar.setText(_translate("editaProdutos", "Consultar"))
