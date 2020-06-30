import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore
from Interface.Home import *
from Interface import controller


class HomeMain(QMainWindow, Ui_Home):

    switch_window = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(HomeMain, self).__init__(parent)
        super().setupUi(self)

        self.CadastrarProdutos.triggered.connect(self.switch_cad_produtos)
        self.ConsultarProdutos.triggered.connect(self.switch_cons_produtos)


    def switch_cad_produtos(self):
        self.switch_window.emit()

    def switch_cons_produtos(self):
        self.switch_window.emit()

