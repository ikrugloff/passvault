#Графический интерфейс пользователского окна регистрации
import sys
from PyQt5 import QtWidgets
from PyQt5 import uic


app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi('registration_page.ui')
print(window.pushButton)
window.show()

def my_f():
    pass

sys.exit(app.exec_())
