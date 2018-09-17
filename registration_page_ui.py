# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Project\registration_page.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_reg_page(object):
    def setupUi(self, RegWindow):
        RegWindow.setObjectName("RegWindow")
        RegWindow.setEnabled(True)
        RegWindow.resize(830, 501)
        RegWindow.setMinimumSize(QtCore.QSize(830, 501))
        RegWindow.setMaximumSize(QtCore.QSize(830, 501))
        self.centralwidget = QtWidgets.QWidget(RegWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setEnabled(True)
        self.verticalFrame.setGeometry(QtCore.QRect(0, 0, 830, 501))
        self.verticalFrame.setMinimumSize(QtCore.QSize(100, 100))
        self.verticalFrame.setMaximumSize(QtCore.QSize(830, 501))
        self.verticalFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalFrame.setObjectName("verticalFrame")
        self.label_3 = QtWidgets.QLabel(self.verticalFrame)
        self.label_3.setGeometry(QtCore.QRect(100, 140, 350, 30))
        self.label_3.setMaximumSize(QtCore.QSize(350, 30))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.verticalFrame)
        self.label_2.setGeometry(QtCore.QRect(100, 120, 158, 17))
        self.label_2.setMaximumSize(QtCore.QSize(350, 30))
        self.label_2.setObjectName("label_2")
        self.pushButtonSave = QtWidgets.QPushButton(self.verticalFrame)
        self.pushButtonSave.setGeometry(QtCore.QRect(700, 430, 81, 29))
        self.pushButtonSave.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.formFrame = QtWidgets.QFrame(self.verticalFrame)
        self.formFrame.setGeometry(QtCore.QRect(0, 410, 830, 90))
        self.formFrame.setMaximumSize(QtCore.QSize(830, 90))
        self.formFrame.setStyleSheet("background-color: rgb(194, 255, 235);\n"
"")
        self.formFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.formFrame.setObjectName("formFrame")
        self.formLayout = QtWidgets.QFormLayout(self.formFrame)
        self.formLayout.setObjectName("formLayout")
        self.formFrame_2 = QtWidgets.QFrame(self.verticalFrame)
        self.formFrame_2.setEnabled(True)
        self.formFrame_2.setGeometry(QtCore.QRect(0, 0, 830, 90))
        self.formFrame_2.setMaximumSize(QtCore.QSize(830, 90))
        self.formFrame_2.setStyleSheet("background-color: rgb(194, 255, 235);\n"
"")
        self.formFrame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.formFrame_2.setObjectName("formFrame_2")
        self.label_main = QtWidgets.QLabel(self.verticalFrame)
        self.label_main.setGeometry(QtCore.QRect(20, 10, 798, 37))
        self.label_main.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(194, 255, 235);\n"
"")
        self.label_main.setObjectName("label_main")
        self.label_little = QtWidgets.QLabel(self.verticalFrame)
        self.label_little.setGeometry(QtCore.QRect(10, 20, 61, 20))
        self.label_little.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(194, 255, 235);")
        self.label_little.setObjectName("label_little")
        self.pasWrapper = QtWidgets.QWidget(self.verticalFrame)
        self.pasWrapper.setGeometry(QtCore.QRect(100, 280, 351, 61))
        self.pasWrapper.setProperty("lineEdit_3", "")
        self.pasWrapper.setObjectName("pasWrapper")
        self.pasInput = QtWidgets.QLineEdit(self.pasWrapper)
        self.pasInput.setEnabled(True)
        self.pasInput.setGeometry(QtCore.QRect(0, 10, 351, 23))
        self.pasInput.setObjectName("pasInput")
        self.emailWrapper = QtWidgets.QWidget(self.verticalFrame)
        self.emailWrapper.setGeometry(QtCore.QRect(100, 190, 351, 61))
        self.emailWrapper.setProperty("lineEdit_3", "")
        self.emailWrapper.setObjectName("emailWrapper")
        self.emailInput = QtWidgets.QLineEdit(self.emailWrapper)
        self.emailInput.setGeometry(QtCore.QRect(0, 20, 351, 21))
        self.emailInput.setObjectName("emailInput")
        self.formFrame_2.raise_()
        self.label_main.raise_()
        self.formFrame.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.pushButtonSave.raise_()
        self.label_little.raise_()
        self.pasWrapper.raise_()
        self.emailWrapper.raise_()
        RegWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegWindow)
        QtCore.QMetaObject.connectSlotsByName(RegWindow)

    def retranslateUi(self, RegWindow):
        _translate = QtCore.QCoreApplication.translate
        RegWindow.setWindowTitle(_translate("RegWindow", "MyWin"))
        self.label_3.setText(_translate("RegWindow", "An email and strong password are all you need to get started."))
        self.label_2.setText(_translate("RegWindow", "Create your free account "))
        self.pushButtonSave.setText(_translate("RegWindow", "Save"))
        self.label_main.setText(_translate("RegWindow", "           Welcome to PassVault"))
        self.label_little.setText(_translate("RegWindow", "PassVault"))
        self.pasInput.setText(_translate("RegWindow", "Create a strong password"))
        self.emailInput.setText(_translate("RegWindow", "Enter your email"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegWindow = QtWidgets.QMainWindow()
    ui = Ui_RegWindow()
    ui.setupUi(RegWindow)
    RegWindow.show()
    sys.exit(app.exec_())

