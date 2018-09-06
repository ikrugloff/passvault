#Графический интерфейс пользователского окна регистрации
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from registration_page_ui import *


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MyWin()
        self.ui.setupUi(self)
        # self.ui.pushButtonSave.clicked.connect(self.stop)
        # self.ui.pushButtonClose.clicked.connect(self.close)  #   Удалить при рефакторинге
        # self.ui.actionExit.triggered.connect(self.close)  #   Удалить при рефакторинге

    # def stop(self):        # убрать эту функцию. Избыточно. Удалить при рефакторинге
        # self.terminate()

    def closeEvent(self, e):    # Функция открытия диалогового окна для подтверждения закрытия окна регистрации
        result = QtWidgets.QMessageBox.question(self, "ConfirmDIalog", "Really quit?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    # myapp = uic.loadUi('registration_page.ui')
    # print(myapp.pushButtonClose)
    myapp.show()
    sys.exit(app.exec_())
