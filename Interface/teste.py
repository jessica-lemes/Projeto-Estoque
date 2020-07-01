import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.central_widget = QWidget()
        self.grid = QGridLayout(self.central_widget)

        self.btn_abrir_janela = QPushButton('Clique em mim')
        self.btn_abrir_janela.setStyleSheet('font-size: 40px;')
        self.grid.addWidget(self.btn_abrir_janela, 0, 0, 1, 1)

        self.btn_abrir_janela.clicked.connect(self.abrir_janela)

        self.setCentralWidget(self.central_widget)

    def abrir_janela(self):
        self.janela_filha = Janela(self)
        self.janela_filha.show()

        self.btn_fechar_janela = QPushButton('Feche a janela')
        self.btn_fechar_janela.setStyleSheet('font-size: 40px;')
        self.grid.addWidget(self.btn_fechar_janela, 1, 0, 1, 1)

        self.btn_fechar_janela.clicked.connect(self.fechar_janela)

    def fechar_janela(self):
        self.janela_filha.fechar()
        self.btn_fechar_janela.deleteLater()


class Janela(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.central_widget = QWidget()
        self.grid = QGridLayout(self.central_widget)
        self.janela_principal = parent

        self.botao = QPushButton('Muda cor na janela principal')
        self.botao.setStyleSheet('font-size: 40px;')
        self.grid.addWidget(self.botao, 0, 0, 1, 1)

        self.botao.clicked.connect(
            self.muda_botao_da_janela_principal
        )

        self.setCentralWidget(self.central_widget)

    def muda_botao_da_janela_principal(self):
        self.janela_principal.btn_abrir_janela.setStyleSheet(
            'font-size: 40px; background: red;'
        )

    def fechar(self):
        self.close()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()