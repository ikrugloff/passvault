# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration_page.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_registration_page(object):
    def setupUi(self, registration_page):
        registration_page.setObjectName("registration_page")
        registration_page.setEnabled(True)
        registration_page.resize(301, 502)
        registration_page.setMinimumSize(QtCore.QSize(301, 502))
        registration_page.setMaximumSize(QtCore.QSize(301, 502))
        self.centralwidget = QtWidgets.QWidget(registration_page)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setEnabled(True)
        self.verticalFrame.setGeometry(QtCore.QRect(0, 0, 301, 501))
        self.verticalFrame.setMinimumSize(QtCore.QSize(100, 100))
        self.verticalFrame.setMaximumSize(QtCore.QSize(830, 501))
        self.verticalFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalFrame.setObjectName("verticalFrame")
        self.pas_wrapper = QtWidgets.QWidget(self.verticalFrame)
        self.pas_wrapper.setGeometry(QtCore.QRect(10, 140, 291, 161))
        self.pas_wrapper.setProperty("lineEdit_3", "")
        self.pas_wrapper.setObjectName("pas_wrapper")
        self.pas_input = QtWidgets.QLineEdit(self.pas_wrapper)
        self.pas_input.setGeometry(QtCore.QRect(10, 120, 241, 21))
        self.pas_input.setObjectName("pas_input")
        self.label_7 = QtWidgets.QLabel(self.pas_wrapper)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 231, 16))
        self.label_7.setObjectName("label_7")
        self.greeting_label = QtWidgets.QLabel(self.pas_wrapper)
        self.greeting_label.setGeometry(QtCore.QRect(20, 0, 231, 91))
        self.greeting_label.setObjectName("greeting_label")
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
        self.footer = QtWidgets.QWidget(self.verticalFrame)
        self.footer.setGeometry(QtCore.QRect(0, 400, 301, 101))
        self.footer.setObjectName("footer")
        self.save_button = QtWidgets.QPushButton(self.footer)
        self.save_button.setGeometry(QtCore.QRect(115, 40, 71, 21))
        self.save_button.setStyleSheet("background-color: rgb(177, 177, 177);")
        self.save_button.setObjectName("save_button")
        registration_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(registration_page)
        QtCore.QMetaObject.connectSlotsByName(registration_page)

    def retranslateUi(self, registration_page):
        _translate = QtCore.QCoreApplication.translate
        registration_page.setWindowTitle(_translate("registration_page", "MyWin"))
        self.pas_input.setText(_translate("registration_page", "Enter your password"))
        self.label_7.setText(_translate("registration_page", "Password"))
        self.greeting_label.setText(_translate("registration_page", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Enter a password for Gimli</span></p></body></html>"))
        self.logo.setText(_translate("registration_page", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">PassVault</span></p></body></html>"))
        self.save_button.setText(_translate("registration_page", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registration_page = QtWidgets.QMainWindow()
    ui = Ui_registration_page()
    ui.setupUi(registration_page)
    registration_page.show()
    sys.exit(app.exec_())

