# Преобразование файлов из ui  в py
# $ pyuic5 C:\Project\registration_page.ui -o C:\Project\registration_page_ui.py -x

# Графический интерфейс пользователского окна регистрации
import sys, os, time  # Не помню, так можно импортировать или нет. В сети вижу, что люди так делают импорты
import sqlalchemy, sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox

import registration_page_ui
import crypt_db


class RegWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = registration_page_ui.Ui_reg_page()
        self.ui.setupUi(self)
        self.ui.pushButtonSave.clicked.connect(self.save_to_db)

    def closeEvent(self, e):  # Функция открытия диалогового окна для подтверждения закрытия окна регистрации
        result = QtWidgets.QMessageBox.question(self, "ConfirmDIalog", "Really quit?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()

    def save_to_db(self):
        usernameguess = self.ui.emailInput.text()
        passwordguess = self.ui.pasInput.text()
        # TODO:
        # Проверка, если такая учетная запись существует, то вывыодить сообщение об ошибке
        # if usernameguess == USERNAME and passwordguess == PASSWORD:
        #     QMessageBox.question(self, 'Wrong login', f'\n This login and password already exists!\n', QMessageBox.Ok)
        # Проверка если поля пустые
        if (len(usernameguess) == 0 and len(passwordguess) == 0) or (
                (len(usernameguess) == 0 or len(passwordguess)) == 0):
            QMessageBox.question(self, 'Empty login or password', f'\n Please, enter login and password\n',
                                 QMessageBox.Ok)
        else:
            QMessageBox.question(self, 'Success', f'\n These login and password saved to DB!\n', QMessageBox.Ok)
            password = crypt_db.encrypt(passwordguess).decode('utf-8')
            crypt_db.create_master_password(password)

            self.close()
            os.system('python core_gui.py')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    reg_page = RegWindow()
    reg_page.show()
    sys.exit(app.exec_())
