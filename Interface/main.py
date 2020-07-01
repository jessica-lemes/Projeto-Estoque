import sys
from PyQt5 import QtWidgets
from Interface import home_menus


def main():
    app = QtWidgets.QApplication(sys.argv)
    principal = home_menus.HomeMain()
    principal.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()