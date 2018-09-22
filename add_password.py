"""
Статьи
http://qaru.site/questions/7301200/pyqt5-pass-a-value-dynamically-in-qlineedit-box-when-event-is-clicked

"""

import sys
import os
import string
import random

import sqlalchemy, sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox

import add_password_ui
import crypt_db


class AddPassword(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = add_password_ui.Ui_AddPass()
        self.ui.setupUi(self)
        self.ui.pushButtonOk.clicked.connect(self.add_new_string)
        self.ui.pushButtonGenerate.clicked.connect(self.gen_password)
        self.ui.pushButtonCancel.clicked.connect(self.close_window)

    def closeEvent(self, e):  # Функция открытия диалогового окна для подтверждения закрытия окна регистрации
        result = QtWidgets.QMessageBox.question(self, "ConfirmDIalog", "Really quit?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()

    def add_new_string(self):
        website = self.ui.emailInput_Website.text()
        login = self.ui.emailInput_Login.text()
        password = self.ui.pasInput_Password.text()

        QMessageBox.question(self, 'Success', f'\n These credentials were saved to DB!\n', QMessageBox.Ok)
        conn = sqlalchemy.create_engine('sqlite:///vault.db')
        passw = crypt_db.encrypt(password).decode('utf-8')
        web = crypt_db.encrypt(website).decode('utf-8')
        log = crypt_db.encrypt(login).decode('utf-8')

        sql = 'INSERT INTO passwords (service, login, password) Values (?, ?, ?)'
        rows = conn.execute(sql, web, log, passw)

    def close_window(self):  # функция закрытия окна добавления пароля при нажатии на кнопку Cancel
        self.close()
        os.system('python main_page.py')

    def gen_password(self):  # Функция генерации пароля
        length = 10
        chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        random.seed = (os.urandom(1024))
        generated_password = (''.join(random.choice(chars) for i in range(length)))
        # print(generated_password)
        self.ui.pasInput_Password.setText(str(generated_password))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    add_pass = AddPassword()
    add_pass.show()
    sys.exit(app.exec_())
