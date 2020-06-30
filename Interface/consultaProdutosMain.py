from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from Interface import consultaProdutos_


class ConsultaProdutos(QMainWindow, consultaProdutos_.Ui_MainWindow):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnPesquisar.clicked.connect(self.pesquisar)
        self.actionsair.triggered.connect(self.sair)

    def pesquisar(self):
        self.switch_window.emit()

    def sair(self):
        self.switch_window.emit()