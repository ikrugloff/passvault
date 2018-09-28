# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_resource_page.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_add_resource_page(object):
    def setupUi(self, add_resource_page):
        add_resource_page.setObjectName("add_resource_page")
        add_resource_page.setEnabled(True)
        add_resource_page.resize(301, 502)
        add_resource_page.setMinimumSize(QtCore.QSize(301, 502))
        add_resource_page.setMaximumSize(QtCore.QSize(301, 502))
        self.centralwidget = QtWidgets.QWidget(add_resource_page)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setEnabled(True)
        self.verticalFrame.setGeometry(QtCore.QRect(0, 0, 301, 502))
        self.verticalFrame.setMinimumSize(QtCore.QSize(301, 502))
        self.verticalFrame.setMaximumSize(QtCore.QSize(301, 502))
        self.verticalFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalFrame.setObjectName("verticalFrame")
        self.header = QtWidgets.QFrame(self.verticalFrame)
        self.header.setGeometry(QtCore.QRect(0, 0, 301, 151))
        self.header.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.logo = QtWidgets.QLabel(self.header)
        self.logo.setGeometry(QtCore.QRect(10, 20, 281, 71))
        self.logo.setStyleSheet("background-color: rgb(192, 89, 255);")
        self.logo.setObjectName("logo")
        self.widget = QtWidgets.QWidget(self.verticalFrame)
        self.widget.setGeometry(QtCore.QRect(0, 150, 301, 271))
        self.widget.setObjectName("widget")
        self.login_wrapper = QtWidgets.QWidget(self.widget)
        self.login_wrapper.setGeometry(QtCore.QRect(10, 90, 291, 61))
        self.login_wrapper.setProperty("lineEdit_3", "")
        self.login_wrapper.setObjectName("login_wrapper")
        self.login_input = QtWidgets.QLineEdit(self.login_wrapper)
        self.login_input.setGeometry(QtCore.QRect(10, 30, 241, 21))
        self.login_input.setObjectName("login_input")
        self.login_label = QtWidgets.QLabel(self.login_wrapper)
        self.login_label.setGeometry(QtCore.QRect(10, 10, 241, 16))
        self.login_label.setObjectName("login_label")
        self.pas_wrapper = QtWidgets.QWidget(self.widget)
        self.pas_wrapper.setGeometry(QtCore.QRect(10, 170, 291, 61))
        self.pas_wrapper.setProperty("lineEdit_3", "")
        self.pas_wrapper.setObjectName("pas_wrapper")
        self.pas_input = QtWidgets.QLineEdit(self.pas_wrapper)
        self.pas_input.setGeometry(QtCore.QRect(10, 30, 241, 21))
        self.pas_input.setObjectName("pas_input")
        self.pas_label = QtWidgets.QLabel(self.pas_wrapper)
        self.pas_label.setGeometry(QtCore.QRect(10, 10, 231, 16))
        self.pas_label.setObjectName("pas_label")
        self.resource_wrapper = QtWidgets.QWidget(self.widget)
        self.resource_wrapper.setGeometry(QtCore.QRect(10, 10, 291, 61))
        self.resource_wrapper.setProperty("lineEdit_3", "")
        self.resource_wrapper.setObjectName("resource_wrapper")
        self.resource_input = QtWidgets.QLineEdit(self.resource_wrapper)
        self.resource_input.setGeometry(QtCore.QRect(10, 30, 241, 21))
        self.resource_input.setObjectName("resource_input")
        self.resource_label = QtWidgets.QLabel(self.resource_wrapper)
        self.resource_label.setGeometry(QtCore.QRect(10, 10, 241, 16))
        self.resource_label.setObjectName("resource_label")
        self.generate_pas_button = QtWidgets.QPushButton(self.widget)
        self.generate_pas_button.setGeometry(QtCore.QRect(170, 240, 91, 21))
        self.generate_pas_button.setObjectName("generate_pas_button")
        self.footer = QtWidgets.QWidget(self.verticalFrame)
        self.footer.setGeometry(QtCore.QRect(0, 420, 301, 101))
        self.footer.setObjectName("footer")
        self.save_button = QtWidgets.QPushButton(self.footer)
        self.save_button.setGeometry(QtCore.QRect(115, 20, 71, 21))
        self.save_button.setStyleSheet("background-color: rgb(177, 177, 177);")
        self.save_button.setObjectName("save_button")
        self.cancel_button = QtWidgets.QPushButton(self.footer)
        self.cancel_button.setGeometry(QtCore.QRect(115, 50, 71, 21))
        self.cancel_button.setObjectName("cancel_button")
        add_resource_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(add_resource_page)
        QtCore.QMetaObject.connectSlotsByName(add_resource_page)

    def retranslateUi(self, add_resource_page):
        _translate = QtCore.QCoreApplication.translate
        add_resource_page.setWindowTitle(_translate("add_resource_page", "MyWin"))
        self.logo.setText(_translate("add_resource_page", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">PassVault</span></p></body></html>"))
        self.login_input.setText(_translate("add_resource_page", "Enter your login"))
        self.login_label.setText(_translate("add_resource_page", "Login"))
        self.pas_input.setText(_translate("add_resource_page", "Enter your password"))
        self.pas_label.setText(_translate("add_resource_page", "Password"))
        self.resource_input.setText(_translate("add_resource_page", "Enter the resource"))
        self.resource_label.setText(_translate("add_resource_page", "Resource"))
        self.generate_pas_button.setText(_translate("add_resource_page", "Generate password"))
        self.save_button.setText(_translate("add_resource_page", "Save"))
        self.cancel_button.setText(_translate("add_resource_page", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_resource_page = QtWidgets.QMainWindow()
    ui = Ui_add_resource_page()
    ui.setupUi(add_resource_page)
    add_resource_page.show()
    sys.exit(app.exec_())

