# Преобразование файлов из ui  в py
# $ pyuic5 C:\Project\registration_page.ui -o C:\Project\registration_page_ui.py -x
# Графический интерфейс пользователского окна регистрации

import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

import registration_page_ui
import crypt_db


class RegWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = registration_page_ui.Ui_registration_page()
        self.ui.setupUi(self)
        self.ui.save_button.clicked.connect(self.save_to_db)

    def closeEvent(self, e):  # Функция открытия диалогового окна для подтверждения закрытия окна регистрации

        result = QtWidgets.QMessageBox.question(
            self,
            "ConfirmDIalog",
            "Really quit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()

    def save_to_db(self):

        passwordguess = self.ui.pas_input.text()

        if len(passwordguess) == 0:
            QMessageBox.question(
                self,
                'Empty login or password',
                f'\n Please, enter login and password\n',
                QMessageBox.Ok
            )
        else:
            QMessageBox.question(
                self,
                'Success',
                f'\n These login and password saved to DB!\n',
                QMessageBox.Ok
            )
            password = crypt_db.encrypt(passwordguess).decode('utf-8')
            crypt_db.create_master_password(password)

            self.close()
            os.system('python start_script.py')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    reg_page = RegWindow()
    reg_page.show()
    sys.exit(app.exec_())
