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
            QMessageBox.question(self, 'Wrong login', f'\n This login and password already exists!\n', QMessageBox.Ok)
        # Проверка если поля пустые
        elif (len(usernameguess) == 0 and len(passwordguess) == 0) or (
                (len(usernameguess) == 0 or len(passwordguess)) == 0):
            QMessageBox.question(self, 'Empty login or password', f'\n Please, enter login and password\n',
                                 QMessageBox.Ok)
        # Сохранений в БД логина и пароля
        else:
            # QMessageBox.question(self, 'Success', f'\n These login and password saved to DB!\n', QMessageBox.Ok)
            # login = crypt_db.encrypt(usernameguess)
            # password = crypt_db.encrypt(passwordguess)
            # conn = sqlalchemy.create_engine('sqlite:///vault.db')
            # sql_1 = 'UPDATE master SET login=? WHERE id = 1'
            # sql_2 = 'UPDATE master SET password=? WHERE id = 1'
            # rows = conn.execute(sql_1, login)
            # rows = conn.execute(sql_2, password)
            # self.close()
            # os.system('main_page.py')
            pass


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


# Генератор паролей
# import os, random, string
# length = 10
# chars = string.ascii_letters + string.digits + '!@#$%^&*()'
# random.seed = (os.urandom(1024))
# print ''.join(random.choice(chars) for i in range(length))
# Gimli = gAAAAABblDQYBbTiNouho6zLrduHqjrenUJm9UDbEXmTiEBGbMyS6K7N2bYDbBO-roAftaLiyQgHdGlaFqw3hDQ-PGlo7s94aw==
# ring = gAAAAABbm9X2-tFinGRksbcAR_yiQ6DL5pY6ytUk6RyyozZ_TTuPXhJZao8SG7uS-CL143QZtgOtubmqhKuH6m7PPYMAjb7x0A==
