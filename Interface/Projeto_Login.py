# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Projeto_Login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(600, 500)
        Login.setMinimumSize(QtCore.QSize(600, 500))
        Login.setMaximumSize(QtCore.QSize(600, 500))
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setGeometry(QtCore.QRect(0, 0, 600, 500))
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.lblLogin = QtWidgets.QLabel(self.content)
        self.lblLogin.setGeometry(QtCore.QRect(250, 90, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblLogin.setFont(font)
        self.lblLogin.setObjectName("lblLogin")
        self.label = QtWidgets.QLabel(self.content)
        self.label.setGeometry(QtCore.QRect(120, 180, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.content)
        self.label_2.setGeometry(QtCore.QRect(130, 220, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtUsuario = QtWidgets.QLineEdit(self.content)
        self.txtUsuario.setGeometry(QtCore.QRect(180, 169, 271, 31))
        self.txtUsuario.setMaxLength(14)
        self.txtUsuario.setObjectName("txtUsuario")
        self.txtSenha = QtWidgets.QLineEdit(self.content)
        self.txtSenha.setGeometry(QtCore.QRect(180, 210, 271, 31))
        self.txtSenha.setMaxLength(16)
        self.txtSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtSenha.setObjectName("txtSenha")
        self.cbxEsqueciSenha = QtWidgets.QCheckBox(self.content)
        self.cbxEsqueciSenha.setGeometry(QtCore.QRect(190, 250, 131, 23))
        self.cbxEsqueciSenha.setObjectName("cbxEsqueciSenha")
        self.btnLogar = QtWidgets.QPushButton(self.content)
        self.btnLogar.setGeometry(QtCore.QRect(250, 320, 89, 25))
        self.btnLogar.setStyleSheet("QPushButton{\n"
"    background-color:#A9A9A9;\n"
"    border: 2px solid rgb(60,60,60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #C0C0C0;\n"
"    border: 2px solid #ffffff;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(250,230,0);\n"
"    border: 2px solid rgb(255,165,24);\n"
"    color: rgb(35,35,35);\n"
"}")
        self.btnLogar.setObjectName("btnLogar")
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "LOGIN"))
        self.lblLogin.setText(_translate("Login", "Login"))
        self.label.setText(_translate("Login", "Usuário"))
        self.label_2.setText(_translate("Login", "Senha"))
        self.txtUsuario.setPlaceholderText(_translate("Login", "Digite seu CPF"))
        self.txtSenha.setPlaceholderText(_translate("Login", "Digite a senha"))
        self.cbxEsqueciSenha.setText(_translate("Login", "Esqueci a senha"))
        self.btnLogar.setText(_translate("Login", "Entrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

