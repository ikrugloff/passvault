import sys
import os
import string
import random

import sqlalchemy

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import add_resource_page_ui
import crypt_db


class AddPassword(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = add_resource_page_ui.Ui_add_resource_page()
        self.ui.setupUi(self)
        self.ui.save_button.clicked.connect(self.add_new_string)
        self.ui.generate_pas_button.clicked.connect(self.gen_password)
        self.ui.cancel_button.clicked.connect(self.close_window)

    def add_new_string(self):
        website = self.ui.resource_input.text()
        login = self.ui.login_input.text()
        password = self.ui.pas_input.text()

        QMessageBox.question(self, 'Success', f'\n These credentials were saved to DB!\n', QMessageBox.Ok)
        conn = sqlalchemy.create_engine('sqlite:///vault.db')
        passw = crypt_db.encrypt(password).decode('utf-8')
        web = crypt_db.encrypt(website).decode('utf-8')
        log = crypt_db.encrypt(login).decode('utf-8')

        sql = 'INSERT INTO passwords (service, login, password) Values (?, ?, ?)'
        rows = conn.execute(sql, web, log, passw)
        self.close()
        os.system('python main_page.py')

    def close_window(self):  # функция закрытия окна добавления пароля при нажатии на кнопку Cancel
        self.close()
        os.system('python main_page.py')

    def gen_password(self):  # Функция генерации пароля
        length = 10
        chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        random.seed = (os.urandom(1024))
        generated_password = (''.join(random.choice(chars) for i in range(length)))
        self.ui.pas_input.setText(str(generated_password))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    add_pass = AddPassword()
    add_pass.show()

    sys.exit(app.exec_())
