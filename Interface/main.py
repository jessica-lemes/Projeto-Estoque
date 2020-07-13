import sys
from PyQt5 import QtWidgets
from Interface import comandos_login

def main():
    app = QtWidgets.QApplication(sys.argv)
    principal = comandos_login.Login()
    principal.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()