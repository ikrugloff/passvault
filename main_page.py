import sys
import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from main_page_ui import *
import crypt_db

USERNAME = crypt_db.get_master_login()
PASSWORD = crypt_db.get_master_pass()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.addNewPas.clicked.connect(self.change_window)

    def load_data(self):
        self.ui.resource_list.clear()
        self.ui.login_list.clear()
        self.ui.pas_list.clear()

        for output in crypt_db.output():
            self.ui.resource_list.addItem(output['Resource_name'])
            self.ui.login_list.addItem(output['Login'])
            self.ui.pas_list.addItem(output['Password'])

    def change_window(self):
        self.close()
        os.system('python add_password.py')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main_page = MainWindow()
    main_page.show()
    main_page.load_data()

    sys.exit(app.exec_())
