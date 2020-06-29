import  sys
from Interface import controller
from PyQt5 import QtWidgets, QtCore


def main():
    app = QtWidgets.QApplication(sys.argv)
    controlador = controller.Controller()
    controlador.show_main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()