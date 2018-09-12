# Преобразование файлов из ui  в py
# $ pyuic5 C:\Project\registration_page.ui -o C:\Project\registration_page_ui.py -x

# Графический интерфейс пользователского окна регистрации

import sys
import os
import time
import sqlalchemy
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox

import registration_page_ui
# import core
import crypt_db
import sqlite3

USERNAME = crypt_db.get_master_login()
PASSWORD = crypt_db.get_master_pass()


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
        # Проверка, если такая учетная запись существует, то вывыодить сообщение об ошибке
        if usernameguess == USERNAME and passwordguess == PASSWORD:
            QMessageBox.question(self, 'Wrong login', f'\n This login already exists!\n', QMessageBox.Ok)

        elif len(usernameguess) == 0 and len(passwordguess) or ((len(usernameguess) == 0 and len(passwordguess)) == 0):
            QMessageBox.question(self, 'Empty login or password', f'\n Please, enter login and password\n',
                                 QMessageBox.Ok)

        # else:
        #     conn = sqlalchemy.create_engine('sqlite:///vault.db')
        # sql = 'INSERT into master values(?)'
        # rows = conn.execute(sql, usernameguess)
        # QMessageBox.question(self, 'Approved', '\nYour password saved!', QMessageBox.Ok)
        # self.close()
        # os.system('login_page.py')  # Пока временно поставил открытие странийы авторизации


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
reg_page = RegWindow()
reg_page.show()
sys.exit(app.exec_())

# Валидация правильности введеной почты
# import re
# def check_valid_email(email):
#     if len(email) > 7:
#         if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
#             return True
#     return False
#
#
# if check_valid_email("my.email@gmail.com") == True:
#     print("This is a valid email address")
# else:
#     print("This is not a valid email address")
